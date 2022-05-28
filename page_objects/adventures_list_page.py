import allure
from playwright.async_api import Page


class AdventuresListPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def get_shop_title(self):
        self.page.wait_for_selector('.resort-title.activity-title')
        return self.page.text_content('.resort-title.activity-title')

    @allure.step
    def click_view_details_btn(self):
        with self.page.context.expect_page() as new_page_info:
            self.page.click('.btn-red.activity-btn')  # Opens a new tab
        new_page = new_page_info.value

        new_page.wait_for_load_state()
        new_page.click('.btn.btn-red.mbn')

    # Get all new pages (including popups) in the context
    def handle_page(self, page):
        self.page.wait_for_load_state()
        print(self.page.title())
