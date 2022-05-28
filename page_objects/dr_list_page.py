import allure

from components.search_input import SearchInput
from page_objects.base_page import BasePage


class DrListPage(BasePage):
    URL = '/s/dive-resorts/all/'
    resort_search_input = SearchInput('#filter-list > div.filter-row.clearfix > div > div')

    @allure.step
    def search_by_resort_name(self, resort_name):
        self.resort_search_input.set_value(resort_name)
        self.page.wait_for_selector('#react-autowhatever-1--item-0 > div')
        self.page.keyboard.press("ArrowDown")

    @allure.step
    def click_on_title(self):
        self.page.wait_for_selector('.resort-title')
        self.page.eval_on_selector('.resort-title', 'el => el.removeAttribute("target")')
        self.page.click('.resort-title')

    @allure.step
    def click_select_in_calendar(self):
        self.page.click('.travel-calendar.visible button.blue-btn')

    @allure.step
    def get_shop_title(self):
        self.page.wait_for_selector('.resort-title')
        return self.page.text_content('.resort-title')
