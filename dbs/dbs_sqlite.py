#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sqlite3


class Sqlite3(object):
    def __init__(self, path):
        # input db file path
        self.db = os.path.join(os.path.dirname(__file__), path)
        # check db file exist
        if os.path.isfile(self.db):
            os.remove(self.db)
        # connect to database
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def exec(self, *args, **kwargs):
        return self.cursor.execute(*args, **kwargs)

    def close(self):
        # close connect
        self.cursor.close()
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    db = Sqlite3(path='../test/data/dbs/test_sqlite3.db')
    db.exec('create table user(id varchar(20) primary key, name varchar(20), score int)')
    db.exec(r"insert into user values ('A-001', 'Adam', 95)")
    db.exec(r"insert into user values ('A-002', 'Bart', 62)")
    db.exec(r"insert into user values ('A-003', 'Lisa', 78)")
    res = db.exec('select * from user where id=?', ('A-001', ))
    for v in res:
        print(v)
    db.close()
