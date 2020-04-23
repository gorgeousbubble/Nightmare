#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import logging
import sys
import os
from const import APPLICATION_NAME
from const import LOGS_DIR
from const import LOGS_TARGET
from cmds import parse_cmd_help
from cmds import parse_cmd_tcp
from cmds import parse_cmd_udp
from cmds import parse_cmd_hash
from logs import Log


# initialize logger instance
log = Log(target=LOGS_TARGET, level=logging.DEBUG, path=LOGS_DIR, app=APPLICATION_NAME)


# application start
if __name__ == '__main__':
    # command parser
    cmd_parser = argparse.ArgumentParser(prog=APPLICATION_NAME)
    sub_parser = cmd_parser.add_subparsers()
    cmd_map = dict()
    cmd_map['tcp'] = {'sub_parser': sub_parser.add_parser('tcp'), 'func': parse_cmd_tcp}
    cmd_map['udp'] = {'sub_parser': sub_parser.add_parser('udp'), 'func': parse_cmd_udp}
    cmd_map['hash'] = {'sub_parser': sub_parser.add_parser('hash'), 'func': parse_cmd_hash}
    # check command args number
    if len(sys.argv) < 2:
        # first display project title
        parse_cmd_help()
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
