from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import registration
from src.config import Config
from src.data import get_sign_up_data
from src.locators import RegLocators, SignInLocators, MainPageLocators

driver = webdriver.Chrome()
driver.get(Config.URL)

driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()  # ищем кнопку "Личный кабинет" и кликаем на нее
WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(RegLocators.REG_TEXT))  # ждем загрузки элемента регистрация на странице
driver.find_element(*RegLocators.REG_TEXT).click()  # кликаем на зарегистрироваться
WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(RegLocators.REG_BUTTON))  # ждем загрузки кнопки "Зарегистрироваться" на странице

# Успешная регистрация
registration(get_sign_up_data.good_pass, driver)
WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(SignInLocators.EMAIL_FIELD))  # ждем загрузки страницы авторизации c введенным логином
assert (driver.find_element(*SignInLocators.EMAIL_FIELD).get_attribute("value") == get_sign_up_data.login), "Error at login"  # проверяем, что значение поля value наша сгенерированная почта
driver.quit()

# Некорректный пароль при регистрации
registration(get_sign_up_data.wrong_pass, driver)
WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(SignInLocators.WRONG_PASS))  # ждем появления надписи "Некорректный пароль"
assert (driver.find_element(*SignInLocators.WRONG_PASS).text == "Некорректный пароль"), "Error at password"  # проверяем, что появилась надпись "Некорректный пароль"

driver.quit()