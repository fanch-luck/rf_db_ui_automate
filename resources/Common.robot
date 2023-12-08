### 项目级复用的通用关键字（不依赖于页面内容）
*** Settings ***
Library        Browser    auto_closing_level=MANUAL
Library        OperatingSystem
Library        resources/UtilLibrary.py
#Variables    data/RegisterConfig.py
#
#*** Test Cases ***
#Test Email Captcha
#    #Log Many    &{email_config}
#    ${captcha}    Get Email Captcha    ${email_config}
#    Log    ${captcha}

*** Keywords ***
Get Email Captcha
    # 检查邮件验证码
    [Arguments]    ${email_conf}
    ${captcha}=    get_em_captcha    ${email_conf}
    [Return]    ${captcha}

Click To Upload
    # 点击一个元素并选择一个文件上传
    [Arguments]    ${selector}    ${filepath}
    ${promise}=    Promise To Upload File    ${filepath}
    Click    ${selector}
    ${upload_result}=    Wait For    ${promise}

Click To Download
    # 点击一个元素来下载文件。若文件存在则覆盖。
    [Arguments]    ${selector}    ${filepath}
    ${promise}=    Promise To Wait For Download    saveAs=${filepath}
    Click    ${selector}
    ${file_obj}=    Wait For    ${promise}
    File Should Exist    ${file_obj}[saveAs]
#    Should Be True    ${file_obj.suggestedFilename}    # 平台设置本身错误

Click To Get Url
    # 点击元素打开新页面并获取页面uid然后关闭该页面
    [Arguments]    ${selector}
    Click    ${selector}    # 点击登录，打开新标签
    ${previous_page_id}=    Switch Page    NEW    # 切换页面到新打开页面，然后返回前一页的ID
    ${new_url}=    Get Url    
    ${new_page_id}=    Switch Page    ${previous_page_id}
    Close Page    ${new_page_id}    # 关闭页面
    [Return]    ${new_url}

Context Init    
    [Arguments]    ${comment}
    Log    ${comment}
    New Browser    chromium    headless=False    downloadsPath=${temp_dir}
    Set Browser Timeout    10 seconds
    New Context    ignoreHTTPSErrors=True

Context Clean
    [Arguments]    ${comment}
    Sleep    3s
    Close Context
    Close Browser
    Log    ${comment}

Open Register Client
    [Arguments]    ${comment}
    Log    ${comment}
    New Page    ${base_url}
    Click    ${DIALOG_OK_BUTTON}
    ${got_title}=    Get Title
    Should Be Equal        ${got_title}    ${client_title}

Close Register Client
    [Arguments]    ${comment}
    Log    ${comment}
    Close Page