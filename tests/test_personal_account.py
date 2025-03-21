from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.locators import SignInLocators, MainPageLocators

class TestPersonalAccount:

    def test_lk(self, driver):
        driver = webdriver.Chrome()
        driver.get(Config.URL)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click() # найти кнопку личный кабинет и кликнуть
        input_email = WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(SignInLocators.EMAIL_FIELD)) # подождать появления поля email
        assert input_email.is_displayed(), "input_email not displayed"

    def test_constractor(self, driver):
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click() # найти кнопку конструктор и кликнуть
        header_text = WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(MainPageLocators.HEADER_OF_CONSTRATOR)) # подождать пока появится надпись соберите бургер
        assert header_text.is_displayed(), "Entrance at constractor is failed"
        driver.quit()