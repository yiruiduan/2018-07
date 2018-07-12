#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,String
from  sqlalchemy.orm import sessionmaker
from  sqlalchemy import func

engine=create_engine("mysql+pymysql://yiruiduan:yiruiduan@192.168.1.115/oldboy",encoding="utf-8")
BASE=declarative_base()

class USER(BASE):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    password=Column(String(64))

    def __repr__(self):
        return "<%s name:%s>"%(self.id,self.name)
BASE.metadata.create_all(engine)

session_class=sessionmaker(bind=engine) #创建与数据库会话的对象session对象
session=session_class()                 #生成session实例
# user_obj=USER(name="yiruiduan",password="123456")  #生成你要创建的数据对象
# user_obj1=USER(name="maguilin",password="123456")      #生成你要创建的数据对象
# session.add(user_obj)                                 #把要创建的数据对象添加到这个session里，一会统一创建
# session.add(user_obj1)                                #把要创建的数据对象添加到这个session里，一会统一创建
# session.commit()                                      #提交session

# data=session.query(USER).filter().all()
# print(data)
# session.rollback()
# data=session.query(USER).filter().all()
# print(data)
# data=session.query(USER).filter_by(name="yiruiduan").delete()
# print(data)
# session.commit()
print(session.query(USER).filter_by(id=14).delete())
session.commit()