from selenium.webdriver.common.by import By

class RegLocators: # страница регистрации
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/../input" # поле ввода Имени
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/../input" # поле ввода email
    PASS_FIELD = By.XPATH, "//label[text()='Пароль']/../input" # поле ввода пароля
    REG_BUTTON = By.XPATH, "//*[text()='Зарегистрироваться']" # кнопка Зарегистрироваться
    ENTER_TEXT = By.XPATH, "//*[text()='Войти']" # текст Войти

class SignInLocators: # страница авторизации
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/../input" # поле ввода email
    PASS_FIELD = By.XPATH, "//label[text()='Пароль']/../input"  # поле ввода пароля
    WRONG_PASS = By.XPATH,"//*[text()='Некорректный пароль']" # сообщение о неверном пароле
    COME_IN_BUTTON = By.XPATH, "//*[text()='Войти']" # кнопка Войти
    ENTRANCE_HEADER = By.XPATH, "//*[text()='Вход']" # заголовок вход
    REG_TEXT = By.XPATH, "//*[text()='Зарегистрироваться']"  # текстовая ссылка Зарегистрироваться

class MainPageLocators: # главная страница
    PERSONAL_ACCOUNT = By.XPATH, "//*[text()='Личный Кабинет']" # кнопка личный кабинет
    ENTER_BUTTON = By.XPATH, "//*[text()='Войти в аккаунт']"  # кнопка войти в аккаунт
    ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"  # кнопка оформить заказ
    CONSTRUCTOR_BUTTON = By.XPATH, "//a[.//p[text()='Конструктор']]"  # кнопка конструктор
    HEADER_OF_CONSTRATOR = By.XPATH, "//*[text()='Соберите бургер']" # заголовок Соберите бургер
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
