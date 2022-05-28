import time
import allure


@allure.title('DC-T99: test checkout page for DR')
def test_dr_checkout(padi_desktop_app):
    padi_desktop_app.goto('/s/dive-resorts/all/')
    list_shop_title = padi_desktop_app.dr_list_page.get_shop_title()
    padi_desktop_app.dr_list_page.click_on_title()
    details_shop_title = padi_desktop_app.details_page.check_h1()
    padi_desktop_app.details_page.click_view_dates_and_prices_btn()
    padi_desktop_app.details_page.click_customize_package_btn()
    padi_desktop_app.vacation_checkout_page.click_continue_btn()
    checkout_shop_title = padi_desktop_app.vacation_checkout_page.get_h1()
    checkout_shop_title_final_step = padi_desktop_app.vacation_checkout_page.get_shop_title_final_step()
    assert list_shop_title == details_shop_title == checkout_shop_title == checkout_shop_title_final_step


@allure.title('DC-T98: test checkout page for LA')
def test_la_checkout(padi_desktop_app):
    padi_desktop_app.goto('/s/liveaboards/all/')
    list_shop_title = padi_desktop_app.la_list_page.get_shop_title()
    padi_desktop_app.la_list_page.click_on_title()
    details_shop_title = padi_desktop_app.details_page.check_h1()
    padi_desktop_app.details_page.click_view_dates_and_prices_btn()
    padi_desktop_app.details_page.click_select_cabin_btn()
    padi_desktop_app.vacation_checkout_page.click_counter_plus_la()
    padi_desktop_app.vacation_checkout_page.click_continue_btn()
    padi_desktop_app.vacation_checkout_page.click_continue_btn()
    checkout_shop_title = padi_desktop_app.vacation_checkout_page.get_h1()
    checkout_shop_title_final_step = padi_desktop_app.vacation_checkout_page.get_shop_title_final_step()
    assert list_shop_title == details_shop_title == checkout_shop_title == checkout_shop_title_final_step


@allure.title('DC-T100: test checkout page for Diving')
def WIP_test_diving_checkout(padi_desktop_app):
    padi_desktop_app.goto('/s/diving/all/')
    list_shop_title = padi_desktop_app.adventures_list_page.get_shop_title()
    with padi_desktop_app.page.context.expect_page() as details_page_info:
        padi_desktop_app.page.click('.btn-red.activity-btn')  # Opens a new tab
    details_page = details_page_info.value

    details_page.wait_for_load_state()
    details_page.click('.btn.btn-red.mbn')
    # padi_desktop_app.adventures_list_page.click_view_details_btn()
    padi_desktop_app.context.on("page", padi_desktop_app.adventures_list_page.handle_page(padi_desktop_app.adventures_details_page))
    padi_desktop_app.adventures_details_page.click_plus_btn()
