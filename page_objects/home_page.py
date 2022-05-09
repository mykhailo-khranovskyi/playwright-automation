import time

import allure
from playwright.async_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def main_search(self, searched_item):
        self.page.fill('.travel-search-input', searched_item)
        self.page.wait_for_selector('.travel-search-container__results')
        self.page.keyboard.press('ArrowDown')
        self.page.keyboard.press('Enter')
        self.page.wait_for_event('load')
