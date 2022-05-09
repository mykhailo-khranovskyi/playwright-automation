import time

import allure
from playwright.async_api import Page


class DcListPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def search_by_dc_name(self, dc_name):
        self.page.fill("#filter-list > div.filter-row.clearfix > div > div > input", dc_name)
        self.page.wait_for_selector('#react-autowhatever-1--item-0 > div')
        self.page.keyboard.press("ArrowDown")

    @allure.step
    def check_dc_presented_in_list(self):
        return self.page.text_content('.resort-title')
