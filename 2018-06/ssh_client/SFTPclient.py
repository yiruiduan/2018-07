#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paramiko
#创建transport连接
private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
transport=paramiko.Transport(("192.168.1.161",22))
transport.connect(username="root",pkey=private_key)
#创建sftp连接
sftp=paramiko.SFTPClient.from_transport(transport)
#上传文件
sftp.put("SSHclient.py","/tmp/test.py")
#下载文件
try:
    sftp.get("/root/.ssh/authorized_keys","authorized_keys")
except FileNotFoundError as e:
    print("没有找到文件！！！")
transport.close()