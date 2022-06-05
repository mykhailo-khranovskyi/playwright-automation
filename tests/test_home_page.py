import allure
from pytest import mark

ddt_for_location_search = {'argnames': 'location,url,h1',
       'argvalues': [('Maldives', 'https://travel.padi.comingsoon.rocks/s/liveaboards/maldives/', '1 liveaboard in the Maldives'),
                     ('Київ', 'https://travel.padi.comingsoon.rocks/s/dive-centers/kiyiv/', '1 dive centers  near Kyiv')],
       'ids': ['DC-T97: test main search by location',
               'DC-T97: test main search by place id']}

ddt_for_shop_search = {'argnames': 'shop_name,url,h1',
       'argvalues': [('Pura Vida Beach & Dive Resort', 'https://travel.padi.comingsoon.rocks/dive-resort/philippines/pura-vida-beach-dive-resort-company/', 'Pura Vida Beach & Dive Resort'),
                     ('Arabian Aggressor', 'https://travel.padi.comingsoon.rocks/liveaboard/sudan/arabian-aggressor/', 'Arabian Aggressor')],
       'ids': ['DC-T97: test main search by shop name (DR)',
               'DC-T97: test main search by shop name (LA)']}


@mark.parametrize(**ddt_for_location_search)
def test_main_search_by_destination(padi_desktop_app, location, url, h1):
    padi_desktop_app.home_page.visit()
    padi_desktop_app.home_page.main_search(location)
    assert padi_desktop_app.list_page.check_url() == url
    assert padi_desktop_app.details_page.title.text_custom() == h1


@mark.parametrize(**ddt_for_shop_search)
def test_main_search_by_shop_name(padi_desktop_app, shop_name, url, h1):
    padi_desktop_app.home_page.visit()
    padi_desktop_app.home_page.main_search(shop_name)
    assert padi_desktop_app.details_page.check_url() == url
    assert padi_desktop_app.details_page.title.text_custom() == h1


@allure.title('DC-T109: test sign in')
def test_sign_in(padi_desktop_app):
    email = 'mykhailo.khranovskyi@djangostars.com'
    password = 'Aa1122334!'
    initial_url = 'https://travel.padi.comingsoon.rocks/'
    padi_desktop_app.home_page.visit()
    padi_desktop_app.home_page.sign_in(email, password)
    assert padi_desktop_app.home_page.check_url() == initial_url
    assert padi_desktop_app.home_page.check_account_icon_displayed()

