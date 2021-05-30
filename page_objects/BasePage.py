from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    path = None

    def __init__(self, browser):
        self.browser = browser
        self.url = browser.url

    def open(self):
        self.browser.get(self.url + self.path)
        return self

    def verify_title(self, title):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.title_is(title))
        assert self.browser.title == title
        return self

    def switch_to_alert_and_ok(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def wait_css_element(self, selector):
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def click_switch_currency(self):
        self.browser.find_element_by_id('form-currency').click()

    def click_to_currency(self, currency):
        self.browser.find_element_by_css_selector(f'button[name="{currency}"]').click()
