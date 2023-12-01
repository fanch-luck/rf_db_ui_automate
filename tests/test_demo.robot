*** Settings ***
Force Tags        Browser
Library           Browser
Documentation    suites级文档
Suite Setup    Log_to_server    # 在当前文件所有Test Cases执行前执行
Suite Teardown    Quit_from_Server    # 在当前文件所有Test Cases执行后执行
Test Setup    Log    Test开始    # 在当前文件每个Test Case执行前执行。会被Test Case内定义的Setup覆盖。
Test Teardown     Log    Test结束    # 在当前文件每个Test Case执行后执行。会被Test Case内定义的Teardown覆盖。


*** Variables ***
${搜索关键词}          百度一下，你就知道

*** Test Cases ***
test_baidu
#    [Tags]    Browser    playwright    浏览器
#    [Timeout]    30 seconds
#    New Browser    chromium    headless=No
#    Set Browser Timeout    60 sec
    New Page    https://www.baidu.com/
    ${title}=    Get Title
    Should Be Equal    ${title}    ${搜索关键词}
    Sleep    2s
    Close Page
#    [Teardown]    Close Page    #关闭浏览器

test_sina
    New Page    https://www.sina.cn/
    ${page_title}=    Get Title    
    Should Be Equal    ${page_title}    手机新浪网
    Sleep    2s
    Close Page

*** Keywords ***
Log_to_server
    Log    Suite开始
    New Browser    chromium    headless=No
    Set Browser Timeout    60 sec

Quit_from_Server
    Close Browser
    Log    Suite结束