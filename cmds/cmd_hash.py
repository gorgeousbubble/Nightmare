#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parse_cmd_hash(cmd_parser, sub_parser):
    # parse sub parameters
    sub_parser.add_argument('-i', '--input', help='input string: the string wait for hash calc',
                            type=str, default='')
    sub_parser.add_argument('-t', '--type', help='algorithm type: calc with which hash algorithms(md5, sha1)',
                            type=str, default='')
    args = cmd_parser.parse_args()
    print(args)
    # check input string
    if args.input == '':
        print('The input string can not be empty!')
        return
    # choose hash algorithm mode
    if args.type == 'md5':
        pass
    elif args.type == 'sha1':
        pass
    else:
        print('Invalid hash algorithm. You can choose one of hash algorithm from support list.')
