*** Settings ***
Resource        resources/Common.robot
Variables        data/RegisterConfig.py
Variables        data/RegisterSelector.py
Suite Setup    Context Init    注册端API测试开始
Suite Teardown    Context Clean    注册端API测试结束
Test Setup    Open Register Client    打开注册端页面
Test Teardown    Close Register Client    关闭注册端页面

*** Variables ***

*** Test Cases ***
Check Front API
#    ${front_page_id}=    Get Page Ids    ACTIVE    ACTIVE    ACTIVE    # 获取当前页面ID
    Click    ${FRONT_TAG}    # 点击“首页”
    Hover    ${FP_REGISTER_BUTTON}
    Click    ${CHECK_RESULT_TAG}    # 点击“查询注册结果”
    Hover    ${RR_NAME}  
    Click    ${QUESTIONS_TAG}    # 点击“查看常见问题”
    Hover    ${QU_NAME}
#    Click    ${UPDATE_IP_TAG}    # 点击“设置公网IP地址”
#    Hover    ${}
    Click    ${FRONT_TAG}    # 返回首页标签

    Click    ${FP_REGISTER_BUTTON}    # 点击注册按钮
    Hover    ${RE_NAME}    # 检测到标题“注册”
    Click    ${FRONT_TAG}
    
    Click    ${FP_REGIST_LINK}    # 点击注册链接
    Hover    ${RE_NAME}
    Click    ${FRONT_TAG}

    Click    ${FP_CHECK_RESULT_LINK}    # 点击查询
    Hover    ${RR_NAME}    #
    Click    ${FRONT_TAG}    #

    Click    ${FP_QUESTIONS_LINK}    # 点击这里
    Hover    ${QU_NAME}    #
    Click    ${FRONT_TAG}    #

    ${url1}=    Click To Get Url    ${FP_LOGIN_BUTTON}    # 点击按钮或者链接来打开新页面并获取该页面的URL，登录
    Should Be Equal    ${url1}    ${login_url}

    ${url1}=    Click To Get Url    ${FP_LOGIN_LINK}    # 点击按钮或者链接来打开新页面并获取该页面的URL，登录
    Should Be Equal    ${url1}    ${login_url}
    
    ${url2}=    Click To Get Url    ${FP_MANUAL_BUTTON}    # 查看手册
    Should Be Equal    ${url2}    ${manual_url}

    Sleep    5s


