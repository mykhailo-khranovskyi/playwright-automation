import allure


@allure.title('DC-T854: test conservation activity flow')
def test_conservation_main_page(padi_desktop_app):
    destination = 'Ukraine'
    padi_desktop_app.conservation_activity_page.visit()
    padi_desktop_app.conservation_activity_page.search_from_main_page(destination)
    actual_destination = padi_desktop_app.conservation_activity_page.get_list_title()
    activity_title = padi_desktop_app.conservation_activity_page.get_activity_title()
    padi_desktop_app.conservation_activity_page.click_on_activity()
    details_activity_title = padi_desktop_app.conservation_activity_page.get_details_activity_title()
    padi_desktop_app.conservation_activity_page.pick_a_date()
    padi_desktop_app.conservation_activity_page.click_checkout_btn()
    checkout_activity_title = padi_desktop_app.conservation_activity_page.get_checkout_activity_title()
    assert destination == actual_destination
    assert activity_title == details_activity_title == checkout_activity_title
