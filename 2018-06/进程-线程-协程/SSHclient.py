#!/usr/bin/python3
# -*- coding: utf-8 -*-
import paramiko
#创建ssh对象
ssh=paramiko.SSHClient()
#ssh容许链接不在know-hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname="192.168.1.161",port=22,username="root",password="zyyrd530487")
#执行命令15768000
stdin, stdout, stderr = ssh.exec_command('dfdfd')
#获取命令结果
#读过以后就没有数据了
result =stdout.read()
if  len(result)==0:
    result = stderr.read()

print(result.decode())
ssh.close()