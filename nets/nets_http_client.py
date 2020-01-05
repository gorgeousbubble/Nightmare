#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import http.client


class HttpClient(object):
    def __init__(self, host='localhost', port=8080):
        self.Host = host
        self.Port = port
        self.Addr = (self.Host, self.Port)
        self.Conn = http.client.HTTPConnection(host=self.Host, port=self.Port)

    def request(self, *args, **kwargs):
        self.Conn.request(*args, **kwargs)

    def response(self):
        response = self.Conn.getresponse()
        return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch http client connect, such as \'127.0.0.1\'', type=str, default='127.0.0.1')
    parser.add_argument(
        '-p', '--port', help='port: port number witch http client connect, such as \'8080\'', type=int, default=8080)
    args = parser.parse_args()
    c = HttpClient(host=args.ip, port=args.port)
    c.request(method='GET', url='/')
    print(c.response())
