from page_objects.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductCardPage(BasePage):
    path = '/index.php?route=product/product&path=57&product_id=49'

    def find_h1_product(self):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(.,"Tweet")]')))
        return self.browser.find_element_by_xpath('//h1[contains(.,"Samsung Galaxy Tab 10.1")]')

    def find_button_add_to_cart(self):
        return self.browser.find_element_by_xpath('//*[@id="button-cart"]')

    def find_input_quantity(self):
        return self.browser.find_element_by_id('input-quantity')

    def find_write_a_review(self):
        return self.browser.find_element_by_link_text('Write a review')

    def find_tab_description(self):
        return self.browser.find_element_by_id('tab-description')
