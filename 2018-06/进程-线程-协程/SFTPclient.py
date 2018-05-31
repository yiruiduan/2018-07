#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paramiko
#创建transport连接
transport=paramiko.Transport(("192.168.1.161",22))
transport.connect(username="root",password="zyyrd530487")
#创建sftp连接
sftp=paramiko.SFTPClient.from_transport(transport)
#上传文件
sftp.put("SSHclient.py","/tmp/test.py")
#下载文件
sftp.get("/root/feiji.py","local_path")
transport.close()