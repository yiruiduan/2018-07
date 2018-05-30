#Author:yiruidaun
import socket,os,json
import hashlib
# client=socket.socket()
# client.connect(("localhost",9999))
# while True:
#     username=input("username>>:")
#     password=input("password>>:")
#     msg="%s:%s"%(username,password)
#     client.send(msg.encode("utf-8"))
#     data=client.recv(1024)
#     if data.decode("utf-8")=="1":
#         print("登录成功！！！")
#         break
# while True:
#     msg=input(">>:")
#     if msg.split(" ")[0] in commond:
#         client.send(msg.encode("utf-8"))
#         data=client.recv(1024)
#         print(data)
#     else:
#         continue
class FtpClient(object):
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.client = socket.socket()
    def connect(self):
        self.client.connect((self.host,self.port))

    def help(self):
        print("""
        ls
        get
        push
        cd ..
        """)

    def login(self):
        while True:
            username=input("username:")
            password=input("password:")
            msg = "%s:%s" % (username, password)
            self.client.send(msg.encode("utf-8"))
            status=self.client.recv(1024)
            if status.decode("utf-8") =="1":
                print("登录成功！！！")
                break

    def interactive(self):
        while True:
            cmd=input(">>:")
            cmd_str=cmd.split()[0]
            if cmd_str == "q":
                self.client.close()
                break
            if hasattr(self,"cmd_%s"%cmd_str):
                func=getattr(self,"cmd_%s"%cmd_str)
                func(cmd)
                # client_obj.send(msg.encode("utf-8"))
                # data=client_obj.recv(1024)
                # print(data)
            else:
                self.help()

    def cmd_put(self,*args):
        #文件上传
        cmd_split=args[0].split()
        if len(cmd_split) >1:
            file_name=cmd_split[1]  #文件名
            if os.path.isfile(file_name):

                file_size=os.stat(file_name).st_size  #文件大小
                msg_dic={
                    "action":"put",
                    "filename":file_name,
                    "size":file_size
                }
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                #防止粘包，等待服务器确认
                server_response=self.client.recv(1024)
                print(server_response)
                f=open(file_name,"rb")
                m=hashlib.md5()       #hashlib计算文件MD5值
                for line in f:
                    self.client.send(line)
                    m.update(line)
                else:
                    f.close()
                    self.client.send(m.hexdigest().encode("utf-8"))
                    file_status=self.client.recv(1024).decode("utf-8")    #接收上传文件后MD5对比状态200正常400是文件MD5不一致
                    if file_status == "200":
                        print("%s上传成功！！！"%file_name)
                    else:
                        print("%s上传失败！！！"%file_name)

            else:
                print(file_name,"is not exist")

    def cmd_get(self,*args):
        cmd_split=args[0].split()
        if len(cmd_split) >1:
            file_name=cmd_split[1] #文件名
            msg_dic={
                "action":"get",
                "filename":file_name
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            server_response_message=self.client.recv(1024)
            server_response=json.loads(server_response_message.decode("utf-8"))
            file_exist_status=server_response["status"]
            if len(server_response)>1:
                file_real_size=server_response["size"]

            if file_exist_status == "201":    #文件是否存在201存在401不存在
                f=open(file_name,"wb")
                m=hashlib.md5()
                file_recv_size=0
                while file_recv_size<file_real_size:
                    if file_real_size-file_recv_size>1024:
                        size=1024
                    else:
                        size=file_real_size-file_recv_size
                    data=self.client.recv(size)
                    m.update(data)
                    f.write(data)
                    file_recv_size+=len(data)
                else:

                    f.close()
                    file_recv_md5=m.hexdigest()
                    file_real_md5=self.client.recv(1024)
                    if file_recv_md5 ==file_real_md5.decode("utf-8"):
                        print("loading success!!!")
            else:
                print("您请求的文件不存在！！！")
        pass


Client=FtpClient("localhost",9999)
Connect=Client.connect()
Client.login()
Client.interactive()