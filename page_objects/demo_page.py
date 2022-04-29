from playwright.async_api import Page


class DemoPages:
    def __init__(self, page: Page):
        self.page = page

    def open_page_after_wait(self, wait_time: int):
        self.page.fill('.waitPageTime', str(wait_time))
        with self.page.expect_navigation(wait_until='load', timeout=(wait_time + 1) * 1000):
            self.page.click('.waitPage', no_wait_after=True)

    def check_wait_page(self):
        return 'Wait Page' == self.page.text_content('h3')

    def open_page_after_wait_ajax(self, wait_time: int):
        self.page.fill('.waitAjaxRequests', str(wait_time))
        self.page.click('.waitAjax')
        self.page.wait_for_load_state('networkidle')

    def get_ajax_responses_count(self):
        return len(self.page.query_selector_all('css=.ajaxResponses > p'))

    def click_new_page_button(self, ctrl_key=False):
        if ctrl_key:
            mod = ['Control']
        else:
            mod = None
        self.page.click('.newPage', modifiers=mod)

    def inject_js(self):
        js = '''
        console.error('This is injected error');
        alert('This is injected alert');        
        '''
        self.page.evaluate(js)




