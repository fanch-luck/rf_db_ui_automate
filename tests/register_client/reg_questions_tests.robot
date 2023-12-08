*** Settings ***
Resource        resources/Common.robot
Variables        data/RegisterConfig.py
Variables        data/RegisterSelector.py
Suite Setup    Context Init    注册端API测试开始
Suite Teardown    Context Clean    注册端API测试结束
Test Setup    Open Register Client    打开注册端页面
Test Teardown    Close Register Client    关闭注册端页面

*** Test Cases ***
Check Questions Number
    Click    ${QUESTIONS_TAG}
    Hover    ${QU_NAME}
    Get Element Count    ${QU_QUESTION}    ==    ${questions_number}
