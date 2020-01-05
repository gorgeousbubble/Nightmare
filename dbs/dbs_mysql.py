#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector


class Mysql(object):
    def __init__(self, db, user, password):
        # input database relay...
        self.db = db
        self.user = user
        self.password = password
        # connect to database
        self.conn = mysql.connector.connect(user=self.user, password=self.password, database=self.db)
        self.cursor = self.conn.cursor()

    def exec(self, *args, **kwargs):
        return self.cursor.execute(*args, **kwargs)

    def close(self):
        # close connect
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
