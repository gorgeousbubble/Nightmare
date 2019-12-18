#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


class Pop3Client(object):
    def __init__(self, host='pop.qq.com', port=995, user='1029535012@qq.com', password='amdepjytfocvbfbc'):
        self.Host = host
        self.Port = port
        self.User = user
        self.Password = password

    @staticmethod
    def _guess(message):
        charset = message.get_charset()
        if charset is None:
            content_type = message.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset

    @staticmethod
    def _decode(s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    def _info(self, message, indent=0):
        if indent == 0:
            for header in ['From', 'To', 'Subject']:
                value = message.get(header, '')
                if value:
                    if header == 'Subject':
                        value = self._decode(value)
                    else:
                        hdr, addr = parseaddr(value)
                        name = self._decode(hdr)
                        value = u'%s <%s>' % (name, addr)
                print('%s%s: %s' % ('  ' * indent, header, value))
        if message.is_multipart():
            parts = message.get_payload()
            for n, part in enumerate(parts):
                print('%spart %s' % ('  ' * indent, n))
                print('%s--------------------' % ('  ' * indent))
                self._info(part, indent + 1)
        else:
            content_type = message.get_content_type()
            if content_type == 'text/plain' or content_type == 'text/html':
                content = message.get_payload(decode=True)
                charset = self._guess(message)
                if charset:
                    content = content.decode(charset)
                print('%sText: %s' % ('  ' * indent, content + '...'))
            else:
                print('%sAttachment: %s' % ('  ' * indent, content_type))

    def fetch(self):
        # fetch mail
        server = poplib.POP3_SSL(host=self.Host, port=self.Port)
        server.set_debuglevel(1)
        # welcome
        print(server.getwelcome().decode('utf-8'))
        server.user(self.User)
        server.pass_(self.Password)
        # emails counter and size
        print('Messages: %s. Size: %s' % server.stat())
        resp, mails, octets = server.list()
        print(mails)
        index = len(mails)
        resp, lines, octets = server.retr(index)
        content = b'\r\n'.join(lines).decode('utf-8')
        # parse email message
        message = Parser().parsestr(content)
        self._info(message)
        server.close()


if __name__ == '__main__':
    c = Pop3Client()
    c.fetch()

