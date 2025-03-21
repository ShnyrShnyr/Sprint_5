from selenium.webdriver.common.by import By
from src.data import get_sign_up_data

class RegLocators: # страница регистрации
    NAME_FIELD = By.XPATH, "//label[text()='Имя']" # поле ввода Имени
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']" # поле ввода email
    PASS_FIELD = By.XPATH, "//label[text()='Пароль']" # поле ввода пароля
    REG_TEXT = By.XPATH, "//a[text()='Зарегистрироваться']" # текстовая ссылка Зарегистрироваться
    REG_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']" # кнопка Зарегистрироваться
    ENT_TEXT = By.CLASS_NAME, "Auth_link__1fOlj" # кнопка Войти

class SignInLocators: # страница авторизации
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']" # поле ввода email
    WRONG_PASS = By.CLASS_NAME,"input__error text_type_main-default" # сообщение о неверном пароле
    COME_IN_BUTTON = By.XPATH, "//button[text()='Войти']" # кнопка Войти

class MainPageLocators: # главная страница
    ENTER_BUTTON = By. XPATH, "// button[text() = 'Войти в аккаунт']" # кнопка войти в аккаунт
    ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']" # кнопка оформить заказ
    PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']" # кнопка личный кабинет