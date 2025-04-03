
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.locators import SignInLocators, MainPageLocators

class TestPersonalAccount:

    def test_lk(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click() # найти кнопку личный кабинет и кликнуть
        text_profile = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.ENTRANCE_HEADER)) # подождать появления поля email
        assert text_profile.is_displayed(), "input_email not displayed"

    def test_constractor(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()  # найти кнопку личный кабинет и кликнуть
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.ENTRANCE_HEADER))  # подождать появления текста профиль
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click() # найти кнопку конструктор и кликнуть
        header_text = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.HEADER_OF_CONSTRATOR)) # подождать пока появится надпись соберите бургер
        assert header_text.is_displayed(), "Entrance at constractor is failed"


    def test_logo(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.ENTRANCE_HEADER))  # подождать появления текста профиль
        driver.find_element(*MainPageLocators.LOGO).click()
        header_text = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.HEADER_OF_CONSTRATOR))  # подождать пока появится надпись соберите бургер
        assert header_text.is_displayed(), "Entrance at logo is failed"


