### 项目级复用的通用关键字（不依赖于页面内容）
*** Settings ***
Library           Browser    auto_closing_level=MANUAL
Library    OperatingSystem

*** Keywords ***
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
