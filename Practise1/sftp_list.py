_author_ = "aman"
import paramiko

sftpURL = 'xyz.xyz.com'
sftpUser = 'user1'
sftpPass = 'pass'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy )
ssh.connect(sftpURL, username=sftpUser, password=sftpPass,allow_agent=False,look_for_keys=False)
sftp = ssh.open_sftp()
files = sftp.listdir("/usr/local/test")
print (files)
dict_files = {}
for fileattr in sftp.listdir_attr("/usr/local/test"):
    if fileattr.filename.endswith(".csv"):
        dict_files[fileattr.st_mtime] = fileattr.filename
print(dict_files)
sort_keys = sorted(list(dict_files.keys()), reverse=True)
print(dict_files[sort_keys[0]])

with sftp.open("/usr/local/test"+"/"+dict_files[sort_keys[0]], mode='r') as file_reader:
    lines = file_reader.readlines()
line = lines[0].replace("\"","")
ssh.close()

