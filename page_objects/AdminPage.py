from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    path = '/admin/'

    def find_logo_open_cart(self):
        return self.browser.find_element_by_xpath("//img[@alt='OpenCart']")

    def find_input_username(self):
        return self.browser.find_element_by_name('username')

    def find_h1_in_form(self):
        return self.browser.find_element_by_xpath('//h1[contains(.," Please enter your login details.")]')

    def find_input_password(self):
        return self.browser.find_element_by_id('input-password')

    def find_login_button(self):
        return self.browser.find_element_by_xpath('//button[contains(.," Login")]')

    def login(self, login, password):
        self.browser.find_element_by_name('username').clear()
        self.browser.find_element_by_name('username').send_keys(login)
        self.browser.find_element_by_id('input-password').clear()
        self.browser.find_element_by_id('input-password').send_keys(password)
        self.browser.find_element_by_xpath('//button[contains(.," Login")]').click()
        return self

    def goto_all_product(self):
        self.browser.find_element_by_id('menu-catalog').click()
        self.browser.find_element_by_xpath('//a[contains(text(),"Products")]').click()
        return self

    def click_add_product(self):
        self.browser.find_element_by_css_selector('.fa-plus').click()

    def fill_general_form_product(self, name, title):
        self.browser.find_element_by_id('input-name1').send_keys(name)
        self.browser.find_element_by_id('input-meta-title1').send_keys(title)

    def goto_data_tab(self):
        self.browser.find_element_by_link_text('Data').click()

    def fill_data_tab_product(self, model):
        self.browser.find_element_by_id('input-model').send_keys(model)

    def click_save_product(self):
        self.browser.find_element_by_css_selector('.fa-save').click()

    def find_and_delete_product(self):
        self.browser.find_element_by_xpath('//tr[20]/td/input').click()
        self.browser.find_element_by_css_selector('.fa-trash-o').click()
