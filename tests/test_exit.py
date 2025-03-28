from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.data import Data
from src.config import Config
from src.locators import PersonalAccount, SignInLocators, MainPageLocators

class TestExit:
    def test_exit(self, driver):
        driver.find_element(*MainPageLocators.ENTER_BUTTON).click() # на главной странице входим в личный кабинет
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.EMAIL_FIELD)).send_keys(Data.LOGIN) #ждем поле email и вводим его
        driver.find_element(*SignInLocators.PASS_FIELD).send_keys(Data.PASSWORD) # ищем элемент пароль и вводим его
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() # ищем кнопку войти и нажимаем
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.ENTER_BUTTON)).click() # ждем загрузки кнопки Личный кабинет на главной странице и нажимаем на него.
        WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(PersonalAccount.EXIT_TEXT)).click() # ждем загрузки кнопки выйти в личном кабинете и нажимаем на нее
        text_entrance = WebDriverWait(driver, Config.TIMEOUT).until(ec.visibility_of_element_located(SignInLocators.ENTRANCE_HEADER)) # ждем заголовок окна авторизации Вход
        assert text_entrance.text == 'Вход' , "Failed in exit at personal account" # проверяем заголовок

