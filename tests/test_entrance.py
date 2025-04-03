from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.data import Data
from src.config import Config
from src.locators import RegLocators, SignInLocators, MainPageLocators
from tests.conftest import driver


class TestEntrance:

    def test_entrance_from_main_page(self, driver):
        driver.find_element(*MainPageLocators.ENTER_BUTTON).click() # найти элемент Войти в аккаунт и кликнуть
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки элемента с введенными данными в email на странице
        driver.find_element(*SignInLocators.EMAIL_FIELD).send_keys(Data.LOGIN) # ввести email
        driver.find_element(*SignInLocators.PASS_FIELD).send_keys(Data.PASSWORD) # ввести пароль
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() #найти элемент Войти и кликнуть
        enter = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert enter.text == "Оформить заказ", "No entrance from Войти в аккаунт"

    def test_entrance_from_account_page(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки элемента с введенными данными в email на странице
        driver.find_element(*SignInLocators.EMAIL_FIELD).send_keys(Data.LOGIN)  # ввести email
        driver.find_element(*SignInLocators.PASS_FIELD).send_keys(Data.PASSWORD)  # ввести пароль
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() #найти элемент Войти и кликнуть
        enter = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert enter.text == "Оформить заказ", "No entrance from Войти в аккаунт"

    def test_entrance_from_reg_page(self, driver):
        driver.get(f'{Config.URL}/register') # зайти на страницу регистрация
        driver.find_element(*RegLocators.ENTER_TEXT).click() # найти Войти и кликнуть
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки элемента с введенными данными в email на странице
        driver.find_element(*SignInLocators.EMAIL_FIELD).send_keys(Data.LOGIN)  # ввести email
        driver.find_element(*SignInLocators.PASS_FIELD).send_keys(Data.PASSWORD)  # ввести пароль
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() #найти элемент Войти и кликнуть
        assert WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed(), "No entrance from Войти из регистрации"

    def test_entrance_from_forgot_pass(self,driver):
        driver.get(f'{Config.URL}/forgot-password') # зайти на страницу забыли пароль
        driver.find_element(*RegLocators.ENTER_TEXT).click() # найти Войти и кликнуть
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки элемента с введенными данными в email на странице
        driver.find_element(*SignInLocators.EMAIL_FIELD).send_keys(Data.LOGIN)  # ввести email
        driver.find_element(*SignInLocators.PASS_FIELD).send_keys(Data.PASSWORD)  # ввести пароль
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() #найти элемент Войти и кликнуть
        assert WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed(), "No entrance from Забыли пароль"
