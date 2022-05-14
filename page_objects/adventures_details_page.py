import allure
from playwright.async_api import Page


class AdventureDetailsPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def click_plus_btn(self):
        self.page.click('.plus-minus-btn.plus')

