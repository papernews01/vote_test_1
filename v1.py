import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Введите длину пароля: "))
if length < 8:
    print("Пароль должен быть минимум 8 символов!")
else:
    print("Ваш пароль:", generate_password(length))