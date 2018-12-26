import tornado.ioloop
import tornado.web
import tornado.escape
from tornado.options import define, options
from db_access import *
from config import SERVER_PORT
import json
define("port", default=SERVER_PORT, help="run on the given port", type=int)
define("debug", default=True, type=bool)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, Welcome to GithubTrendingApi')
        self.finish()


class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        cc = self.get_argument('lang', '')
        dd = self.get_argument('since', '')
        if not cc and not dd:
            res = get_api('default')
        else:
            res = get_api(cc, dd)
        self.finish(json.dumps(res, ensure_ascii=False))


class DevHandler(tornado.web.RequestHandler):
    def get(self):
        cc = self.get_argument('lang', '')
        dd = self.get_argument('since', '')
        if not cc and not dd:
            res = get_dev('default')
        else:
            res = get_dev(cc, dd)
        self.finish(json.dumps(res, ensure_ascii=False))


class LanguagesHandler(tornado.web.RequestHandler):
    def get(self):
        res = get_languages()
        self.finish(json.dumps(res, ensure_ascii=False))


settings = {
        "debug": False,
}


application = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/api', ApiHandler),
    (r'/api/developers', DevHandler),
    (r'/api/languages', LanguagesHandler),
], **settings)


def run():
    application.listen(options.port)
    print("App Start running at: http://127.0.0.1:{port}".format(port=options.port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    run()
