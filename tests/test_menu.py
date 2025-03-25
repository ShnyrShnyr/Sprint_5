from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.locators import MainPageLocators


class TestMenu:
    def test_menu(self, driver):
        driver.find_element(*MainPageLocators.BUNS_TEXT).click()
        buns = WebDriverWait(driver,Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.BUNS_MENU))
        driver.find_element(*MainPageLocators.SAUSES_TEXT).click()
        sauses = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.SAUSES_MENU))
        driver.find_element(*MainPageLocators.FILLINGS_TEXT).click()
        fillings = WebDriverWait(driver,Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.FILLINGS_MENU))
        assert buns.is_displayed(), "Failed BULKI click"
        assert sauses.is_displayed(), "Failed SOUSES click"
        assert fillings.is_displayed(), "Failed NACHINKI click"

