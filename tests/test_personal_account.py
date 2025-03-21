from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.config import Config
from src.locators import RegLocators, SignInLocators, MainPageLocators

driver = webdriver.Chrome()
driver.get(Config.URL)

driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
WebDriverWait(driver, Config.TIMEOUT).until(EC.visibility_of_element_located(SignInLocators.EMAIL_FIELD))