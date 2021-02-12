#filename handle2.py
import web


class Handle(object):
    # get方法，验证token
    def GET(self):
        data = web.input()
        echostr = data.echostr
        return echostr
