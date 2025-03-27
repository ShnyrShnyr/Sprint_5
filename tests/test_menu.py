from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.locators import MainPageLocators


class TestMenu:
    def test_menu_buns(self, driver):
        if driver.find_element(*MainPageLocators.BUNS_MENU):
            element = WebDriverWait(driver,Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.CHANGED_MENU))
            class_value = element.get_attribute("class")
        assert 'current' in class_value, "Failed BUNS click"

    def test_menu_souses(self, driver):
        driver.find_element(*MainPageLocators.SOUSES_MENU).click()
        element = WebDriverWait(driver,Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.CHANGED_MENU))
        class_value = element.get_attribute("class")
        assert 'current' in class_value, "Failed SOUSES click"

    def test_menu_fillings(self, driver):
        driver.find_element(*MainPageLocators.FILLINGS_MENU).click()
        element = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.CHANGED_MENU))
        class_value = element.get_attribute("class")
        assert 'current' in class_value, "Failed FILLINGS click"
