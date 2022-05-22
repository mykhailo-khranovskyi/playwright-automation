from page_objects.base_page import BaseComponent


class SearchFieldComponent(BaseComponent):
    def __init__(self, base_selector):
        self.base_selector = base_selector

    def search_and_choose(self, text):
        self.page.fill(self.base_selector + 'input', text)
        self.page.click(self.base_selector + '.typeahead-item')
