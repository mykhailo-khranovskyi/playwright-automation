from page_objects.base_page import BaseComponent, Element


class TextInput(BaseComponent):
    def __init__(self, selector: str):
        self.input = Element(f'{selector} input')

    def set_value(self, text):
        self.input.fill(text)

    def get_value(self):
        return self.input.get_attribute('value')
