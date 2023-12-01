#!usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: PythonVariables.py
# Author:    fan20200225
# Date:      2023/11/19 0019
# -----------------------------------------------------------
from faker import Faker


class StudentA:
    name = 'Li Hua'
    age = 18
    subjects = ['math', 'english', 'history']
    info = {'province': 'fujian', 'email': '350001'}


py_scalar = 'robot framework'
py_scalar2 = 'openai'
py_list = ['r', 'o', 'b', 'o', 't']
py_dict = {'name': 'robot', 'password': 'framework'}


def get_rand_student():
    fake = Faker()
    return dict(
        name=fake.name(),
        age=18,
        classes=['math', 'english', 'history'],
        info={'province': 'guangdong', 'email': fake.ascii_email()}
    )


studentB = get_rand_student()
