#!/usr/bin/env python
from config import Config
from wsgiref.simple_server import make_server
from create_app import CreateApp


api = CreateApp(config=Config())

if __name__ == '__main__':
    with make_server('', 8000, api.start_app()) as httpd:
        httpd.serve_forever()