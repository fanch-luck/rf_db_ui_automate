*** Settings ***
Library          Browser    # 与resource的库设置一致
Variables        data/RegisterSelector.py
Variables        data/RegisterConfig.py
Resource         resources/Common.robot

*** Keywords ***
register_submit
    [Arguments]    ${UNIT_NAME}    ${UNIT_USCC}    ${SAFER_NAME}    ${SAFER_ID}    ${SAFER_PHONE}    ${SAFER_EMAIL}    ${RECORDED}    ${RECORDED_CODE}    ${IP_ADDRESS}
    Log    正在提交注册资料
    Fill Text    ${RE_UNIT_NAME_INPUT}    ${UNIT_NAME}
    Fill Text    ${RE_UNIT_USCC_INPUT}   ${UNIT_USCC}
    Fill Text    ${RE_SAFER_NAME_INPUT}    ${SAFER_NAME}
    Fill Text    ${RE_SAFER_ID_INPUT}    ${SAFER_ID}
    Fill Text    ${RE_SAFER_PHONE_INPUT}    ${SAFER_PHONE}
    Fill Text    ${RE_SAFER_EMAIL_INPUT}    ${SAFER_EMAIL}
    Click    ${RE_SEND_CAPTCHA_BUTTON}
    ${captcha}=    Get Email Captcha    ${email_config}  # 使用data/RegisterConfig.py的邮箱配置，提取邮箱验证码
    Fill Text    ${RE_CAPTCHA_INPUT}    ${captcha}
    Click To Download    ${RE_DOWNLOAD_ENTRUST_PAPER_LINK}    ${download_dir}\\单位授权委托书.docx    # 下载委托书模板
    Sleep    ${operation_interval}
    Click To Upload    ${RE_UPLOAD_ENTRUST_PAPER_BUTTON}    ${annexes_dir}\\单位授权委托书.jpg    # 上传委托书
    Sleep    ${operation_interval}
    Click To Upload    ${RE_UPLOAD_BUSINESS_LICENSE_BUTTON}    ${annexes_dir}\\测试营业执照.png    # 上传营业执照
    Sleep    ${operation_interval}
    Click To Upload    ${RE_UPLOAD_SAFER_IDCARD_PORTRAIT_BUTTON}    ${annexes_dir}\\身份证人像面.jpg
    Sleep    ${operation_interval}
    Click To Upload    ${RE_UPLOAD_SAFER_IDCARD_EMBLEM_BUTTON}    ${annexes_dir}\\身份证国徽面.jpg
    Sleep    ${operation_interval}
    Run Keyword If    ${RECORDED}    Click    ${RE_RECORDED_YES_RADIO}    ELSE    Click    ${RE_RECORDED_NO_RADIO}
    Run Keyword If    ${RECORDED}    Fill Text    ${RE_RECORDED_CODE_INPUT}    ${RECORDED_CODE}
    Fill Text    ${RE_IP_ADDRESS_INPUT}    ${IP_ADDRESS}
    Click    ${RE_SUBMIT_BUTTON}    # 提交注册
    Sleep    ${operation_interval}
    Hover    ${RE_FINISHED_TEXT}    # 注册完成！文本
    Click    ${RE_FINISHED_RETURN_BUTTON}    # 返回
    Sleep    ${operation_interval}

