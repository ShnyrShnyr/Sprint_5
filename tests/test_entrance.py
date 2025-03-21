from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.locators import RegLocators, SignInLocators, MainPageLocators

class TestEntrance:
    def test_enter(self):
        driver = webdriver.Chrome()
        driver.get(Config.URL)

        driver.find_element(*MainPageLocators.ENTER_BUTTON).click() # найти элемент Войти в аккаунт и кликнуть
        WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки элемента с введенными данными в email на странице
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() #найти элемент Войти и кликнуть
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed(), "No entrance from Войти в аккаунт"

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки элемента с введенными данными в email на странице
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() #найти элемент Войти и кликнуть
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed(), "No entrance from Личный кабинет"

        driver.get(f'{Config.URL}/register') # зайти на страницу регистрация
        driver.find_element(*RegLocators.ENT_TEXT).click() # найти Войти и кликнуть
        WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки элемента с введенными данными в email на странице
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() #найти элемент Войти и кликнуть
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed(), "No entrance from Войти из регистрации"

        driver.get(f'{Config.URL}/forgot-password') # зайти на страницу забыли пароль
        driver.find_element(*RegLocators.ENT_TEXT).click() # найти Войти и кликнуть
        WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки элемента с введенными данными в email на странице
        driver.find_element(*SignInLocators.COME_IN_BUTTON).click() #найти элемент Войти и кликнуть
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed(), "No entrance from Забыли пароль"

        driver.quit()
