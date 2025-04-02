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




class PersonalAccount:
    EXIT_TEXT = By.XPATH, "//button[text()='Выход']" # текстовая ссылка Выход
