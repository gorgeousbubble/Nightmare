#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class HttpServer(HTTPServer):
    def __init__(self, host='localhost', port=8080):
        self.Host = host
        self.Port = port
        self.Addr = (self.Host, self.Port)
        self.httpServerSocket = HTTPServer(self.Addr, HttpResquestHandler)

    def start(self):
        self.httpServerSocket.serve_forever()


class HttpResquestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        r = 'hello,world!'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(r.encode('utf-8'))


if __name__ == '__main__':
    s = HttpServer()
    print('Start Listen And Server on {}'.format(s.Addr))
    s.start()
