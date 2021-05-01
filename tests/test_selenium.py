import pytest

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.skip()
def test_test():
    with webdriver.Firefox() as driver:
        driver.get("https://google.com/")

        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("naruto")
        search_field.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_changes)
        page = BeautifulSoup(driver.page_source)

        links = page.find_all(name="a")

        link = links[0]

        print(link)
