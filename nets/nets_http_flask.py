#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'hello,world!'


@app.route('/nightmare', methods=['GET'])
def base():
    return 'Nightmare Project'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--ip', help='ip address: ipv4 address witch http flask server listen, such as \'0.0.0.0\'', type=str, default='0.0.0.0')
    parser.add_argument(
        '-p', '--port', help='port: port number witch http flask server listen, such as \'5000\'', type=int, default=5000)
    args = parser.parse_args()
    print('Start Listen And Server on {}:{}'.format(args.ip, args.port))
    app.run(host=args.ip, port=args.port, debug=True)
