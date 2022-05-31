import allure
import re
from playwright.async_api import Page
from page_objects.base_page import BasePage


class ConservationActivityPage(BasePage):
    URL = '/conservation/activities/'

    @allure.step
    def search_from_main_page(self, searched_item):
        self.page.fill('.travel-search-input', searched_item)
        self.page.wait_for_selector('.travel-search-container__results')
        self.page.keyboard.press('ArrowDown')
        self.page.keyboard.press('Enter')
        self.page.wait_for_event('load')

    @allure.step
    def click_on_activity(self):
        self.page.wait_for_selector('.conservation-card')
        self.page.eval_on_selector('.conservation-card', 'el => el.removeAttribute("target")')
        self.page.click('.conservation-card')

    @allure.step
    def pick_a_date(self):
        self.page.click('.travel-datepicker')
        self.page.click('.travel-calendar-day.clickable.available')

    @allure.step
    def click_checkout_btn(self):
        self.page.click('.btn-guides-blue')

    @allure.step
    def get_list_title(self):
        raw = self.page.locator('.sites-section-title').text_content()
        result = re.search(r'(in )(.+)', raw)
        return result.group(2)

    @allure.step
    def get_activity_title(self):
        return self.page.locator('.conservation-card__title').text_content()

    @allure.step
    def get_details_activity_title(self):
        return self.page.text_content('h1')

    @allure.step
    def get_checkout_activity_title(self):
        return self.page.text_content('.activity-title')
