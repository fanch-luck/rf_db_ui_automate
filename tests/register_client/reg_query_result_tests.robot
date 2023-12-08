*** Settings ***
Resource    resources/Common.robot
Resource    tests/templates/reg_query_result.robot
Variables        data/RegisterConfig.py
Variables        data/RegisterSelector.py
Test Template   Query Register Result
Suite Setup    Context Init    注册端测试
Suite Teardown    Context Clean    注册端测试结束
Test Setup    Open Register Client    打开注册端
Test Teardown    Close Register Client    关闭注册端

*** Test Cases ***
case1
    立信电子网络有限公司    徐萍    fch@fjjzwl.com
case2
    网新恒天传媒有限公司    陈玲    fch@fjjzwl.com
