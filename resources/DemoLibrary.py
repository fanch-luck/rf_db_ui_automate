#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: robot_frame_demo...DemoLibrary
# Author:    fan
# date:      2023/11/16 016 14:05
# -----------------------------------------------------------
class DemoLibrary:
    def __init__(self, *args, **kwargs):
        print(f'Sample Library initialized with args: {args} and kwargs: {kwargs}')

    def my_keyword(self, *args, **kwargs):
        print(f'Kewword got args: {args} and kwargs: {kwargs}')
        return 'Hellow RobotFramework'
