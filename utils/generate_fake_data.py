#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: rf_db_ui_automate...utils
# Author:    fan
# date:      2023/12/1 001 17:49
# -----------------------------------------------------------
import os, sys
import pandas
# 创建一组注册端随机数据
def gen_data(meta_data='.\data\Register.datamodel', output='.\data\Register.data'):
    os.system(
        f"datafaker "
        f"mysql mysql+mysqldb://root:fjjzwl-1qaz-0okm-2wsx@192.168.0.103:3306/reminder t_register "
        f"100  "
        f"--outprint "
        f"--withheader "
        f"--meta {meta_data} "
        f">> {output}"
        )


def gen_case_data(data_from=None, use_columns=None, use_row_num=0, case_register_submit=None, start_line=0):
    """
    从data文件生成用例数据，插入测试用例
    :param data_from: .data文件路径
    :param use_columns: 使用数据列，要求顺序
    :param case_register_submit: 插入用例文件路径
    :param start_line: 从用例文件该行号插入用例数据
    :return: 0 正常结束返回0
    """
    print(data_from, use_columns, case_register_submit, start_line)
    if os.path.exists(data_from) and os.path.exists(case_register_submit):
        df = pandas.read_csv('data\\Register.data', index_col='ID', encoding="utf-8")
        if set(use_columns) > set(df.columns):  # 使用字段溢出
            print('  use_column包含字段与数据源不匹配')
        else:
            row_num, col_num = df.shape
            new_df = pandas.DataFrame(df.loc[1:10, use_columns], columns=use_columns)
            new_df.a

    else:
        print('  所引用的的文件不存在。')


if __name__ == '__main__':
    # 注册提交数据生成参数
    register_submit_data_conf = {
        'data_from': r'.\data\Register.data',
        'use_columns': ['ID', 'UNIT_NAME', 'UNIT_USCC', 'SAFER_NAME', 'SAFER_ID', 'SAFER_PHONE', 'SAFER_EMAIL',
            'IS_RECORDED', 'RECORDED_CODE', 'IP_ADDRESS'],
        'use_row_num': 10,
        'case_register_submit': r'.\tests\register_client\reg_register_submit_tests.robot',
        'start_line': 25
    }
    # 查看注册结果数据生成参数
    query_result_data_conf = {
        'data_from': r'.\data\Register.data',
        'use_columns': ['ID', 'UNIT_NAME', 'SAFER_NAME', 'SAFER_EMAIL'],
        'case_register_submit': r'.\tests\register_client\reg_query_result_tests.robot',
        'start_line': 13
    }
    gen_case_data(**register_submit_data_conf)
