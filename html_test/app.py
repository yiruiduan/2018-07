#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # user=self.get_argument("username")
        # email=self.get_argument("email")
        # password=self.get_argument("password")
        # if user=="yiruiduan" and password=="123456" and email=="297109186@qq.com":
        #     self.write("ok")
        print("456")
        area=self.get_argument("msg")
        print(area)
        # favor=self.get_arguments("favor")
        # print(favor)
        # self.write("get")
        # else:
        #     self.write("滚")
    def post(self, *args, **kwargs):
        print("123")
        self.write("POST")


application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(9998)
    tornado.ioloop.IOLoop.instance().start()