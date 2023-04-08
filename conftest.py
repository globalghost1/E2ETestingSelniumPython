import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 


@pytest.fixture(scope="class")

def setup(request):
    driver = webdriver.Chrome(executable_path="/home/parallels/Downloads/chromedriver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close
    

