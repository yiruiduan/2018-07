#!/usr/bin/python3
# -*- coding: utf-8 -*-
import paramiko,threading

host_list1=[{"hostip":"192.168.1.127","hostport":22,"username":"root","password":"zyyrd530487"},
            {"hostip": "192.168.1.130", "hostport": 22, "username": "root", "password": "zyyrd530487"},
            {"hostip": "192.168.1.131", "hostport": 22, "username": "root", "password": "zyyrd530487"},
            {"hostip": "192.168.1.161", "hostport": 22, "username": "root", "password": "zyyrd530487"}]
def echo_host(host_list):
    for host in host_list:
        print(host["hostip"])

def ssh_client(host_message,cmd):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host_message["hostip"],port=host_message["hostport"],username=host_message["username"],password=host_message["password"])
    stdin,stdout,stderr=ssh.exec_command(cmd)
    result = stdout.read()
    if len(result) == 0:
        result = stderr.read()
    print("\033[31;1m%s\033[0m"%host_message["hostip"])
    print(result.decode())
def ssh_sftp(host_message,cmd,file_name):
    transport=paramiko.Transport((host_message["hostip"],host_message["hostport"]))
    transport.connect(username=host_message["username"],password=host_message["password"])
    sftp=paramiko.SFTPClient.from_transport(transport)
    if cmd == "put":
        sftp.put(file_name,"/root/%s"%file_name)
    # elif cmd == "get":
    #     try:
    #         sftp.get(file_name, file_name)
    #     except FileNotFoundError as e:
    #         print("没有找到文件！！！")
    #     transport.close()

echo_host(host_list1)
cmd=input(">>:")
if cmd.startswith("put"):
    for host_message in host_list1:
        t=threading.Thread(target=ssh_sftp,args=(host_message,cmd.split()[0],cmd.split()[1]))
        t.start()
else:
    for host_message in host_list1:
        t=threading.Thread(target=ssh_client,args=(host_message,cmd))
        t.start()
