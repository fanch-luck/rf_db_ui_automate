*** Settings ***
Resource    resources/Common.robot
Resource    tests/templates/reg_register_submit.robot
Variables        data/RegisterConfig.py
Variables        data/RegisterSelector.py
Test Template   register_submit
Suite Setup    Context Init    注册端测试
Suite Teardown    Context Clean    注册端测试结束
Test Setup    Start Case    打开注册提交页面
Test Teardown    Finish Case    关闭注册提交页面

*** Test Cases ***
case1
    立信电子网络有限公司    717761201952857786    徐萍    330601197503247281    15013169505    fch@jzwl.com    1    80285361446    192.88.107.193
case2
    网新恒天传媒有限公司    296154249513110934    陈玲    210882200106268165    13952525960    fch@jzwl.com    0    89641630512    203.1.190.153


*** Keywords ***
Start Case
    [Arguments]    ${comment}
    Log    ${comment}
    New Page    ${base_url}
    Click    ${DIALOG_OK_BUTTON}
    ${got_title}=    Get Title
    Should Be Equal        ${got_title}    ${client_title}
    Click    ${FP_REGISTER_BUTTON}
    Get Text    ${RE_NAME}    ==    注册
    Sleep    2s

Finish Case
    [Arguments]    ${comment}
    Log    ${comment}
    Close Page


