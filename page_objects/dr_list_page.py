import allure
from playwright.async_api import Page


class DrListPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def search_by_resort_name(self, resort_name):
        self.page.fill("#filter-list > div.filter-row.clearfix > div > div > input", resort_name)
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
