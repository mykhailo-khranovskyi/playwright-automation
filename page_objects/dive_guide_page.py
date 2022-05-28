import allure
from playwright.async_api import Page


class DiveGuidePage:
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
    def select_dive_sites(self):
        self.page.click('.icon-dive-sites')

    @allure.step
    def click_on_dive_site(self):
        self.page.wait_for_selector('.operator-item-card')
        self.page.eval_on_selector('.operator-item-card', 'el => el.removeAttribute("target")')
        self.page.click('.operator-item-card')

    @allure.step
    def get_dive_site_title(self):
        return self.page.locator('.operator-item-card__title').text_content()

    @allure.step
    def get_dive_site_details_title(self):
        return self.page.locator('.dive-site-header__title').text_content()
