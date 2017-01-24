import os
import sys
import paramiko

address = sys.argv[1]
port = int(sys.argv[2])
name = sys.argv[3]
path = sys.argv[4]
prefix = sys.argv[5]
counts = int(sys.argv[6]) + 1
mode = int(sys.argv[7], 8)

print address
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(address, port=port, username=name) 

i=1
while i < counts:
        fld=os.path.join(path, prefix+str(i))
        
        stdin, stdout, stderr = ssh.exec_command('mkdir ' + fld)
        stdin, stdout, stderr = ssh.exec_command('chmod ' + fld)
        i+=1

print stdout.read()

ssh.close()