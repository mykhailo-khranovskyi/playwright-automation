from components.input_field import TextInput
from page_objects.base_page import BaseComponent


class SearchInput(BaseComponent):
    def __init__(self, selector: str):
        self.selector = selector

    @property
    def input(self):
        return TextInput(self.selector)

    @property
    def auto_suggest_dropdown(self):
        return self.page.locator(f'{self.selector} ul[role=listbox]')

    def search_and_choose_first(self, text):
        self.input.set_value(text)
        self.auto_suggest_dropdown.wait_for()
        self.page.keyboard.press("ArrowDown")
