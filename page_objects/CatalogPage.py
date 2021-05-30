from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    path = '/index.php?route=product/category&path=20'

    def find_top_menu(self):
        return self.browser.find_element_by_css_selector('#top > div.container')

    def find_left_menu(self):
        return self.browser.find_element_by_id('column-left')

    def find_link_product_compare(self):
        return self.browser.find_elements_by_partial_link_text('Product Compare')

    def find_class_input_group(self):
        return self.browser.find_element_by_class_name('input-group')

    def find_search_button(self):
        return self.browser.find_element_by_xpath('//*[@id="search"]/span/button')
