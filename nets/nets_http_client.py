#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import http.client
import time


class HttpClient(object):
    def __init__(self, host, port, timeout=5, retry=3):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.retry = retry
        self.addr = (self.host, self.port)

    def request(self, *args, **kwargs):
        # http response message
        response = None
        try:
            # connect to http server
            conn = http.client.HTTPConnection(host=self.host, port=self.port, timeout=self.timeout)
            # send http request
            conn.request(*args, **kwargs)
            # fetch http response
            response = conn.getresponse()
        except Exception as e:
            print(e)
        finally:
            return response

    def request_with_retry(self, *args, **kwargs):
        # connect to http server
        conn = http.client.HTTPConnection(host=self.host, port=self.port, timeout=self.timeout)
        # send http request and retry
        while True:
            try:
                # send request when response 200 return
                conn.request(*args, **kwargs)
                response = conn.getresponse()
                if response.status == http.HTTPStatus.OK:
                    break
            except Exception as e:
                # response error
                response = e
                pass
            self.retry -= 1
            time.sleep(1)
            if self.retry > 0:
                time.sleep(1)
            else:
                break
        if isinstance(response, Exception):
            raise response
        return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch http client connect, such as \'127.0.0.1\'', type=str, default='127.0.0.1')
    parser.add_argument(
        '-p', '--port', help='port: port number witch http client connect, such as \'8080\'', type=int, default=8080)
    args = parser.parse_args()
    c = HttpClient(host=args.ip, port=args.port)
    print(c.request(method='GET', url='/'))
