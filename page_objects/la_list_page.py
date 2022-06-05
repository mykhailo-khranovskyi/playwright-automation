import allure

from page_objects.base_page import BasePage, Element, BaseComponent


class LaListCard(BaseComponent):
    def __init__(self, selector: str, page):
        self.page = page
        self.title = Element(f'{selector} .shop-title')


class LaListPage(BasePage):
    URL = '/s/liveaboards/all/'

    def get_card_by_counter(self, counter):
        return LaListCard(f'div.search-page-item-card:nth-of-type({counter})', page=self.page)

    @allure.step
    def get_shop_title(self):
        self.page.wait_for_selector('.shop-title')
        return self.page.text_content('.shop-title')
