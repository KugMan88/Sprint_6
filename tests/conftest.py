import pytest
from selenium import webdriver
from urls import URLS


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(URLS.BASE_URL)

    yield browser
    browser.quit()