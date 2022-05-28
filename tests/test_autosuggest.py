import allure


@allure.title('DC-T1120: test autosuggest for DR')
def test_autosuggest_for_dr(padi_desktop_app):
    resort_name = 'Breathless Cabo San Lucas Resort & Spa'
    padi_desktop_app.goto('/s/dive-resorts/all/')
    padi_desktop_app.dr_list_page.search_by_resort_name(resort_name)
    assert padi_desktop_app.dr_list_page.get_shop_title() == resort_name


@allure.title('DC-T1120: test autosuggest for LA')
def test_autosuggest_for_la(padi_desktop_app):
    la_name = 'Solomons PNG Master'
    padi_desktop_app.goto('/s/liveaboards/all/')
    padi_desktop_app.la_list_page.search_by_la_name(la_name)
    assert padi_desktop_app.la_list_page.get_shop_title() == la_name


@allure.title('DC-T1120: test autosuggest for DC')
def test_autosuggest_for_dc(padi_desktop_app):
    dc_name = 'QA_DC_TEST'
    padi_desktop_app.goto('/s/dive-centers/all/')
    padi_desktop_app.dc_list_page.search_by_dc_name(dc_name)
    assert padi_desktop_app.dc_list_page.get_shop_title() == dc_name
