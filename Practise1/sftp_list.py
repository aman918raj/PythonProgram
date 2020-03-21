_author_ = "aman"
import paramiko

sftpURL = 'secureftp.imshealth.com'
sftpUser = 'Philippines'
sftpPass = 'Ketti937'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy )
ssh.connect(sftpURL, username=sftpUser, password=sftpPass,allow_agent=False,look_for_keys=False)
sftp = ssh.open_sftp()
files = sftp.listdir("/Philippines/In/development/df5/ph9/data/ecp")
print (files)
dict_files = {}
for fileattr in sftp.listdir_attr("/Philippines/In/development/df5/ph9/data/ecp"):
    if fileattr.filename.endswith(".cmplt"):
        dict_files[fileattr.st_mtime] = fileattr.filename
print(dict_files)
sort_keys = sorted(list(dict_files.keys()), reverse=True)
print(dict_files[sort_keys[0]])

with sftp.open("/Philippines/In/development/df5/ph9/data/ecp"+"/"+dict_files[sort_keys[0]], mode='r') as file_reader:
    lines = file_reader.readlines()
line = lines[0].replace("\"","")
ssh.close()

