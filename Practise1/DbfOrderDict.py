from dbfread import DBF
#import csv
import sys
import os
import csv
#from pyspark.sql import *
#from pyspark import SparkContext, SparkConf
#from pyspark import *
#import pyspark.sql.functions as F
import pandas as pd
import subprocess
import xlrd

def test():
    print("test")
    def inside_test():
        print("inside test")
    inside_test()
def run_cmd(args_list):
    print('Running system command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output, s_err

def write_to_csv(lst_rec):

    with open(output_path, "w",newline="",encoding='utf-16') as f:
        writer = csv.writer(f, delimiter=str("@"))
        writer.writerows(lst_rec)

def convert_rec(dbf, lst_of_key,lst_of_value):
    i = 0
    for records in dbf:
        lst_value = list(records.values())
        lst_of_value.insert(i,lst_value)
        if i == 0:
            for key in records.keys():
                lst_of_key.append(key)
        i += 1
        if(i < 30):
            print(lst_value[5])
    return lst_of_key,lst_of_value

test()
input_path = "C:/Users/aman.raj/Documents/BCN0220.DBF"
#input_path = str(sys.argv[1])
print("input Path : "+ input_path )
output_path = "C:/Users/aman.raj/Documents/out/BCN0220.csv"
#output_path = os.path.splitext(input_path)[0]+".csv"
print(output_path)
#hdfs_path = str(sys.argv[2])
dbf = DBF(input_path,encoding='iso-8859-1',ignore_missing_memofile=True)
lst_of_key = []
lst_of_value=[[]]
print(dbf)
lst_of_key,lst_of_value=convert_rec(dbf,lst_of_key,lst_of_value)
write_to_csv(lst_of_value)
#(ret, out, err)=run_cmd(['hdfs','dfs','-put','output_path',hdfs_path])
#(ret, out, err)= run_cmd(['rm', 'input_path'])
#(ret, out, err)= run_cmd(['rm', 'output_path'])

#convert_rec(dbf, lst_of_key,lst_of_value)
#print(lst_of_key)
#print(lst_of_value)
#df = pd.DataFrame(dbf)
#df.to_csv("C:/Users/aman.raj/out/test.csv",index=False)
#hadoop_home = "HADOOP_HOME"
#hadoop_home_dir = "C:/Users/aman.raj/hadoop/"
#win_util = "winutils.exe"

#os.environ[hadoop_home]= hadoop_home_dir
#spark = SparkSession.builder.appName("dbf reader").master("local").getOrCreate()
#df = spark.sparkContext.parallelize(lst_of_value).toDF(lst_of_key)
#df.show(10)
#df.toPandas().to_csv("C:/Users/aman.raj/out/test.csv")
#df.createOrReplaceTempView("test")
#spark.sql("create table xyz as select * from test")
#df.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv")