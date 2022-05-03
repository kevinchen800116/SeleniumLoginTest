
from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time


class AddPage():
    inputBtn=(By.XPATH,'/html/body/div/div/div/main/div/div/div[1]/div/div/div[1]/input')
    DelFOp=(By.XPATH,'/html/body/div/div/div/main/div/div/div[2]/div[1]/div/div[3]/button/span/i')
    
    def AddInfo(self):
        self.find_element(*self.inputBtn).send_keys("selenium測試")
        time.sleep(1)
        self.find_element(*self.inputBtn).send_keys(Keys.ENTER)
        

    def DelFO(self):
        self.find_element(*self.DelFOp).click()

class kevinLogin(BasePage,AddPage):
    # 定位器，通过元素属性定位元素对象
    username_loc = (By.ID, 'input-10')
    password_loc = (By.ID, 'password')
    btn =(By.XPATH,'/html/body/div/div/div/main/div/div/div/div/div/div[2]/button')

    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)
        
    def click_loginBtn(self):
        self.find_element(*self.btn).click()
        
