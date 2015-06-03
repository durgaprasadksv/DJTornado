#!/usr/bin/env python

# Run this with
# PYTHONPATH=. DJANGO_SETTINGS_MODULE=testsite.settings testsite/tornado_main.py
# Serves by default at
# http://localhost:8080/hello-tornado and
# http://localhost:8080/hello-django

from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
from django.core.wsgi import get_wsgi_application
define('port', type=int, default=8080)

def main():
  parse_command_line()
  import os
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJTornado.settings")
  parse_command_line()
  wsgi_app = get_wsgi_application()
  container = tornado.wsgi.WSGIContainer(wsgi_app)
  tornado_app = tornado.web.Application(
        [
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': "/Users/abc/path/static"}),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ])

  server = tornado.httpserver.HTTPServer(tornado_app)
  server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()
if __name__ == '__main__':
  main()
