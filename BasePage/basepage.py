from BasePage.browser import *

driver = None
# 定义打开浏览器方法
def br(brow):
    global driver
    driver = open_browser(brow)
    return driver

def find_element(local):
    try:
        element = driver.find_element_by_xpath(local)
    except Exception as e:
        print("页面找不到元素，原因是-%s" %e)
        exit()
        print(driver)
    else:
        return element

def send_value(local,value):
    print("输入测试内容.....")
    find_element(local).send_keys(value)

def click(local):
    print("点击按钮.....")
    find_element(local).click()

def exc_result(exc_result):
    try:
        assert exc_result in driver.page_source
    except:
        print("期望结果-%s,测试失败" % exc_result)
    else:
        print("期望结果-%s,测试通过!" % exc_result)