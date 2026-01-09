from selenium import webdriver
import pytest
import undetected_chromedriver as uc

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = uc.Chrome()
        print("Launching Chrome browser....")

        # driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser....")

    else:
        driver = webdriver.Edge()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# pytest html report 使用专门处理 metadata 的钩子
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    # 直接修改字典，不需要通过 config._
    metadata['Project Name'] = "nopCommerce demo"
    metadata['Module Name'] = "Login"
    metadata['Tester'] = "Elisa"

    # 你甚至可以在这里删除一些不想在报告里显示的信息
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)

# 运行pytest -v -s --html=Reports\report.html testCases/test_login.py --browser chrome

# 运行时指定浏览器 pytest -v -s testCase/test_login.py --browser chrome
# 同时开多个窗口运行代码 pytest -v -s -n=3 testCases/test_login.py --browser chrome
# n最大是3 不然就会运行很慢

# pytest html report
# def pytest_configure(config):
#     config._metadata['Project Name'] = "nopCommerce demo"
#     config._metadata['Module Name'] = "Customers"
#     config._metadata['Tester'] = "Pavan"
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

