import allure
from playwright.async_api import Page, expect


class VacationChekoutPage:
    def __init__(self, page: Page):
        self.page = page

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

    @allure.step
    def click_counter_plus_la(self):
        self.page.click('.cabin-prices__guests .counter-plus')
