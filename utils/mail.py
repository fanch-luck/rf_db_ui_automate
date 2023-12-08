#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: db_ui...mail
# Author:    fan
# date:      2023/6/29 029 17:38
# -----------------------------------------------------------

import poplib
import imaplib
import base64
import email
import re, time
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def connect_pop3_server(config):
    server = poplib.POP3_SSL(config["server"], config["port"])

    server.set_debuglevel(0)  # 打印调试日志
    print(server.getwelcome().decode("utf8"))  # 打印欢迎信息
    server.user(config["account"])
    server.pass_(config["password"])
    email_stat = server.stat()
    email_list = server.list()
    # print(email_stat)
    # if email_stat[0] == b'+OK':
    #     print(f"邮箱状态，消息数量{email_stat[1]}，容量大小{email_stat[2]}", )
    print(email_list)
    if email_list[0] == b'+OK':
        print(f"消息数量：{len(email_list[1])}，消息列表：{email_list[1]}")
    return server, email_list


def decode_subject(encoded_subject):
    # 获取编码方式
    encoding = encoded_subject.split('?')[1]
    # 获取编码内容
    encoded_text = encoded_subject.split('?')[3]
    # 解码内容
    decoded_text = base64.b64decode(encoded_text).decode(encoding)
    return decoded_text


# 解析邮件内容
def get_body(msg):
    """获取邮件正文"""
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,decode=True)


def decode_data(bytes, added_encode=None):
    """
    字节解码
    :param bytes:
    :return:
    """
    def _decode(bytes, encoding):
        try:
            return str(bytes, encoding=encoding)
        except Exception as e:
            return None

    encodes = ['UTF-8', 'GBK', 'GB2312']
    if added_encode:
        encodes = [added_encode] + encodes
    for encoding in encodes:
        str_data = _decode(bytes, encoding)
        if str_data is not None:
            return str_data
    return None


def connect_imap_server(config):
    """连接邮件imap服务器"""
    conn = imaplib.IMAP4_SSL(config["imap_server"], config["imap_port"])
    conn.login(config["account"], config["password"])
    return conn


def get_inbox_email_num(conn):
    """获取收件箱邮件数量"""
    conn.select("INBOX")
    resp, mails = conn.search(None, 'ALL')
    if resp == "OK":
        # print(resp)
        # print(mails)
        mails_list = mails[0].split()
        mail_nums = len(mails_list)
        print("收件数量", mail_nums)
        return mail_nums
    else:
        return None


def get_last_mail_body(conn, email_num: int):
    resp, data = conn.fetch(str(email_num), '(RFC822)')
    emailbody = data[0][1]
    mail = email.message_from_bytes(emailbody)
    mail_encode = decode_header(mail.get("Subject"))[0][1]
    mail_title = decode_data(decode_header(mail.get("Subject"))[0][0], mail_encode)
    print("邮件标题", mail_title)
    mail_body = decode_data(get_body(mail))
    print("邮件正文", mail_body)
    return mail_title, mail_body


def check_verify(mail_config):
    conn = connect_imap_server(mail_config)
    num1 = get_inbox_email_num(conn)  # 第一次查邮件数量
    count = 0
    title, body = None, None
    while True:
        time.sleep(5)  # 进行验证码邮件发送操作，并等待服务器收到邮件
        print(f"正在接收邮件...{count}")
        num2 = get_inbox_email_num(conn)  # 第二次查邮件数量
        if num2 - num1 >= 1:
            # 根据num2 num1大小判断是否已经收到邮件，如果已经收到邮件则解析邮件内容，返回正文（由主程序进行解析）
            title, body = get_last_mail_body(conn, num2)
            break
        count += 1
        if count > 6:
            print('收取邮件超时（30秒）')
            break
    if title == "福州网安":
        verify = re.search('\d\d\d\d\d\d', body).group()
    else:
        verify = None
    return verify


if __name__ == "__main__":
    config = {
        "pop_server": "pop.exmail.qq.com",
        "pop_port": "995",
        "imap_server": "imap.exmail.qq.com",
        "imap_port": "993",
        "account": "fch@fjjzwl.com",
        "password": "NfbSF2prdfwFggEC"
    }
    print(check_verify(config))


