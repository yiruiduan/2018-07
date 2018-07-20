#!/usr/bin/python3
# -*- coding: utf-8 -*-
import orm_many_to_many
from sqlalchemy.orm import sessionmaker
session_class=sessionmaker(bind=orm_many_to_many.engine)
session=session_class()
#查询数据
# author_obj=session.query(orm_many_to_many.Author).filter(orm_many_to_many.Author.name=="yiruiduan").first()
# print(author_obj)
# book_obj=session.query(orm_many_to_many.Book).filter(orm_many_to_many.Book.id==2).first()
# book_obj.authors.remove(author_obj)
# session.commit()
#插入数据
# b1=orm_many_to_many.Book(name="learn python with alex",pub_date="2018-07-16")
# b2=orm_many_to_many.Book(name="learn linux with alex",pub_date="2016-07-16")
# b3=orm_many_to_many.Book(name="learn go with alex",pub_date="2015-07-16")
# a1=orm_many_to_many.Author(name="yiruiduan")
# a2=orm_many_to_many.Author(name="yinuo")
# a3=orm_many_to_many.Author(name="zhangye")
# b1.authors=[a1,a3]
# b2.authors=[a1,a2,a3]
# session.add_all([b1,b2,b3,a1,a2,a3])
b1=orm_many_to_many.Book(name="放风筝的人",pub_date="2018-07-16")
session.add(b1)
session.commit()