from page_objects.AdminPage import AdminPage


def test_find_el_on_admin_page(browser):
    admin_page = AdminPage(browser).open()
    admin_page.find_logo_open_cart()
    admin_page.find_input_username()
    admin_page.find_h1_in_form()
    admin_page.find_input_password()
    admin_page.find_login_button()


def test_add_product(browser):
    admin_page = AdminPage(browser).open()
    admin_page.login('user', 'bitnami')
    admin_page.verify_title('Dashboard')
    admin_page.goto_all_product()
    admin_page.verify_title('Products')
    admin_page.click_add_product()
    admin_page.fill_general_form_product('test', 'test')
    admin_page.goto_data_tab()
    admin_page.fill_data_tab_product('test')
    admin_page.click_save_product()
    admin_page.wait_css_element('.alert-dismissible')


def test_delete_product(browser):
    admin_page = AdminPage(browser)
    admin_page.goto_all_product()
    admin_page.verify_title('Products')
    admin_page.find_and_delete_product()
    admin_page.switch_to_alert_and_ok()
    admin_page.wait_css_element('.alert-dismissible')
