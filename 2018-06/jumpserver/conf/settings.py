#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlalchemy

DB_host="192.168.1.115"
DB_user="yiruiduan"
DB_password="yiruiduan"
DB="jumpserver"
ConnParams="mysql+pymysql://%s:%s@%s/%s?charset=utf8"%(DB_user,DB_password,DB_host,DB)
