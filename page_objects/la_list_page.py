import time

import allure
from playwright.async_api import Page


class LaListPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def search_by_la_name(self, la_name):
        self.page.fill("#filter-list > div.filter-row.clearfix > div > div > input", la_name)
        self.page.wait_for_selector('#react-autowhatever-1--item-0 > div')
        self.page.keyboard.press("ArrowDown")

    @allure.step
    def check_la_presented_in_list(self):
        return self.page.text_content('.shop-title')