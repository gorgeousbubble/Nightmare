#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from nets import TcpServer


class TestTcpServer(unittest.TestCase):
    def test_init(self):
        s = TcpServer(host='127.0.0.1', port=6000)
        self.assertEqual(s.Host, '127.0.0.1')
        self.assertEqual(s.Port, 6000)
        self.assertEqual(s.Addr, ('127.0.0.1', 6000))
        s.stop()
