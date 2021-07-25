import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_failed_authorization_message(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_name("username").send_keys("tomsmith")
    driver.find_element_by_name("password").send_keys("SuperSecretPassword")
    driver.find_element_by_css_selector(".fa.fa-2x.fa-sign-in").click()
    driver.find_element_by_xpath("//div[@id='flash']")
