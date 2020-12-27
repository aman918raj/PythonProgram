from airflow import DAG
from airflow.models import Variable
from airflow.operators import TriggerDagRunOperator
from airflow.operators.rxcorp_tsa import SFTPSensor
from datetime import timedelta, datetime
from airflow.operators import TriggerDagRunOperator
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {
    'owner': 'Airflow_Apac',
    'depends_on_past': False,
    'email': [Variable.get("envShortName_ph9_notification_email")],
    'start_date': datetime(2019, 8, 28, 14, 30, 0),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(dag_id='envShortName_ph_pck_add_attr_fl_wtchr',
          default_args=default_args,
          max_active_runs=1,
          concurrency=1,
          schedule_interval="*/5 * * * *",
          catchup=False)

sftp_conn = Variable.get("ph9_sftp_conn_string")
sftp_file_path = Variable.get("envShortName_ph9_sftp_add_attr_file_path")
local_file_path = Variable.get("envShortName_ph9_edgenode_path")
mfg_file_name = Variable.get("envShortName_ph9_add_attr_mfg_file_name")
cont_file_name = Variable.get("envShortName_ph9_add_attr_container_file_name")

task_sftp_mfg_file_sensor = SFTPSensor(task_id='sftp_mfg_file_sensor',
                                       sftp_conn_id='philippines_secureftp',
                                       filepath=sftp_file_path,
                                       filepattern=mfg_file_name,
                                       do_xcom_push=True,
                                       dag=dag)

task_sftp_cont_file_sensor = SFTPSensor(task_id='sftp_cont_file_sensor',
                                        sftp_conn_id='philippines_secureftp',
                                        filepath=sftp_file_path,
                                        filepattern=cont_file_name,
                                        do_xcom_push=True,
                                        dag=dag)

file_to_inprogress = """#!/bin/bash
mfg_file={{ ti.xcom_pull(task_ids="sftp_mfg_file_sensor", key="file_name") }}
container_file={{ ti.xcom_pull(task_ids="sftp_cont_file_sensor", key="file_name") }}
mfg_date=$(echo ${mfg_file} | awk -F"_" '{print $4}')
container_date=$(echo ${container_file} | awk -F"_" '{print $4}')
mfg_file_len=`echo $mfg_file | wc -c`
container_file_len=`echo $container_file | wc -c`

if [[ $mfg_date == $container_date ]] && [[ $mfg_file_len -gt 1 ]] && [[ $container_file_len -gt 1 ]]
then
sftp -b - """ + sftp_conn + """<<EOF 2>&1
rename """ + sftp_file_path + """/$mfg_file """ + sftp_file_path + """/inprogress/$mfg_file
rename """ + sftp_file_path + """/$container_file """ + sftp_file_path + """/inprogress/$container_file
bye
EOF
else
echo files not in same date
fi
"""

task_file_to_inprogress = SSHOperator(task_id='file_to_inprogress',
                                      ssh_conn_id='envShortName_ph9_edge_node_ssh',
                                      command=file_to_inprogress,
                                      do_xcom_push=True,
                                      dag=dag)


def pck_add_attr_trigger(context, dag_run_obj):
    task_instance = context["task_instance"]
    mfg_file = task_instance.xcom_pull(task_ids='sftp_mfg_file_sensor', key='file_name').strip()
    cont_file = task_instance.xcom_pull(task_ids='sftp_cont_file_sensor', key='file_name').strip()
    print("mfg_file : " + mfg_file)
    print("cont_file : " + cont_file)
    if len(mfg_file) > 0 and len(cont_file) > 0:
        mfg_date = mfg_file.split("_")[3]
        cont_date = cont_file.split("_")[3]
        if mfg_date == cont_date:
            dag_run_obj.payload = {
            "mfg_file": "{}".format(mfg_file),
            "cont_file": "{}".format(cont_file)
            }
            return dag_run_obj

task_pck_add_attr_trigger = TriggerDagRunOperator(task_id='pck_add_attr_trigger',
                                                  trigger_dag_id="envShortName_ph_pck_add_attr_process",
                                                  python_callable=pck_add_attr_trigger,
                                                  dag=dag)

task_sftp_mfg_file_sensor >> task_sftp_cont_file_sensor >> task_file_to_inprogress >> task_pck_add_attr_trigger