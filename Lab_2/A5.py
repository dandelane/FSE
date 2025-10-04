a = int(input('Enter 1st number: '))    # Вводим первое число
b = int(input('Enter 2nd number: '))    # Вводим второе число
result = ["NO", "YES"][a % b == 0]  # NO - не делится число A  нацело на число B, YES - делится
print(result)