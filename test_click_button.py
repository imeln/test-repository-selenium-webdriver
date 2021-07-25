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


def test_click_button(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    link = driver.find_element_by_css_selector("button[onclick='addElement()']")
    link.click()
    WebDriverWait(driver, 10)
    driver.find_element_by_class_name("added-manually")
