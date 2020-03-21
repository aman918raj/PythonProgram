import os
import fnmatch

from airflow.contrib.hooks.sftp_hook import SFTPHook
from airflow.operators.sensors import BaseSensorOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException


class SFTPSensor(BaseSensorOperator):
    """
    #Airflow sftp sensor monitors a particular location for a particular file pattern
    """
    @apply_defaults
    def __init__(self, filepath, filepattern, sftp_conn_id='sftp_default', *args, **kwargs):
        super(SFTPSensor, self).__init__(*args, **kwargs)
        self.filepath = filepath
        self.filepattern = filepattern
        self.hook = SFTPHook(sftp_conn_id)

    def poke(self, context):
        full_path = self.filepath
        dict_files = {}
        oldest_file = ""
        files = self.hook.list_directory(full_path)
        pattern = self.filepattern

        for file in files:
            if not fnmatch.fnmatch(file, pattern):
                self.log.info(file)
                self.log.info(pattern)
            else:
                self.log.info("File found {}".format(file))
                dict_files[int(self.hook.get_mod_time(full_path + "/" + file))] = file

        print("files found with modified time : {0}".format(dict_files))
        length_dict = len(dict_files)
        if length_dict > 0:
            dict_of_files_sorted = sorted(list(dict_files.keys()))
            oldest_file = dict_files[dict_of_files_sorted[0]]
        context["task_instance"].xcom_push("file_name", oldest_file)
        self.log.info("xcom_pushed : {}".format(oldest_file))
        return True
