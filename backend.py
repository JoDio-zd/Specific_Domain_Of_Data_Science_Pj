import paramiko
import time
import re
import os

a = re.compile(r'\w+\.')
req = re.compile(r'\w+\.\w+')
b = re.compile(r'[^\.]+')

server = 'gpu82.mistgpu.xyz'
port = 30320
usernames = 'mist'
passwords = 'jiqixuexi123'

class uploadphoto():

    def uploadfile_to_server(self, filename):
        t = paramiko.Transport((server, port))
        t.connect(username=usernames, password=passwords)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(filename, '/home/mist/data/EDSR-PyTorch/test/' + req.findall(filename)[0])
        t.close()

    def exec(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, port, usernames, passwords)
        stdin, stdout, stderr = ssh.exec_command('cd data/EDSR-PyTorch/src; ./demo.sh')
        time.sleep(5)
        print(stdout.read().decode('utf-8'))
        ssh.close()

    def download(self, filename):
        t = paramiko.Transport((server, port))
        t.connect(username=usernames, password=passwords)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get('/home/mist/data/EDSR-PyTorch/experiment/test/results-Demo/' + a.findall(filename)[0][:-1] +  '_x4_SR.' + b.findall(filename)[1], b.findall(filename)[0] + '_fixed.' + b.findall(filename)[1])
        t.close()
        os.system("open " + b.findall(filename)[0] + '_fixed.' + b.findall(filename)[1])
