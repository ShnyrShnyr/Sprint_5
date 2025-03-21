# функция генерирует креды для регистрации и сохраняет их в переменные
import faker
import random

def get_sign_up_data():
    fake = faker.Faker()
    login = f'AndreyShnyrin19{random.randint(100, 999)}@yandex.ru'
    good_pass = fake.password(length=6)
    wrong_pass = fake.password(length=5)
    return login, good_pass, wrong_pass
