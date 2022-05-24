from page_objects.base_page import BaseComponent


class TextInput(BaseComponent):
    def __init__(self, selector: str):
        self.selector = selector

    @property
    def input(self):
        return self.page.locator(f'{self.selector} input')

    def set_value(self, text):
        self.input.fill(text)

    def get_value(self):
        return self.input.get_attribute('value')
