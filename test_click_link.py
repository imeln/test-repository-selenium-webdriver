import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_click_link(driver):
    driver.get("https://the-internet.herokuapp.com/")
    link = driver.find_element_by_link_text('A/B Testing')
    link.click()
