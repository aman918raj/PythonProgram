_author_ = "aman"
from pyspark import SparkContext, SparkConf
import subprocess
import pickle

set_env = "%PATH%;set PATH=C:\\hadoop\\bin"

conf = SparkConf().setAppName("wordcount").setMaster("local")
sc = SparkContext(conf=conf)
file = sc.binaryFiles("C:\\Users\\aman.raj\\Desktop\\python_output\\excel\\test1.xlsx")

file_map = file.map(lambda x: pickle.load(x[1]))

print(file_map.first())

