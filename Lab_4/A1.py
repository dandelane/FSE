import random
import time
N = int(input("Введите количество примеров: "))
nomer = int()
all_time = int()
correct_answer = int()
pravilny_otvet = int()
for i in range(N):
    nomer += 1
    print(f"Вопрос {nomer}/{N}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_answer = a * b
    while True:
        try:
            start_time = time.time()
            answer = int(input(f"{a} × {b} = "))
            time_spend = time.time() - start_time
            all_time += time_spend
            if answer == correct_answer:
                print(f"Верно! (Время: {time_spend:.1f} сек)")
                pravilny_otvet += 1
                break
            else:
                print(f"Неверно! Правильно: {correct_answer} (Время: {time_spend:.1f} сек) ")
                break
        except ValueError:
            print("Пожалуйста, введите целое число!")
sr_time = all_time / N
procent_pravilny_otvet = int()
procent_pravilny_otvet = (pravilny_otvet / N) * 100
print("==================================================")
print("СТАТИСТИКА:")
print("==================================================")
print(f"Общее время: {all_time:.1f} секунд")
print(f"Среднее время на вопрос: {sr_time:.1f} сек")
print(f"Правильных ответов:{pravilny_otvet}/{N} ")
print(f"Процент правильных: {procent_pravilny_otvet:.1f}%")