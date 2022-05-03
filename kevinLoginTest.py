from kevinLogin import kevinLogin
from selenium import webdriver
import traceback
import time
# from xvfbwrapper import Xvfb
# from pyvirtualdisplay import Display
import os

# driver = webdriver.Chrome(executable_path="chromedriver.exe")

# os.environ['DISPLAY'] = ':1'

# display = Display(visible=0, size=(800, 600))
# display.start()

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--start-fullscreen')
# 防止打印無用log
options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
options.add_argument('disable-infobars')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path=r"C:\Users\user\AppData\Local\Programs\Python\Python310\chromedriver.exe",chrome_options=options)
# driver.set_window_size(1200, 4500)
driver.implicitly_wait(30)
url = "https://kevinchen800116.github.io/login/#/login"
username = "qwer"
password = "1234"


try:
    # 声明LoginPage类对象
    login_page = kevinLogin(driver, url, u"login")
    login_page.open()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.take_screenshot()
    login_page.click_loginBtn()
    time.sleep(1)
    login_page.AddInfo()
    time.sleep(1)
    login_page.DelFO()
    time.sleep(10)
    driver.quit()

except Exception as e:

    print('有錯誤'+str(e))
    traceback.print_exc()
    driver.close()
    driver.quit()
finally:
    print('測試結束')
