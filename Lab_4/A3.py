packets = input("Введите последовательность из 0 и 1: ")
if len(packets) < 5:
    print("Ошибка, длина строки должна быть не менее 5 символов")
elif not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    total_packets = len(packets)
    lost_packets = packets.count("0")
    max_streak = 0
    current_streak = 0
    for packet in packets:
        if packet == "0":
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0
    lost_percent = (lost_packets / total_packets) * 100
    if lost_percent <= 1:
        quality = "отличное"
    elif lost_percent <= 5:
        quality = "хорошее"
    elif lost_percent <= 10:
        quality = "удовлетворительное"
    elif lost_percent <= 20:
        quality = "плохое"
    else:
        quality = "критическое состояние сети"
    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_streak}")
    print(f"Процент потерь: {lost_percent:.1f}%")
    print(f"Качество связи: {quality}")
