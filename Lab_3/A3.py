max = 10000  # Счётчик от 0 до 9999
previous = int(input("Предыдущее: "))
current = int(input("Текущее: "))
used = float
if current >= previous:
    used = current - previous
else:
    used = (max - previous) + current
    # Расчёт стоимости
if used <= 300:
    cost = 21.00
elif used <= 600:
    cost = 21.00 + (used - 300) * 0.06
elif used <= 800:
    cost = 21.00 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21.00 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
avg_price = cost / used
print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"    {previous}      {current}        {used}      {cost:.2f}      {avg_price:.2f}")