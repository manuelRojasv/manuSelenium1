from selenium import webdriver
import time
import HtmlTestRunner
import unittest
from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()



        '''self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id('btnLogin').click()
        self.driver.find_element_by_id('welcome').click()
        self.driver.find_element_by_link_text('Logout').click()'''
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test is completed')

if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Manu/PycharmProjects/manuSelenium1/reports"))