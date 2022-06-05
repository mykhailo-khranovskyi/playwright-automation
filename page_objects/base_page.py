from typing import Union

from playwright.async_api import Page

from urls import FRONTEND_BASE_URL


class BaseComponent:
    def __get__(self, obj: Union['BasePage', 'BaseComponent'], objtype=None):
        if isinstance(obj, (BaseComponent, BasePage)):
            self.page = obj.page
        return self

    def __getattribute__(self, item):
        attr = super().__getattribute__(item)
        if isinstance(attr, (Element, BaseComponent)):
            attr.page = self.page
        return attr


class Element:
    def __init__(self, selector: str):
        self.selector = selector

    def __get__(self, obj: Union['BasePage', BaseComponent], objtype=None):
        if isinstance(obj, (BasePage, BaseComponent)):
            self.page = obj.page
        return self

    @property
    def find(self):
        return self.page.locator(self.selector).first

    def click(self, **kwargs):
        self.find.click(**kwargs)

    def text_content(self, **kwargs):
        return self.find.text_content(**kwargs)

    def text_custom(self, **kwargs):
        initial_text = self.text_content(**kwargs)
        return initial_text.replace('\n          ', '').strip()

    def evaluate(self, expression: str, **kwargs):
        self.find.evaluate(expression, **kwargs)

    def fill(self, value, **kwargs):
        self.find.fill(value, **kwargs)

    def get_attribute(self, name, **kwargs):
        return self.find.get_attribute(name, **kwargs)

    def wait_for(self, **kwargs):
        self.find.wait_for(**kwargs)


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self):
        self.page.goto(FRONTEND_BASE_URL + self.URL)

    def wait_for_load_state(self):
        self.page.wait_for_load_state()
