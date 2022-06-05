import allure

from page_objects.base_page import BasePage, Element


class DetailsPage(BasePage):
    title = Element('h1')

    # View dates price section
    price_view = Element('#minimum-price span')
    dates_prices_button = Element('.buttons-pan .btn.btn-red')

    # Pricing cards for Dive resorts
    customize_package_button = Element('.pricing-wrapper .btn-red')

    # Pricing cards for Liveaboards
    select_cabin_button = Element('.product-status-wrapper .btn-red')

    @allure.step
    def check_url(self):
        return self.page.url
