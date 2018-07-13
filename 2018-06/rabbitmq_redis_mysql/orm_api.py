#!/usr/bin/python3
# -*- coding: utf-8 -*-
import orm_many_fk
from sqlalchemy.orm import sessionmaker
session_class=sessionmaker(bind=orm_many_fk.engine)
session=session_class()
# a1=orm_many_fk.Address(street="tundiancun",city="haidian",state="beijing")
# a2=orm_many_fk.Address(street="tiantongyuan",city="changpin",state="beijing")
# a3=orm_many_fk.Address(street="qiaoxiqu",city="zhangjiakou",state="hebei")
# a4=orm_many_fk.Address(street="kangbaoxian",city="zhangjiakou",state="hebei")
#
#
# session.add_all([a1,a2,a3,a4])
#
# c1=orm_many_fk.Customer(name="yiruidaun",billing_address=a1,shipping_address=a1)
# c2=orm_many_fk.Customer(name="zhangye",billing_address=a2,shipping_address=a3)
# session.add_all([c1,c2])
# session.commit()
data=session.query(orm_many_fk.Customer).filter_by(id=2).first()
print(data.shipping_address.street)