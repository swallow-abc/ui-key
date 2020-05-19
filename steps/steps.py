from BasePage.basepage import *

driver = None
# 定义打开浏览器方法
def open_br(brow):
    global driver
    driver = br(brow)
    return driver

# 定义打开网页的方法
def get_url(url):
    geturl(url)

#定义输入关键字的方法
def input(xpath_pt,value):
    send_value(xpath_pt,value)

# 定义点击元素方法
def click_el(xpah_pt):
    click(xpah_pt)

# 定义期望结果判断方法
def except_result(exc):
    exc_result(exc)

# 定义关闭浏览器方法
def close_br():
    cloes_browser()

# 定义等待时间方法
def wait_time(seconds):
    sleep_time(seconds)

# 隐性等待
def wait_imp(seconds):
    print("等待页面加载.....")
    wait_implicitly(seconds)