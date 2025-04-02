from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.locators import MainPageLocators


class TestMenu:

    def test_menu_souses(self, driver):
        driver.find_element(*MainPageLocators.SOUSES_MENU).click() #кликаю по тексту "Соусы" на табе
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.SOUSES_TEXT)) #жду, когда будет виден текст соусы в самом меню
        element = driver.find_element(*MainPageLocators.SOUSES_TAB) #ищу и опледеляю переменную элемент по слову "Соусы", поднимаясь в дом на 1 уровень вверх
        class_value = element.get_attribute("class") # сохраняю в переменную значение class
        assert 'current' in class_value, "Failed SOUSES click" #проверяю, что в этом значении есть current

    def test_menu_fillings(self, driver):
        driver.find_element(*MainPageLocators.FILLINGS_MENU).click()
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.FILLINGS_TEXT))
        element = driver.find_element(*MainPageLocators.FILLINGS_TAB)
        class_value = element.get_attribute("class")
        assert 'current' in class_value, "Failed FILLINGS click"

    def test_menu_buns(self, driver):
        driver.find_element(*MainPageLocators.FILLINGS_MENU).click()
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.FILLINGS_TEXT))
        driver.find_element(*MainPageLocators.BUNS_MENU).click()
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.BUNS_TEXT))
        element = driver.find_element(*MainPageLocators.BUNS_TAB)
        class_value = element.get_attribute("class")
        assert 'current' in class_value, "Failed BUNS click"
