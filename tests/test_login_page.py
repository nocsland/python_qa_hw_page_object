from page_objects.LoginPage import LoginPage


def test_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_url()
    login_page.find_input_email()
    login_page.find_continue_button()
    login_page.find_input_password()
    login_page.find_forgotten_password()
    login_page.find_login_button()



