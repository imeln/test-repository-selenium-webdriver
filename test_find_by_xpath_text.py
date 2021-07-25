import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_find_by_xpath_text(driver):
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element_by_xpath("//h2[normalize-space()='Available Examples']")
