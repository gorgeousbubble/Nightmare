#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from nets import UdpServer
from nets import UdpClient


def parse_cmd_udp(cmd_parser, sub_parser):
    # parse sub parameters
    sub_parser.add_argument('-i', '--ip', help='ip address: ipv4 address witch tcp server listen, such as \'127.0.0.1\'', type=str, default='127.0.0.1')
    sub_parser.add_argument('-p', '--port', help='port: port number witch tcp server listen, such as \'6001\'', type=int, default=6001)
    sub_parser.add_argument('-m', '--mode', help='mode: udp mode choose, \'s\' or \'server\' indicate udp server, \'c\' or \'client\' indicate udp client', type=str, default='server')
    args = cmd_parser.parse_args()
    print(args)
    # choose udp mode
    if args.mode == 'server' or args.mode == 's':
        s = UdpServer(host=args.ip, port=args.port)
        s.start()
    elif args.mode == 'client' or args.mode == 'c':
        c = UdpClient(host=args.ip, port=args.port)
        c.start()
    else:
        print('Invalid Udp Mode. You can input \'c\' stand for \'client\' or \'s\' for \'server\'.')