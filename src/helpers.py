# функция генерирует креды для регистрации и сохраняет их в переменные
import faker
import random

def get_sign_up_data():
    fake = faker.Faker()
    login = f'AndreyShnyrin19{random.randint(100, 999)}@yandex.ru'
    password = fake.password(length=6)
    return login, password
