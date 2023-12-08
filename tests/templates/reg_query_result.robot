*** Settings ***
Resource        resources/Common.robot
Variables        data/RegisterConfig.py
Variables        data/RegisterSelector.py

*** Keywords ***
Query Register Result
    [Arguments]    ${UNIT_NAME}    ${SAFER_NAME}    ${SAFER_EMAIL}
    Log    正在查询注册结果
    Click    ${CHECK_RESULT_TAG}    # 点击查询注册结果
    Hover    ${RR_NAME}
    Fill Text    ${RR_UNIT_NAME_INPUT}    ${UNIT_NAME}    
    Fill Text    ${RR_SAFER_NAME_INPUT}    ${SAFER_NAME}
    Fill Text    ${RR_SAFER_EMAIL_INPUT}    ${SAFER_EMAIL}
    Click    ${RR_QUERY_BUTTON}    # 点击查询
    ${svg_class}=    Get Attribute    ${RR_QUERY_RESULT_UNDER_REVIEW}    class
    Log    ${svg_class}
    Click     ${RR_QUERY_RETURN_BUTTON}
    Sleep    5s