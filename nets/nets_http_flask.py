#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'hello,world!'


@app.route('/nightmare', methods=['GET'])
def home():
    return 'Nightmare Project'


if __name__ == '__main__':
    app.debug = True
    app.run()
