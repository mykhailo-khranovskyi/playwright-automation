import allure

from page_objects.base_page import BasePage, Element


class VacationCheckoutPage(BasePage):
    header_shop_title = Element('.shop-info h1')
    shop_title = Element('.shop-title')

    # Livaboard
    counter_plus_la = Element('.cabin-prices__guests .counter-plus')

    # Main navigation
    continue_button = Element('.btn-wrap .btn-red')

    @allure.step
    def click_continue_btn(self):
        self.page.click('.btn-wrap .btn-red')

    @allure.step
    def get_url(self):
        return self.page.url

    @allure.step
    def get_h1(self):
        return self.page.locator('h1').text_content()

    @allure.step
    def get_shop_title_final_step(self):
        return self.page.locator('.shop-title').text_content()
