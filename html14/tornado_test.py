#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        user=self.get_argument("user")
        pwd=self.get_argument("password")
        tel_code=self.get_argument("tel_code")

        # sex=self.get_argument("sex")
        # fav=self.get_arguments("fav")
        # file=self.get_argument("file")
        # meno=self.get_argument("meno")
        # city=self.get_arguments("city")
        print(user,pwd,tel_code)
        self.write("ok")
        # if user=="yiruiduan" and pwd=="530487":
        #     self.write("OK")
        # else:
        #     self.write("gun")
    def post(self):
        print("123")
        self.write("POST")
application=tornado.web.Application([("/index",MainHandler),])

if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()