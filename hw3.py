import sys
import paramiko
import os

host = sys.argv[1]
port = int(sys.argv[2])
uname = sys.argv[3]
path = sys.argv[4]
pref = sys.argv[5]
count = int(sys.argv[6])
mode = sys.argv[7]

fullpath = os.path.join(path, pref)

folders = []

for i in range(1, count+1):
    folder = fullpath + str(i)
    folders.append(folder)


print('Connection to ', host)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=uname) 

for i in folders:
    mkdir_cmd = 'mkdir ' + i
    chmod_cmd = 'chmod %s %s' %(mode, i)    
    stdin, stdout, stderr = ssh.exec_command(mkdir_cmd)
    stdin, stdout, stderr = ssh.exec_command(chmod_cmd)
    print('On %s host created %s folder with %s permission' %(host, i, mode))

ssh.close()