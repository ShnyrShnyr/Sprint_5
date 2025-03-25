from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.data import Data
from src.helpers import get_sign_up_data
from src.locators import SignInLocators, RegLocators
login, password = get_sign_up_data()

class TestRegistration:
    def test_success_reg(self):
        driver = webdriver.Chrome()
        driver.get(f'{Config.URL}/register')

        # Успешная регистрация
        driver.find_element(*RegLocators.NAME_FIELD).send_keys(Data.NAME) # найти поле имя и заполнить
        driver.find_element(*RegLocators.EMAIL_FIELD).send_keys(login) # найти поле email и заполнить
        driver.find_element(*RegLocators.PASS_FIELD).send_keys(password) # найти поле пароль и заполнить
        driver.find_element(*RegLocators.REG_BUTTON).click() # нажать кнопку зарегистрироваться
        email = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки страницы авторизации c введенным логином
        assert email.get_attribute("value") == login, "Failed success registration"  # проверяем, что значение поля value наша сгенерированная почта
        driver.quit()

        # Некорректный пароль при регистрации
    def test_fail_registration(self):
        driver = webdriver.Chrome()
        driver.get(f'{Config.URL}/register')
        driver.find_element(*RegLocators.NAME_FIELD).send_keys(Data.NAME) # найти поле имя и заполнить
        driver.find_element(*RegLocators.EMAIL_FIELD).send_keys(login) # найти поле email и заполнить
        driver.find_element(*RegLocators.PASS_FIELD).send_keys(Data.WRONG_PASS) # найти поле пароль и заполнить
        driver.find_element(*RegLocators.REG_BUTTON).click() # нажать кнопку зарегистрироваться
        email = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.WRONG_PASS))  # ждем появления надписи "Некорректный пароль"
        assert email.text == "Некорректный пароль", "Failed wrong registration"  # проверяем, что появилась надпись "Некорректный пароль"
        driver.quit()