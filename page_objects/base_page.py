from typing import Union

from playwright.async_api import Page

from urls import FRONTEND_BASE_URL


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self):
        self.page.goto(FRONTEND_BASE_URL + self.URL)


class BaseComponent:
    def __get__(self, obj: Union['BasePage', 'BaseComponent'], objtype=None):
        if isinstance(obj, (BaseComponent, BasePage)):
            self.page = obj.page
        return self

    def __getattribute__(self, item):
        attr = super().__getattribute__(item)
        if isinstance(attr, BaseComponent):
            attr.page = self.page
        return attr
