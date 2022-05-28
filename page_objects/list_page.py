import allure
from playwright.async_api import Page


class ListPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def check_url(self):
        return self.page.url.split('?')[0]

    @allure.step
    def check_h1(self):
        return self.page.text_content('h1')
