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

    HEADER_OF_CONSTRATOR = By.XPATH, "//h1" # заголовок Соберите бургер
    LOGO = By.XPATH, "//div/a" # логотип в хедерах
    BUNS_TAB = By.XPATH, "//span[text()='Булки']/.."  # таб булки
    SOUSES_TAB = By.XPATH, "//span[text()='Соусы']/.."  # таб соусы
    FILLINGS_TAB = By.XPATH, "//span[text()='Начинки']/.."  # таб начинки
    BUNS_MENU = By.XPATH, "//span[text()='Булки']" # заголовок булки
    SOUSES_MENU = By.XPATH, "//span[text()='Соусы']" # заголовок соусы
    FILLINGS_MENU = By.XPATH, "//span[text()='Начинки']" # заголовок начинки
    BUNS_TEXT = By.XPATH, "//h2[text()='Булки']"  # текст булки
    SOUSES_TEXT = By.XPATH, "//h2[text()='Соусы']"  # текст Соусы
    FILLINGS_TEXT = By.XPATH, "//h2[text()='Начинки']"  # текст Начинки


class PersonalAccount:
    EXIT_TEXT = By.XPATH, "//button[text()='Выход']" # текстовая ссылка Выход
