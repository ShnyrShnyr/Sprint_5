import pytest
from selenium import webdriver
from src.config import Config
from src.locators import RegLocators
from src.data import get_sign_up_data

def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    width, height = Config.RESOLUTION
    chrome_options.add_argument(f'--window-size={width}, {height}')
    return chrome_options

@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get (Config.URL)
    yield chrome
    chrome.quit()

@pytest.fixture
def registration(password, driver):
    driver.find_element(RegLocators.NAME_FIELD).send_keys('Андрей')
    driver.find_element(RegLocators.EMAIL_FIELD).send_keys(get_sign_up_data.login)
    driver.find_element(RegLocators.PASS_FIELD).send_keys(password)
    driver.find_element(RegLocators.REG_BUTTON).click()
