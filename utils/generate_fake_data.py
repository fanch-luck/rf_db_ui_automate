#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: rf_db_ui_automate...utils
# Author:    fan
# date:      2023/12/1 001 17:49
# -----------------------------------------------------------
import os, sys
import pandas
import numpy
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


def gen_case_data(data_from=None, use_columns=None, use_row_num=1, case_register_submit=None):
    """
    从data文件生成用例数据，插入测试用例
    :param data_from: .data文件路径
    :param use_columns: 使用数据列，要求顺序
    :param use_row_num: 使用数据行数，至少为1
    :param case_register_submit: 插入用例文件路径
    :return: 0 正常结束返回0
    """
    use_row_num = int(use_row_num)
    if use_row_num < 1:
        use_row_num = 1
    if os.path.exists(data_from) and os.path.exists(case_register_submit):
        df = pandas.read_csv('data\\Register.data', encoding="utf-8")
        if set(use_columns) > set(df.columns):  # 使用字段溢出
            # print(set(use_columns))
            # print(set(df.columns))
            print('  use_column包含字段与数据源不匹配')
        else:
            new_df = pandas.DataFrame(df.loc[0:use_row_num-1, use_columns], columns=use_columns)  # 以use_columns为列名，取df前10行生成新表
            cases = []  # 定义用例列表（由case标题和case数据构成一个用例）
            for r in range(use_row_num):  # 逐行处理：
                case_title = f'case{list(new_df.loc[r, ["ID"]])[0]}\n'  # case标题
                # 从新表获取一行数据 转为字符串列表
                case_linel  = [f'{item}' if isinstance(item, numpy.int64) else item for item in new_df.loc[r, new_df.columns]]
                case_line ='    ' + '    '.join(case_linel) + '\n'  # 组装一行用例数据
                cases.append(case_title)
                cases.append(case_line)
            with open(case_register_submit, 'r', encoding='utf-8') as case_file:
                old_lines = case_file.readlines()  # 读取case文件（不包含case数据）
            new_lines = old_lines + cases  # 拼接case数据到case文件
            with open(case_register_submit, 'w', encoding='utf-8') as case_file:
                case_file.writelines(new_lines)  # 将数据写回原case文件
    else:
        print('  所引用的的文件不存在。')


if __name__ == '__main__':
    # 注册提交数据生成参数
    register_submit_data_conf = {
        'data_from': r'.\data\Register.data',
        'use_columns': ['ID', 'UNIT_NAME', 'UNIT_USCC', 'SAFER_NAME', 'SAFER_ID', 'SAFER_PHONE', 'SAFER_EMAIL',
            'IS_RECORDED', 'RECORDED_CODE', 'IP_ADDRESS'],
        'use_row_num': 5,
        'case_register_submit': r'.\tests\register_client\reg_register_submit_tests----.robot'
    }
    # 查看注册结果数据生成参数
    query_result_data_conf = {
        'data_from': r'.\data\Register.data',
        'use_columns': ['ID', 'UNIT_NAME', 'SAFER_NAME', 'SAFER_EMAIL'],
        'use_row_num': 10,
        'case_register_submit': r'.\tests\register_client\reg_query_result_tests.robot'
    }
    gen_case_data(**register_submit_data_conf)
