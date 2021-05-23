from page_objects.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    path = '/index.php?route=account/login'

    def find_input_email(self):
        return self.browser.find_element_by_id('input-email')

    def find_continue_button(self):
        return self.browser.find_element_by_link_text('Continue')

    def find_input_password(self):
        return self.browser.find_element_by_xpath('//*[@id="input-password"]')

    def find_forgotten_password(self):
        return self.browser.find_element_by_link_text('Forgotten Password')

    def find_login_button(self):
        return self.browser.find_element_by_xpath('//*[@id="content"]//form/input')
