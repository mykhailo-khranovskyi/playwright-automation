import allure
from playwright.async_api import Page


class DrListPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def search_by_resort_name(self, resort_name):
        self.page.fill("#filter-list > div.filter-row.clearfix > div > div > input", resort_name)
        self.page.keyboard.press("ArrowDown")

    @allure.step
    def check_resort_presented_in_list(self):
        return self.page.text_content('.resort-title')
