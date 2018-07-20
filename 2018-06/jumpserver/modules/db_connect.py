#!/usr/bin/python3
# -*- coding: utf-8 -*-
from conf import settings
from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker
engine=create_engine(settings.ConnParams)
session_class=sessionmaker(bind=engine)
session=session_class()