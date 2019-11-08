_author_ = "aman"
from pyspark.sql import SparkSession
from pyspark import *
from pyspark.sql.functions import *
from functools import reduce

def rename_columns(df2, list_cols_df, list_cols):
    i = 0
    for col in list_cols_df:
        df3 = df2.withColumnRenamed(col, list_cols[list_cols_df.index(col)])
        i += 1
    return df3

spark = SparkSession.builder.appName("sample").config("spark.sql.warehouse.dir", "warehouse").getOrCreate()

df1 = spark.read.csv("C:\\Users\\aman.raj\\Documents\\PPI_REG_FACT_M0619.csv")
df2 = df1.groupBy(col("_c0"), col("_c1")).agg(sum(col("_c2")), sum(col("_c5")))

list_cols = ["FileId", "Code", "Expense", "Revenue"]
list_cols_df = df2.columns

df3 = rename_columns(df2, list_cols_df, list_cols)
df3.show()
# df3 = reduce(lambda df2,x : df2.withColumnRenamed(list_cols_df[x], list_cols[x]), range[len(list_cols_df)], df2)
# print(df3.columns)

