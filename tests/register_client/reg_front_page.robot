*** Settings ***
Library           Browser    auto_closing_level=MANUAL
Variables        data/RegisterSelector.py
Documentation    注册端首页
Suite Setup    Context Init
Suite Teardown    Context Clean
Test Setup    Log    Test开始
Test Teardown     Log    Test结束


*** Variables ***
${url}          https://192.168.0.222:18287/#/login
${url_title}    等保备案预登记系统
${temp_dir}    tmp
*** Test Cases ***
open_page
    New Page    ${url}
    Click    ${DIALOG_OK_BUTTON}
    ${got_title}=    Get Title
    Should Be Equal        ${got_title}    ${url_title}

check_api
    Click    ${FRONT_TAG}
    Get Text    ${FP_MANUAL_BUTTON}    ==    查 看 手 册
#    Click    ${CHECK_RESULT_TAG}
#    Click    ${UPDATE_IP_TAG}
#    Click    ${QUESTIONS_TAG}

regsiter_submit
    Click    ${FP_REGISTER_BUTTON}
    Get Text    ${RE_NAME}    ==    注册

*** Keywords ***
Context Init
    Log    注册端首页开始
    New Browser    chromium    headless=False
    Set Browser Timeout    10 seconds
    New Context    ignoreHTTPSErrors=True

Context Clean
    Sleep    5s
    Close Page
    Close Context
    Close Browser
    Log    注册端首页结束
    
