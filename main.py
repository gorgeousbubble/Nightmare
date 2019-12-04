#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys
import os
from cmds import parse_cmd_tcp
from cmds import parse_cmd_udp


if __name__ == '__main__':
    # command parser
    cmd_parser = argparse.ArgumentParser(prog='Nightmare')
    sub_parser = cmd_parser.add_subparsers()
    cmd_map = dict()
    cmd_map['tcp'] = {'sub_parser': sub_parser.add_parser('tcp'), 'func': parse_cmd_tcp}
    cmd_map['udp'] = {'sub_parser': sub_parser.add_parser('udp'), 'func': parse_cmd_udp}
    # check command args number
    if len(sys.argv) < 2:
        # append '--help' display usage
        sys.argv.append('--help')
        cmd_parser.parse_args()
    else:
        # check command function supported
        if sys.argv[1] not in cmd_map:
            sys.argv[1] = '--help'
            cmd_parser.parse_args()
        # execute sub-parse function
        cmd = cmd_parser
        sub = cmd_map[sys.argv[1]]['sub_parser']
        fun = cmd_map[sys.argv[1]]['func']
        fun(cmd, sub)