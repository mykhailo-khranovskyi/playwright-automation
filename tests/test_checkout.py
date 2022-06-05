import allure


@allure.title('DC-T99: test checkout page for DR')
def test_dr_checkout(padi_desktop_app):
    # Navigate to Dive Resorts List page
    padi_desktop_app.dr_list_page.visit()

    # Dive resorts list page actions
    dr_card = padi_desktop_app.dr_list_page.get_card_by_counter(1)
    list_shop_title = dr_card.title.text_content()
    dr_card.title.evaluate('el => el.removeAttribute("target")')  # TODO: handle second tab without this hack
    dr_card.title.click()

    # Detail page actions
    details_shop_title = padi_desktop_app.details_page.title.text_custom()
    padi_desktop_app.details_page.wait_for_load_state()
    padi_desktop_app.details_page.dates_prices_button.click()
    padi_desktop_app.details_page.customize_package_button.click()

    # Vacation checkout actions
    padi_desktop_app.vacation_checkout_page.continue_button.click()
    checkout_shop_title = padi_desktop_app.vacation_checkout_page.header_shop_title.text_content()
    checkout_shop_title_final_step = padi_desktop_app.vacation_checkout_page.shop_title.text_content()

    assert list_shop_title == details_shop_title == checkout_shop_title == checkout_shop_title_final_step


@allure.title('DC-T98: test checkout page for LA')
def test_la_checkout(padi_desktop_app):
    # Navigate to Dive Resorts List page
    padi_desktop_app.la_list_page.visit()

    # Liveaboards List page actions
    la_card = padi_desktop_app.la_list_page.get_card_by_counter(1)
    list_shop_title = la_card.title.text_content()
    la_card.title.evaluate('el => el.removeAttribute("target")')  # TODO: handle second tab without this hack
    la_card.title.click()

    # Detail page actions
    details_shop_title = padi_desktop_app.details_page.title.text_custom()
    padi_desktop_app.details_page.wait_for_load_state()
    padi_desktop_app.details_page.dates_prices_button.click()
    padi_desktop_app.details_page.select_cabin_button.click()

    # Vacation checkout actions
    padi_desktop_app.vacation_checkout_page.counter_plus_la.click()
    padi_desktop_app.vacation_checkout_page.continue_button.click()
    padi_desktop_app.vacation_checkout_page.continue_button.click()
    checkout_shop_title = padi_desktop_app.vacation_checkout_page.header_shop_title.text_content()
    checkout_shop_title_final_step = padi_desktop_app.vacation_checkout_page.shop_title.text_content()

    assert list_shop_title == details_shop_title == checkout_shop_title == checkout_shop_title_final_step


@allure.title('DC-T100: test checkout page for Diving')
def WIP_test_diving_checkout(padi_desktop_app):
    padi_desktop_app.adventures_list_page.visit()
    list_shop_title = padi_desktop_app.adventures_list_page.get_shop_title()
    with padi_desktop_app.page.context.expect_page() as details_page_info:
        padi_desktop_app.page.click('.btn-red.activity-btn')  # Opens a new tab
    details_page = details_page_info.value

    details_page.wait_for_load_state()
    details_page.click('.btn.btn-red.mbn')
    # padi_desktop_app.adventures_list_page.click_view_details_btn()
    padi_desktop_app.context.on("page", padi_desktop_app.adventures_list_page.handle_page(padi_desktop_app.adventures_details_page))
    padi_desktop_app.adventures_details_page.click_plus_btn()
