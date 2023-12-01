#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: rf_db_ui_automate...RegisterSelector.py
# Author:    fan
# date:      2023/11/29 029 11:37
# -----------------------------------------------------------
class RegisterSelector:
    """
    备案注册页面 界面元素
    优先采取css选择器+文本选择器，示例（）：
    page.locator('css=div[role=dialog] button:has-text("确 定")').click()  # 文本模糊匹配模式
    page.locator('css=div[role=dialog] button>span:text("确 定")').click()  # 文本严格匹配模式
    page.locator('css=div[role=dialog] button >> text="确 定"').click()  # 复合匹配
    获取文本
    page.locator('div[class=el-row] h1').all_inner_texts()  # 模糊，返回字符串列表
    page.locator('div[class=el-row] h1').text_content()  # 严格，返回字符串
    """
    # 打开注册端
    DIALOG_OK_BUTTON = 'div[role=dialog] button:has-text("确 定")'  # 提示弹框
    PAGE_NAME = 'div[class=el-row] h1'  # 使用.text_content()方法获取精确文本
    FRONT_TAG = 'div[class="login-title el-row"]>ul>li:text("首页")'
    CHECK_RESULT_TAG = 'div[class="login-title el-row"]>ul>li:text("查询注册结果")'
    UPDATE_IP_TAG = 'div[class="login-title el-row"]>ul>li:text("设置公网IP地址")'
    QUESTIONS_TAG = 'div[class="login-title el-row"]>ul>li:text("常见问题")'
    # 首页
    FP_LOGIN_BUTTON = 'div[class=btn_box]>button>span:text("登 录")'  # 打开新标签页
    FP_REGISTER_BUTTON = 'div[class=btn_box]>button>span:text("注 册")'  # 保持在当前页面
    FP_MANUAL_BUTTON = 'div[class=btn_box]>button>span:text("查 看 手 册")'  # 打开新标签页
    FP_UNIT_REGIST_LINK = 'div[class="content_box___Lf_tu"] ul>li span:text("注册")'
    FP_CHECK_RESULT_LINK = 'div[class="content_box___Lf_tu"] ul>li span:text("查询")'
    FP_LOGIN_LINK = 'div[class="content_box___Lf_tu"] ul>li span:text("登录")'
    FP_QUESTIONS_LINK = 'div[class="content_box___Lf_tu"] ul>li span:text("这里")'
    # 注册（仍在'首页'范围内）
    RE_NAME = 'div[class="el-card__body"]>p>span:text("注册")'
    RE_UNIT_NAME_INPUT = 'div[class="el-card__body"] div>input[placeholder="单位名称(全称)"]'
    RE_UNIT_USCC_INPUT = 'div[class="el-card__body"] div>input[placeholder="统一社会信用代码"]'  # 官方确定的统一社会信用代码英文名缩写
    RE_SAFER_NAME_INPUT = 'div[class="el-card__body"] div>input[placeholder="安全员姓名"]'  # 安全员姓名
    RE_SAFER_ID_INPUT = 'div[class="el-card__body"] div>input[placeholder="安全员身份证号"]'  # 安全员身份证号
    RE_SAFER_PHONE_INPUT = 'div[class="el-card__body"] div>input[placeholder="安全员手机号"]'
    RE_SAFER_EMAIL_INPUT = 'div[class="el-card__body"] div>input[placeholder="安全员电子邮箱"]'
    RE_SEND_CAPTCHA_BUTTON = 'div[class="el-card__body"] button>span:has-text("发送验证码")'  # 发送验证码到邮箱
    RE_CAPTCHA_INPUT = 'div[class="el-card__body"] div>input[placeholder="获取邮箱验证码"]'  # 输入验证码
    RE_DOWNLOAD_ENTRUST_PAPER_LINK = 'div[class="el-card__body"] span>a>span:text("点击下载")'  # 下载委托书（模板）
    RE_UPLOAD_ENTRUST_PAPER_BUTTON = 'div[class="el-card__body"] button>span:text("上传委托书")'  # 上传委托书
    RE_UPLOAD_BUSINESS_LICENSE_BUTTON = 'div[class="el-card__body"] button>span:text("上传组织机构代码证/营业执照")' # 上传组织机构代码证/营业执照
    RE_UPLOAD_SAFER_IDCARD_PORTRAIT_BUTTON = 'div[class="el-card__body"] span>a>span:text("上传身份证人像面")'  # 身份证人像面
    RE_UPLOAD_SAFER_IDCARD_EMBLEM_BUTTON = 'div[class="el-card__body"] span>a>span:text("上传身份证国徽面")'  # 身份证国徽面
    RE_RECORDED_YES_RADIO = 'div[class="el-card__body"] div[role="radiogroup"] span:has-text("已备案")'  # 已备案
    RE_RECORDED_CODE_INPUT = 'div[class="el-card__body"] div>input[placeholder="备案表编号"]'  # 已备案编号,只有已备案才显示
    RE_RECORDED_NO_RADIO = 'div[class="el-card__body"] div[role="radiogroup"] span:has-text("未备案")'  # 未备案
    RE_IP_ADDRESS_INPUT = 'div[class="el-card__body"] div>input[placeholder="固定公网IP地址"]'  #
    RE_SUBMIT_BUTTON = 'div[class="el-card__body"] button>span:text("提 交")'  # 注册提交
    RE_CANCEL_BUTTON = 'div[class="el-card__body"] span>a>span:text("取 消")'  # 注册取消，返回

