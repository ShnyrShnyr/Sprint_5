from selenium.webdriver.common.by import By

class RegLocators: # страница регистрации
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/../input" # поле ввода Имени
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/../input" # поле ввода email
    PASS_FIELD = By.XPATH, "//label[text()='Пароль']/../input" # поле ввода пароля
    REG_BUTTON = By.XPATH, "//form/button" # кнопка Зарегистрироваться
    ENTER_TEXT = By.XPATH, "//p/a" # кнопка Войти

class SignInLocators: # страница авторизации
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/../input" # поле ввода email
    PASS_FIELD = By.XPATH, "//label[text()='Пароль']/../input"  # поле ввода пароля
    WRONG_PASS = By.XPATH,"//fieldset/div/p" # сообщение о неверном пароле
    COME_IN_BUTTON = By.XPATH, "//form/button" # кнопка Войти
    ENTRANCE_HEADER = By.XPATH, "//main/div/h2" # заголовок вход
    REG_TEXT = By.XPATH, "//form/button"  # текстовая ссылка Зарегистрироваться

class MainPageLocators: # главная страница
    ENTER_BUTTON = By. XPATH, "//nav/a" # кнопка войти в аккаунт
    ORDER_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']" # кнопка оформить заказ
    CONSTRUCTOR_BUTTON = By.XPATH, "//a[.//p[text()='Конструктор']]"  # кнопка конструктор
    HEADER_OF_CONSTRATOR = By.XPATH, "//h1" # заголовок Соберите бургер
    LOGO = By.XPATH, "//div/a" # логотип в хедерах
    BUNS_TEXT = By.XPATH, "//h2[text()='Булки']" # текст булки
    SOUSES_TEXT = By.XPATH, "//h2[text()='Соусы']"  # текст Соусы
    FILLINGS_TEXT = By.XPATH, "//h2[text()='Начинки']"  # текст Начинки
    BUNS_MENU = By.XPATH, "//div[contains(@class, 'current')]" # заголовок булки кликабельный выбранный
    SOUSES_MENU = By.XPATH, "//span[text()='Соусы']" # заголовок соусы кликабельный
    FILLINGS_MENU = By.XPATH, "//span[text()='Начинки']" # заголовок начинки кликабельный


class PersonalAccount:
    EXIT_TEXT = By.XPATH, "//button[text()='Выход']" # текстовая ссылка Выход
