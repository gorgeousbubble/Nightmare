#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


class SmtpClient(object):
    def __init__(self, host='smtp.qq.com', port=465, user='1029535012@qq.com', password='amdepjytfocvbfbc'):
        self.Host = host
        self.Port = port
        self.User = user
        self.Password = password

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send(self, to='', subject='', body=''):
        # message
        message = MIMEText(body, 'plain', 'utf-8')
        message['From'] = self._format_addr('Nightmare <%s>' % self.User)
        message['To'] = self._format_addr('alopex <%s>' % to)
        message['Subject'] = Header(subject, charset='utf-8').encode()
        # send email
        server = smtplib.SMTP_SSL(self.Host, self.Port)
        server.set_debuglevel(1)
        server.login(self.User, self.Password)
        server.sendmail(self.User, [to], message.as_string())
        server.quit()


if __name__ == '__main__':
    c = SmtpClient()
    c.send(to='alopex6414@outlook.com', subject='Nightmare', body='hello,world!(Automatic send by Nightmare client.)')
