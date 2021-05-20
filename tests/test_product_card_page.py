from page_objects.ProductCardPage import ProductCardPage


def tests_product_card_page(browser):
    product_card_page = ProductCardPage(browser)
    product_card_page.open_url()
    product_card_page.find_h1_product()
    product_card_page.find_button_add_to_cart()
    product_card_page.find_input_quantity()
    product_card_page.find_write_a_review()
    product_card_page.find_tab_description()


