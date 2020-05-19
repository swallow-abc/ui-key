from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = None
def open_browser(browser):
    global driver
    if "chrome" in browser.lower():
        print("启动谷歌浏览器")
        driver = webdriver.Chrome()
    elif "ie" in browser.lower():
        print("启动IE浏览器")
        driver = webdriver.Ie()
    elif "firefox" in browser.lower():
        print("启动火狐浏览器")
        driver = webdriver.Firefox()
    else:
        print("浏览器类型不存在，请重新检查！")
        exit()
    return driver

def geturl(url):
    print("打开网址.....")
    driver.get(url)
    driver.maximize_window()

def cloes_browser():
    print("关闭浏览器.....")
    driver.quit()

# 定义等待时间方法
def sleep_time(seconds):
    time.sleep(seconds)

# 隐性等待
def wait_implicitly(seconds):
    driver.implicitly_wait(seconds)

# 显性等待时间
def wait_webwait(seconds,local):
    try:
        WebDriverWait(driver,seconds).until(EC.invisibility_of_element_located(local))
    except:
        print("页面找不到元素")
    else:
        return driver.find_element(local)