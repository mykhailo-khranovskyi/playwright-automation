import time
import allure


@allure.title('test autosuggest for DR')
def test_autosuggest_for_dr(padi_desktop_app):
    resort_name = 'BREATHLESS'
    padi_desktop_app.goto('/s/dive-resorts/all/')
    padi_desktop_app.dr_list_page.search_by_resort_name(resort_name)
    assert padi_desktop_app.dr_list_page.check_resort_presented_in_list() == resort_name
