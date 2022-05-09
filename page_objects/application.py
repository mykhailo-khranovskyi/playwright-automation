import logging
import allure
from playwright.sync_api import Browser
from playwright.sync_api import Request, Route, ConsoleMessage, Dialog
from .TBD_test_cases import TestCases
from .TBD_demo_page import DemoPages
from .dr_list_page import DrListPage
from .la_list_page import LaListPage
from .dc_list_page import DcListPage
from .home_page import HomePage
from .list_page import ListPage
from .details_page import DetailsPage


class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(http_credentials={"username": "diviac", "password": "rembo"}, **kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_cases = TestCases(self.page)
        self.demo_pages = DemoPages(self.page)
        self.dr_list_page = DrListPage(self.page)
        self.la_list_page = LaListPage(self.page)
        self.dc_list_page = DcListPage(self.page)
        self.home_page = HomePage(self.page)
        self.list_page = ListPage(self.page)
        self.details_page = DetailsPage(self.page)


        def console_handler(message: ConsoleMessage):
            if message.type == 'error':
                logging.error(f'page {self.page.url}, console error: {message.text}')

        def dialog_handler(dialog: Dialog):
            logging.warning(f'page {self.page.url}, dialog text: {dialog.message}')
            dialog.accept()

        self.page.on('console', console_handler)
        self.page.on('dialog', dialog_handler)

    @allure.step
    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    @allure.step
    def navigate_to(self, menu:str):
        self.page.locator(f"css=header >> text='{menu}'").click()
        self.page.wait_for_load_state()

    @allure.step
    def login(self, login: str, password: str):
        self.page.fill("input[name=\"username\"]", login)
        self.page.fill("input[name=\"password\"]", password)
        self.page.locator("text=Login").click()

    @allure.step
    def create_test(self, test_name: str, test_description: str):
        self.page.fill("input[name=\"name\"]", test_name)
        self.page.fill("textarea[name=\"description\"]", test_description)
        self.page.locator("input:has-text(\"Create\")").click()

    @allure.step
    def click_menu_button(self):
        self.page.click('.menuBtn')

    @allure.step
    def is_menu_button_visible(self):
        return self.page.is_visible('.menuBtn')

    @allure.step
    def get_location(self):
        return self.page.text_content('.position')

    @allure.step
    def intercept_requests(self, url: str, payload: str):
        def handler(route: Route, request: Request):
            route.fulfill(status=200, body=payload)
        self.page.route(url, handler)

    @allure.step
    def stop_intercept(self, url: str):
        self.page.unroute(url)

    @allure.step
    def refresh_dashboard(self):
        self.page.click('input')
        self.page.wait_for_event('response')

    @allure.step
    def get_total_tests_stats(self):
        return self.page.text_content('.total >> span')

    @allure.step
    def close(self):
        self.page.close()
        self.context.close()
