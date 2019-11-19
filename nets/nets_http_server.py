#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class HttpServer(HTTPServer):
    def __init__(self, host='localhost', port=8080):
        self.Host = host
        self.Port = port
        self.Addr = (self.Host, self.Port)
        self.httpServerSocket = HTTPServer(self.Addr, HttpResquestHandler)

    def start(self):
        print('Start Listen And Server on {}'.format(self.Addr))
        self.httpServerSocket.serve_forever()


class HttpResquestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        r = 'hello,world!'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(r.encode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch http server listen, such as \'127.0.0.1\'', type=str, default='127.0.0.1')
    parser.add_argument(
        '-p', '--port', help='port: port number witch http server listen, such as \'8080\'', type=int, default=8080)
    args = parser.parse_args()
    s = HttpServer(host=args.ip, port=args.port)
    s.start()
