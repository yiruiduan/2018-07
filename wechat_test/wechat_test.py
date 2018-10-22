#!/usr/bin/python3
# -*- coding: utf-8 -*-


import requests,sys,json,datetime
import urllib3
urllib3.disable_warnings()
#!/usr/bin/python
#_*_coding:utf-8 _*_



def GetToken(Corpid,Secret):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
        "corpid":Corpid,
        "corpsecret":Secret
    }
    r = requests.get(url=Url,params=Data,verify=False)
    Token = r.json()['access_token']
    return Token

def SendMessage(Token,User,Agentid,Subject,Content):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        "touser": User,                                 # 企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        #"totag": Tagid,                                # 企业号中的标签id，群发使用（推荐）
        #"toparty": Partyid                             # 企业号中的部门id，群发时使用。
        "msgtype": "text",                              # 消息类型。
        "agentid": Agentid,                             # 企业号中的应用id。
        "text": {
            "content": Subject + '\n' + Content
        },
        "safe": "0"
    }
    r = requests.post(url=Url,data=json.dumps(Data),verify=False)
    return r.text


if __name__ == '__main__':
    User = sys.argv[1]
    Subject = sys.argv[2]
    Content = sys.argv[3]

    Corpid = "ww02d563e1ba4671f7"                                                   # CorpID是企业号的标识
    Secret = "HH1Gg3Al1xBgKDLiHK4m3BwL2zlHZzk4PnKpkJcCAM0"     # Secret是管理组凭证密钥
    #Tagid = "1"                                                                     # 通讯录标签ID
    Agentid = "1000002"                                                                   # 应用ID
    #Partyid = "1"                                                                  # 部门ID

    Token = GetToken(Corpid, Secret)
    print(Token)
    Status = SendMessage(Token,User,Agentid,Subject,Content)
    print (Status)
    with open("/tmp/zabbix_python.log","w") as f:
        f.write("%s %s %s"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),User,Status))
