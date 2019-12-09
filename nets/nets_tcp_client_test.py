#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from nets import TcpClient


class TestTcpClient(unittest.TestCase):
    def test_init(self):
        c = TcpClient(host='127.0.0.1', port=6000)
        self.assertEqual(c.Host, '127.0.0.1')
        self.assertEqual(c.Port, 6000)
        self.assertEqual(c.Addr, ('127.0.0.1', 6000))
        c.stop()
