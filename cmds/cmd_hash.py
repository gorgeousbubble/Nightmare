#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hash import hash_md5, hash_sha1, hash_sha256


def parse_cmd_hash(cmd_parser, sub_parser):
    # parse sub parameters
    sub_parser.add_argument('-i', '--input', help='input string: the string wait for hash calc',
                            type=str, default='')
    sub_parser.add_argument('-t', '--type', help='algorithm type: calc with which hash algorithms(md5, sha1, sha256)',
                            type=str, default='')
    args = cmd_parser.parse_args()
    # check input string
    if args.input == '':
        print('The input string can not be empty!')
        return
    # choose hash algorithm mode
    if args.type == 'md5':
        r = hash_md5(args.input)
        print('calc md5:{}'.format(r))
    elif args.type == 'sha1':
        r = hash_sha1(args.input)
        print('calc sha1:{}'.format(r))
    elif args.type == 'sha256':
        r = hash_sha256(args.input)
        print('calc sha256:{}'.format(r))
    else:
        print('Invalid hash algorithm. You can choose one of hash algorithm from support list.')
