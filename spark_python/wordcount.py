_author_ = "aman"
from pyspark import SparkContext, SparkConf
import os

# set_env = "%PATH%;set PATH=C:\\hadoop\\bin"
# os.system(set_env)

conf = SparkConf().setAppName("wordcount").setMaster("local")
sc = SparkContext(conf=conf)
file = sc.textFile("C:\\Users\\aman.raj\\Desktop\\python_output\\file1.txt")
file_flatmap = file.flatMap(lambda x: x.split(" "))
file_map = file_flatmap.map(lambda x: (x,1))
file_reduce = file_map.reduceByKey(lambda a,b: a+b)

word_count = file_reduce.collect()

for (word,count) in word_count:
    print(word +" --> {0}".format(count))
