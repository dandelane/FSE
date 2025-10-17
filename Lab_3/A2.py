import string
# Ввод пароля
password = input("Введите пароль: ")
# Допустимые символы
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
# Список ошибок
errors = []
# Проверка длины
if len(password) != 8:
    errors.append("Длина пароля не равна 8")
# Проверка наличия заглавных букв
if password == password.lower():
    errors.append("В пароле отсутствуют заглавные буквы")
# Проверка наличия строчных букв
if password == password.upper():
    errors.append("В пароле отсутствуют строчные буквы")
# Проверка наличия цифр
if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")
# Проверка наличия специальных символов
if not any(symbol in "*-#" for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")
# Проверка на недопустимые символы
if not all(symbol in allowed for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")
# Вывод результата
if not errors:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)