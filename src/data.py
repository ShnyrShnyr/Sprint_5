# функция генерирует креды для регистрации и сохраняет их в переменные
'''import string


class RegCreds:

    characters = string.ascii_letters + string.digits + string.punctuation
    good_pass = ''.join(random.choice(characters) for _ in range(6))
    wrong_pass = ''.join(random.choice(characters) for _ in range(5))'''
import faker
import random

def get_sign_up_data():
    fake = faker.Faker()
    login = f'AndreyShnyrin19{random.randint(100, 999)}@yandex.ru'
    good_pass = fake.password(length=6)
    wrong_pass = fake.password(length=5)
    return
