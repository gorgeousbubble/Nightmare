#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hash import hash_gen


def parse_cmd_hash(cmd_parser, sub_parser):
    # parse sub parameters
    sub_parser.add_argument('-i', '--input', help='input string: the string wait for hash calc',
                            type=str, default='')
    sub_parser.add_argument('-t', '--type', help='algorithm type: calc with which hash algorithms(md5, sha1, sha256)',
                            type=str, default='')
    args = cmd_parser.parse_args()
    # generate hash code
    hash_gen(args.input, args.type)
