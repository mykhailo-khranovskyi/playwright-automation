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

    @allure.step
    def sign_in(self, email, password):
        self.page.hover('.guest')
        self.page.click('body > div.header-bg > header > div.right-part > nav > ul > li:nth-child(3) > div > div > ul > li:nth-child(1) > a')
        self.page.fill('input', email)
        self.page.click('button')
        self.page.wait_for_selector('div.login__back')
        self.page.fill('input[type=password]', password)
        self.page.click('button')
        self.page.wait_for_selector('.logged-user')

    @allure.step
    def check_url(self):
        return self.page.url

    @allure.step
    def check_account_icon_displayed(self):
        return self.page.locator('.logged-user')
