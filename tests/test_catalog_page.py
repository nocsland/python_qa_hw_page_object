from page_objects.CatalogPage import CatalogPage


def tests_find_el_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_url()
    catalog_page.find_top_menu()
    catalog_page.find_left_menu()
    catalog_page.find_link_product_compare()
    catalog_page.find_class_input_group()
    catalog_page.find_search_button()

