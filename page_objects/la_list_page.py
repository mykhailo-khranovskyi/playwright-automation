import allure

from page_objects.base_page import BasePage


class LaListPage(BasePage):
    URL = '/s/liveaboards/all/'

    @allure.step
    def search_by_la_name(self, la_name):
        self.page.fill("#filter-list > div.filter-row.clearfix > div > div > input", la_name)
        self.page.wait_for_selector('#react-autowhatever-1--item-0 > div')
        self.page.keyboard.press("ArrowDown")

    @allure.step
    def get_shop_title(self):
        self.page.wait_for_selector('.shop-title')
        return self.page.text_content('.shop-title')

    @allure.step
    def click_on_title(self):
        self.page.wait_for_selector('.shop-title')
        self.page.eval_on_selector('.shop-title', 'el => el.removeAttribute("target")')
        self.page.click('.shop-title')

