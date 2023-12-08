#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: db_ui...verify
# Author:    fan
# date:      2023/7/31 031 15:01
# -----------------------------------------------------------

# 提供验证码校验接口

import ddddocr
import base64


def base64tohex(base64_src: str) -> bytes:
    """
    base64图片解码
    :param base64_src: 网页图片base64编码，如"data:image/jpeg;base64,/9j/...."
    :return: 图片字节码
    """
    image_base64 = base64_src.split(",")[-1]
    image_hex = base64.b64decode(image_base64)
    return image_hex


def get_target_loc(slide: bytes, background: bytes) -> dict:
    """
    获取缺口位置大小信息
    :param slide: slide image hex
    :param background: background image hex
    :return: like {'target_y': 0, 'target': [331, 0, 441, 360]}
    """
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    res = det.slide_match(
        slide,
        background
    #    simple_target=True
    )
    return res


def filetohex(imagepath: str) -> bytes:
    """
    图片编码
    :param imagepath: 图片路径
    :return: 图片字节码
    """
    with open(imagepath, "rb") as f:
        image_hex = f.read()
    return image_hex


if __name__ == "__main__":
    sb = filetohex("../slide.png")
    bb = filetohex("../bg.jpg")
    loc = get_target_loc(sb, bb)
    print(loc)
