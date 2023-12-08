#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: rf_db_ui_automate...RegisterConfig.py
# Author:    fan
# date:      2023/12/4 004 15:49
# -----------------------------------------------------------

class RegisterConfig:
    annexes_dir = 'data/annexes'
    download_dir = 'tmp'
    operation_interval = '2s'
    base_url = 'https://192.168.0.222:18287'
    client_title = '等保备案预登记系统'
    email_config = {
        "pop_server": "pop.exmail.qq.com",
        "pop_port": "995",
        "imap_server": "imap.exmail.qq.com",
        "imap_port": "993",
        "account": "fch@fjjzwl.com",
        "password": "NfbSF2prdfwFggEC"
    }
    # 首页
    login_url = 'https://record.fjjzwl.com:8281/'
    manual_url = "https://192.168.0.222:18287/%E7%AD%89%E4%BF%9D%E5%A4%87%E6%A1%88%E9%A2%84%E7%99%BB%E8%AE%B0%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf"
    # 常见问题
    questions_number = 15
    # 查询注册结果

