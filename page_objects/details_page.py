import time
import re
import allure
from playwright.async_api import Page, expect


class DetailsPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def check_url(self):
        return self.page.url

    @allure.step
    def check_h1(self):
         raw = self.page.locator('h1').text_content()
         result = re.search(r'\w.+', raw)
         return result.group(0)

