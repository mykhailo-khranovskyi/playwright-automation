from components.input_field import TextInput
from page_objects.base_page import BaseComponent, Element


class SearchInput(BaseComponent):
    def __init__(self, selector: str):
        self.input = TextInput(selector)
        self.auto_suggest_dropdown = Element(f'{selector} ul[role=listbox]')

    def search_and_choose_first(self, text):
        self.input.set_value(text)
        self.auto_suggest_dropdown.wait_for()
        self.page.keyboard.press("ArrowDown")
