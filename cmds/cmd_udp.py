#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nets import start_udp_client
from nets import start_udp_server


def parse_cmd_udp(cmd_parser, sub_parser):
    # parse sub parameters
    sub_parser.add_argument('-i', '--ip', help='ip address: ipv4 address witch tcp server listen',
                            type=str, default='127.0.0.1')
    sub_parser.add_argument('-p', '--port', help='port: port number witch tcp server listen',
                            type=int, default=6001)
    sub_parser.add_argument('-m', '--mode', help='mode: udp mode choose, \'server\' or \'client\' indicate udp client',
                            type=str, default='server')
    args = cmd_parser.parse_args()
    # choose udp mode
    if args.mode == 'server' or args.mode == 's':
        start_udp_server(host=args.ip, port=args.port)
    elif args.mode == 'client' or args.mode == 'c':
        start_udp_client(host=args.ip, port=args.port)
    else:
        print('Invalid Udp Mode. You can input \'c\' stand for \'client\' or \'s\' for \'server\'.')
