import allure


@allure.title('DC-T628: test dive guide flow')
def test_dive_guide_page(padi_desktop_app):
    padi_desktop_app.goto('/exploration/')
    padi_desktop_app.dive_guide_page.main_search('Ukraine')
    padi_desktop_app.dive_guide_page.select_dive_sites()
    main_page_dive_site_title = padi_desktop_app.dive_guide_page.get_dive_site_title()
    padi_desktop_app.dive_guide_page.click_on_dive_site()
    dive_site_details_title = padi_desktop_app.dive_guide_page.get_dive_site_details_title()
    assert main_page_dive_site_title == dive_site_details_title
