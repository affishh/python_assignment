import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without UI
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_home_page(driver):
    # Make sure your Flask app is running on localhost:5000
    driver.get("http://127.0.0.1:5000/")
    time.sleep(1)
    header = driver.find_element(By.TAG_NAME, "h1")
    assert header.text == "Welcome to the Sample App"
