# Playwright automation with python
Test project for test automation for PADI Travel

Tools:
- Playwright (test automation tool)
- Pytest (test runner)
- PyCharm (IDE)
- Allure (reporter)

## Install guide
1. Install python
2. Install PyCharm
3. Install python dependencies `pip install -r requirements.txt`
4. Make sure playwright version 1.8+ installed

## Project structure
- conftest.py file contains main fixtures to work
- Page objects stored in page_object folder
- Tests stored in tests folder
– Settings are spread between:
  - pytest.ini
  - settings.py

## Run guide
- Run tests: `pytest`
- Generate allure report: `allure serve ./report/ --port 3060`
- Clean allure report: `allure generate --clean --output ./report/`

## Useful links
- [Playwright python docs](https://playwright.dev/python/)
- [Udemy Course](https://www.udemy.com/course/test-automation-with-playwright-and-python/)
- [Youtube Course](https://www.youtube.com/playlist?list=PLGE9K4YL_ywj4F7cSA4oDptnqTmyS7hZp)
- [GitHub MS Playwright](https://github.com/microsoft/playwright-python)
- [Allure docs](https://docs.qameta.io/allure/)



