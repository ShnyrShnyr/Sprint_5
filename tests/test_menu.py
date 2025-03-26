from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.locators import MainPageLocators


class TestMenu:
    def test_menu_scroll_buns(self, driver):
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*MainPageLocators.BUNS_MENU)
        buns = WebDriverWait(driver,Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.BUNS_TEXT))
        driver.execute_script("arguments[0].scrollIntoView();", buns)
        assert "Failed BUNS click"

    def test_menu_scroll_souses(self, driver):
        driver.find_element(*MainPageLocators.SOUSES_MENU).click()
        souses = WebDriverWait(driver,Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.SOUSES_TEXT))
        driver.execute_script("arguments[0].scrollIntoView();", souses)
        assert "Failed SOUSES click"

    def test_menu_scroll_fillings(self, driver):
        driver.find_element(*MainPageLocators.FILLINGS_MENU).click()
        fillings = WebDriverWait(driver,Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.FILLINGS_TEXT))
        driver.execute_script("arguments[0].scrollIntoView();", fillings)
        assert "Failed FILLINGS click"
