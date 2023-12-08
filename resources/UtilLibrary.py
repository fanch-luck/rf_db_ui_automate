#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: rf_db_ui_automate...UtilLibrary
# Author:    fan
# date:      2023/12/6 006 10:33
# -----------------------------------------------------------
from utils.mail import check_verify


def get_em_captcha(mail_config=None):
    """
    获取邮箱验证码
    :param mail_config: 邮箱配置dict
    :return: 邮件验证码
    """
    captcha = check_verify(mail_config)
    return captcha

if __name__ == '__main__':
    config = {
        "pop_server": "pop.exmail.qq.com",
        "pop_port": "995",
        "imap_server": "imap.exmail.qq.com",
        "imap_port": "993",
        "account": "",
        "password": ""
    }
    print(get_em_captcha(config))
