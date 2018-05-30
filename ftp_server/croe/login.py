#Author:yiruidaun
import os,json
from conf import setting
from croe import user_message

def login(username,password):
    user_date=user_message.user_messages(username)
    if not user_date:
        print("zhanghumima youwu")
        return 0
    else:
        if password ==user_date["password"]:
            return 1
        else:
            return 0

