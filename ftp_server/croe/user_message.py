#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json,os
from conf import setting
def user_messages(username):
    user_file = "%s\\conf\\user\\%s.json" % (setting.BaseDir, username)
    if os.path.isfile(user_file):
        with open(user_file,"r") as f:
            user_data=json.load(f)
            return user_data