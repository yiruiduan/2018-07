#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time,os,hashlib,json
from conf import setting
def cmd_put(cmd_tuple):
    cmd_str=cmd_tuple[0]
    server_obj=cmd_tuple[1]
    server_obj.send(b"ok")
    file_name=cmd_str["filename"]
    file_size=int(cmd_str["size"])
    file_real_size=0
    if os.path.isfile(cmd_str["filename"]):
        print("文件已经存在是否覆盖！！！")
        f=open("%s.new"%file_name,"wb")
    else:
        f=open(file_name,"wb")
    m=hashlib.md5()
    while file_real_size <file_size:
        if file_size-file_real_size>1024:
            size=1024
        else:
            size=file_size-file_real_size
        data=server_obj.recv(size)
        m.update(data)
        f.write(data)
        file_real_size+=len(data)
    else:
        file_recv_md5=m.hexdigest()
        file_real_md5=server_obj.recv(1024).decode("utf-8")
        if file_recv_md5 ==file_real_md5:
            return "200"
        else:
            return "400"
    f.close()

def cmd_get(cmd_tuple):
    cmd_str = cmd_tuple[0]
    server_obj = cmd_tuple[1]
    file_name=cmd_str["filename"]
    if os.path.isfile(file_name):
        file_size = os.stat(file_name).st_size
        status="201"
        msg_dic={
            "size":file_size,
            "status":status
        }
        server_obj.send(json.dumps(msg_dic).encode("utf-8"))
        m=hashlib.md5()
        f=open(file_name,"rb")
        for line in f:
            server_obj.send(line)
            m.update(line)
        else:
            f.close()
            return m.hexdigest()

    else:
        status="401"
        msg_dic = {
            "status": status
        }
        return json.dumps(msg_dic)
