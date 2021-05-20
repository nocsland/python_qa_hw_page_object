from page_objects.MainPage import MainPage


def test_is_title(browser):
    main_page = MainPage(browser)
    main_page.open_url()
    main_page.verify_title('Your Store')


def test_find_el_main(browser):
    main_page = MainPage(browser)
    main_page.open_url()
    main_page.find_h1_your_store()
    main_page.find_name_search()
    main_page.find_id_cart()
    main_page.find_link_iphone()
    main_page.find_part_link_terms()


def test_add_new_user(browser):
    main_page = MainPage(browser)
    main_page.open_url()
    main_page.click_add_user()
    main_page.fill_register_form('Ivan7', 'Ivanov7', 'test7@ya.ru', '+79000551127', 'test')
    main_page.click_agree_and_continue()
    main_page.verify_title('My Account')


def test_switch_currency(browser):
    main_page = MainPage(browser)
    main_page.open_url()
    main_page.click_switch_currency()
    main_page.wait_css_element('button[name="EUR"]')
    main_page.click_to_currency('EUR')
    main_page.click_switch_currency()
    main_page.wait_css_element('button[name="GBP"]')
    main_page.click_to_currency('GBP')
    main_page.click_switch_currency()
    main_page.wait_css_element('button[name="USD"]')
    main_page.click_to_currency('USD')
