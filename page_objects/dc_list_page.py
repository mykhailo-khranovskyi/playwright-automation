import allure

from page_objects.base_page import BasePage


class DcListPage(BasePage):
    URL = '/s/dive-centers/all/'

    @allure.step
    def search_by_dc_name(self, dc_name):
        self.page.fill("#filter-list > div.filter-row.clearfix > div > div > input", dc_name)
        self.page.wait_for_selector('#react-autowhatever-1--item-0 > div')
        self.page.keyboard.press("ArrowDown")

    @allure.step
    def get_shop_title(self):
        self.page.wait_for_selector('.resort-title')
        return self.page.text_content('.resort-title')

    @allure.step
    def click_on_title(self):
        self.page.wait_for_selector('.resort-title')
        self.page.eval_on_selector('.resort-title', 'el => el.removeAttribute("target")')
        self.page.click('.resort-title')
