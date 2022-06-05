import allure

from components.search_input import SearchInput
from page_objects.base_page import BasePage, BaseComponent, Element


class DrListCard(BaseComponent):
    def __init__(self, selector: str, page):
        self.page = page
        self.title = Element(f'{selector} .resort-title')


class DrListPage(BasePage):
    URL = '/s/dive-resorts/all/'
    resort_search_input = SearchInput('#filter-list > div.filter-row.clearfix > div > div')

    def get_card_by_counter(self, counter):
        return DrListCard(f'div.search-page-item-card:nth-of-type({counter})', page=self.page)

    @allure.step
    def get_shop_title(self):
        self.page.wait_for_selector('.resort-title')
        return self.page.text_content('.resort-title')
