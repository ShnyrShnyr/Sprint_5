from selenium.webdriver.common.by import By

class RegLocators: # страница регистрации
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/../input" # поле ввода Имени
    EMAIL_FIELD = By.XPATH, "//fieldset[2]/div/div/input" # поле ввода email
    PASS_FIELD = By.XPATH, "//fieldset[3]/div/div/input" # поле ввода пароля
    REG_BUTTON = By.XPATH, "//form/button" # кнопка Зарегистрироваться
    ENTER_TEXT = By.XPATH, "//p/a" # кнопка Войти

class SignInLocators: # страница авторизации
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/../input" # поле ввода email
    PASS_FIELD = By.XPATH, "//fieldset[2]/div/div/input"  # поле ввода пароля
    WRONG_PASS = By.XPATH,"//fieldset/div/p" # сообщение о неверном пароле
    COME_IN_BUTTON = By.XPATH, "//form/button" # кнопка Войти
    ENTRANCE_HEADER = By.XPATH, "//main/div/h2" # заголовок вход
    REG_TEXT = By.XPATH, "//form/button"  # текстовая ссылка Зарегистрироваться

class MainPageLocators: # главная страница
    ENTER_BUTTON = By. XPATH, "//nav/a" # кнопка войти в аккаунт
    ORDER_BUTTON = By.XPATH, "//main/section/div/button" # кнопка оформить заказ
    CONSTRUCTOR_BUTTON = By.XPATH, "//li[1]/a"  # кнопка конструктор
    HEADER_OF_CONSTRATOR = By.XPATH, "//h1" # заголовок Соберите бургер
    LOGO = By.XPATH, "//div/a" # логотип в хедерах
    BUNS_TEXT = By.XPATH, "//section/div/h2[1]" # текст булки
    SAUSES_TEXT = By.XPATH, "//section/div/h2[2]"  # текст Соусы
    FILLINGS_TEXT = By.XPATH, "//section/div/h2[3]"  # текст Начинки
    BUNS_MENU = By.XPATH, "//main/section[1]/div[1]/div[1]" # заголовок булки
    SAUSES_MENU = By.XPATH, "//main/section[1]/div[1]/div[2]" # заголовок соусы
    FILLINGS_MENU = By.XPATH, "//main/section[1]/div[1]/div[3]" # заголовок начинки


class PersonalAccount:
    EXIT_TEXT = By.XPATH, "//button[text()='Выход']" # текстовая ссылка Выход
