def test_location_ok(mobile_app_auth):
    location = mobile_app_auth.get_location()
    assert '000:000' == location
