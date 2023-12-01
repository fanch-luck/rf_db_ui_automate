#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: rf_db_ui_automate...utils
# Author:    fan
# date:      2023/12/1 001 17:49
# -----------------------------------------------------------
import os
os.system(
    f"datafaker "
    f"mysql mysql+mysqldb://root:fjjzwl-1qaz-0okm-2wsx@192.168.0.103:3306/reminder t_register "
    f"100  "
    f"--outprint "
    f"--withheader "
    f"--meta .\data\Register.datamodel "
    f">> .\data\Register.data"
    )
