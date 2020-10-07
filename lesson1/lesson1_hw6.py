# задание 6
a = input("Сколько км спортсмен пробежал в первый день: ")
b = input("Результат не менее: ")

a = float(a)
b = int(b)

percent = 0.1
day = 1

while a < b:
    day += 1
    a += a * percent

print(f"На {day}-й день спортсмен достиг результата — не менее {b} км")
