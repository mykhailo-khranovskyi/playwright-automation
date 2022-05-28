import re
import allure
from playwright.async_api import Page


class DetailsPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def check_url(self):
        return self.page.url

    @allure.step
    def check_h1(self):
        raw = self.page.locator('h1').text_content()
        result = re.search(r'\w.+', raw)
        return result.group(0)

    @allure.step
    def click_view_dates_and_prices_btn(self):
        self.page.wait_for_url('')
        self.page.wait_for_load_state()
        self.page.click('.buttons-pan .btn.btn-red')

    @allure.step
    def click_customize_package_btn(self):
        self.page.click('.pricing-wrapper .btn-red')

    @allure.step
    def click_select_cabin_btn(self):
        self.page.click('.product-status-wrapper .btn-red')
