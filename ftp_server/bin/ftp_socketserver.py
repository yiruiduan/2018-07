#Author:yiruidaun

#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author:yiruidaun
import os,sys,socketserver,datetime,time,json
BaseDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)
from croe import login
from croe import time_now
from croe import commond
login_status=False
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        with open("%s\\log\\access.log"%BaseDir,"a+",encoding="utf-8") as f:
            while True:
                global login_status
                if login_status==False:
                    while True:
                        try:
                            self.data = self.request.recv(1024).strip()
                            print(self.data)
                            username = self.data.decode("utf-8").split(":")[0]
                            password = self.data.decode("utf-8").split(":")[1]
                            status = login.login(username, password)
                            self.request.send(str(status).encode("utf-8"))
                            if status == 1:
                                print("%s登录成功" % username)
                                login_status=True
                                break
                            else:
                                print("%s登录失败" % username)
                        except ConnectionResetError as e:
                            print("error:%s" % e)
                            break
                try:
                    print(self.client_address)
                    f.write("%s %s正常访问\n" % (time_now.time_now(), self.client_address))
                    f.flush()
                    self.data=self.request.recv(1024).strip()
                    if not self.data:
                        login_status=False
                        break
                    # commond.cmd_put(self.data)
                    cmd_json=json.loads(self.data.decode("utf-8"))
                    if hasattr(self,cmd_json["action"]):
                        func=getattr(self,cmd_json["action"])
                        file_status=func(cmd_json,self.request)
                    print("\033[32;1m%s\033[0m"%file_status)
                    self.request.send(file_status.encode("utf-8"))
                except ConnectionResetError as e:
                    f.write("%s error:%s\n"%(time_now.time_now(),e))
                    f.flush()
                    login_status=False
                    break
    def put(self,*args):
        return commond.cmd_put(args)
    def get(self,*args):
        return commond.cmd_get(args)



if __name__=="__main__":
    HOST,PORT="localhost",9999
    server=socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
