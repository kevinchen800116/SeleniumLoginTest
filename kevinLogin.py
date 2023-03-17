
from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time


class AddPage():
    inputBtn=(By.XPATH,'/html/body/div/div/div/main/div/div/div[1]/div/div/div[1]/input')
    DelFOp=(By.XPATH,'/html/body/div/div/div/main/div/div/div[2]/div[1]/div/div[3]/button/span/i')
    LeaveBtn=(By.XPATH,"/html/body/div/div/div/header/div[2]/button[4]/span/i")
    
    selectionBtn=(By.CLASS_NAME,"v-input--selection-controls__ripple")
    
    def click_selectionBtn(self,i):
        BTN=self.find_elements(*self.selectionBtn)
        BTN[i].click()
        
    def quiteBtn(self):
        self.find_element(*self.LeaveBtn).click()
    def AddInfo(self,text):
        self.find_element(*self.inputBtn).send_keys(text)
        time.sleep(1)
        self.find_element(*self.inputBtn).send_keys(Keys.ENTER)
        

    def DelFO(self):
        time.sleep(1)
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
        
