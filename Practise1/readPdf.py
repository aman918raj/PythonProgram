_author_ = "aman"

import tabula
import os
import pandas as pd

def convertToCsv(inp_path, out_path):

    #df_list = tabula.read_pdf(inp_path, pandas_options={}, encoding='utf-8', pages='all')
   # df = pd.concat(df_list)
   # print(df)
   # s='\u03B5'
   # df.to_csv(out_path,sep=s, index=False)
    tabula.convert_into(inp_path, out_path, output_format="tsv", pages='all')


file_path = "C:/Users/aman.raj/Desktop/files/pdf3"
lstOfFiles = os.listdir(file_path)
print(lstOfFiles)

for file in lstOfFiles:
    file_lst_path = file_path+"/"+file
    out_path = os.path.dirname(file_path)+"/csv_uni/"+os.path.splitext(file)[0]+".csv"
    if(os.path.isfile(file_lst_path)):
        print(file_lst_path)
        print(out_path)
        convertToCsv(file_lst_path,out_path)
