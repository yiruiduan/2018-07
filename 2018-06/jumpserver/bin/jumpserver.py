#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,sys
BaseDir=os.path.dirname(os.path.dirname(os.path.abspath("jumpserver.py")))
sys.path.append(BaseDir)





if __name__=="__main__":
    from modules.actions import excute_from_command_line
    excute_from_command_line(sys.argv)
