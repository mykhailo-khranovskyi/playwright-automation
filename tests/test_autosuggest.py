import pytest


@pytest.mark.parametrize('page_name,item_name,method_name', [
    ('dr_list_page', 'Breathless Cabo San Lucas Resort & Spa', 'search_by_resort_name'),
    ('la_list_page', 'Solomons PNG Master', 'search_by_la_name'),
    ('dc_list_page', 'QA_DC_TEST', 'search_by_dc_name')
])
def test_autosuggest(padi_desktop_app, page_name, item_name, method_name):
    getattr(padi_desktop_app, page_name).visit()
    getattr(getattr(padi_desktop_app, page_name), method_name)(item_name)
    assert getattr(padi_desktop_app, page_name).get_shop_title() == item_name
