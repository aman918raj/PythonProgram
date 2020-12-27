import os
import sys
from zipfile import ZipFile
import subprocess
import tabula

def convertToCsv(inp_path, out_path):
    print("converting {0} to {1}".format(inp_path,out_path))
    try:
        tabula.convert_into(inp_path, out_path, output_format="tsv", pages='all')
    except RuntimeError:
        print(f"Exception occured while processing file {inp_path}")

#run commands
def run_cmd(args_list):
    print('Running system command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output, s_err

#unzip files
def unzip_files(file_path, out_path):
    print("Inside unzip_files")
    with ZipFile(file_path, 'r') as zip:
        print('Extracting all the files now...')
        try:
            zip.extractall(out_path)
        except RuntimeError:
            print(f"Exception occured while processing file {file_path}")
        print("Unzipping finished")

#iterating through sub directory
def get_files_from_sub_dir(file_path, edge_node_path):
    print("Inside get_files_from_sub_dir")
    lst_of_files = os.listdir(file_path)
    for file in lst_of_files:
        sub_file = file_path+ '/' +file
        print("sub file is : {}".format(sub_file))
        if os.path.isdir(sub_file):
            get_files_from_sub_dir(sub_file,edge_node_path)
        else:
            (ret, out, err) = run_cmd(['mv', sub_file, edge_node_path])

#processing file
def process_files(edge_node_path, lst_files):
    print("inside process_files")
    for file in lst_files:
        file_path = edge_node_path + '/' + file
        if os.path.isdir(file_path):
            get_files_from_sub_dir(file_path,edge_node_path)
            (ret, out, err) = run_cmd(['rm', '-r', file_path])
    lst_of_files=os.listdir(edge_node_path)
    print(f"list of files after getting all files in working dir : \n{lst_of_files}")
    for file in lst_of_files:
        file_path = edge_node_path + '/' + file
        out_path = edge_node_path+ '/' + os.path.splitext(file)[0] + '.csv'
        print("do process")
        convertToCsv(file_path , out_path)

print("starting pdf reader")
if (len(sys.argv) !=4):
    print(f"Needed 4 arguments, but received : {len(sys.argv)}")
    sys.exit(1)

edge_node_path = sys.argv[1] ##this should not contain path ending with '/'
hdfs_file_path = sys.argv[2] #this should contain path ending with '/'
archive_file_path = sys.argv[3] #this should contain path ending with '/'

#deleting if edge node dir exists
if os.path.exists(edge_node_path):
    (ret, out, err) = run_cmd(['rm', '-r', edge_node_path])

print(f"edge_node_path : {edge_node_path} , hdfs_file_path : {hdfs_file_path} , archive_file_path : {archive_file_path}")

#creating archieve dir on hdfs and processing dir on edge node
(ret, out, err)=run_cmd(['hdfs','dfs','-mkdir',archive_file_path])
(ret, out, err)=run_cmd(['mkdir','-p',edge_node_path])
(ret, out, err)=run_cmd(['hdfs','dfs','-get',hdfs_file_path+'*',edge_node_path])

lst_files = os.listdir(edge_node_path)
print(f"files copied to edge node : {lst_files}")

#unzip file
for file in lst_files:
    zip_file = edge_node_path+'/'+file
    if file.lower().endswith(".zip"):
        print("zip file :"+zip_file)
        unzip_files(zip_file, edge_node_path)
        (ret, out, err) = run_cmd([ 'rm', zip_file])

lst_files = os.listdir(edge_node_path)
process_files(edge_node_path, lst_files)

lst_csv_files = os.listdir(edge_node_path)
print(lst_csv_files)
#copying existing file in hdfs landing dir to archieve dir, moving all files to hdfs location and deleting edge node dir
print(f"copying existing file in hdfs landing dir :{hdfs_file_path} to archieve dir : {archive_file_path}, "
      f"moving all files to hdfs location : {hdfs_file_path} and deleting edge node dir : {edge_node_path}")
(ret, out, err)=run_cmd(['hdfs','dfs','-mv',hdfs_file_path+'*',archive_file_path])