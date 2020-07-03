#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from dbs.dbs_sqlite import Sqlite3


class TestSqlite3(unittest.TestCase):
    def test_query_simple(self):
        db = Sqlite3(path='../test/data/dbs/test_sqlite3.db')
        db.exec('create table user(id varchar(20) primary key, name varchar(20), score int)')
        db.exec(r"insert into user values ('A-001', 'Adam', 95)")
        db.exec(r"insert into user values ('A-002', 'Bart', 62)")
        db.exec(r"insert into user values ('A-003', 'Lisa', 78)")
        values = db.exec('select * from user where id=?', ('A-001',)).fetchall()
        self.assertEqual(len(values), 1)
        self.assertTupleEqual(values[0], ('A-001', 'Adam', 95))
        db.close()
