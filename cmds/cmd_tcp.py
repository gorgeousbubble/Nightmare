#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nets import start_tcp_client
from nets import start_tcp_server


def parse_cmd_tcp(cmd_parser, sub_parser):
    # parse sub parameters
    sub_parser.add_argument('-i', '--ip', help='ip address: ipv4 address witch tcp server listen',
                            type=str, default='127.0.0.1')
    sub_parser.add_argument('-p', '--port', help='port: port number witch tcp server listen',
                            type=int, default=6000)
    sub_parser.add_argument('-m', '--mode', help='mode: tcp mode choose, \'server\' or \'client\' indicate tcp mode',
                            type=str, default='server')
    args = cmd_parser.parse_args()
    # choose tcp mode
    if args.mode == 'server' or args.mode == 's':
        start_tcp_server(host=args.ip, port=args.port)
    elif args.mode == 'client' or args.mode == 'c':
        start_tcp_client(host=args.ip, port=args.port)
    else:
        print('Invalid Tcp Mode. You can input \'c\' stand for \'client\' or \'s\' for \'server\'.')
