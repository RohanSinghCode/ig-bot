from selenium import webdriver
import os 
import time

class InstagramBot:

    def __init__(self, username,password):
        ''' 
        Args:
            username : The instagram username for a user
            Password : The instagram password for a user
        Attributes:
            driver: Selenium.webdriver.Chrome: Automate Chrome function
        '''
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.implicitly_wait(20)
        self.login()

    def login(self):
        self.driver.get('{}/accounts/login'.format(self.base_url))

        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        
        time.sleep(2)

    def nav_user(self,user):
        self.driver.get('{}/{}'.format(self.base_url,user))

    def follow_user(self,user):
        self.nav_user(user)
        follow_button = self.driver.find_element_by_xpath("//*[text()='Follow']")
        follow_button.click()
        


if __name__== '__main__':
    ig_bot = InstagramBot('your_username','your_password')
    ig_bot.follow_user('rohhannsinnghh')

    