charge = int(input("Введите заряд (от 0 до 100): "))

if charge < 0 or charge > 100:
    print("Ошибка диапазона")
elif 0 <= charge <= 19:
    print("Низкий")
elif 20 <= charge <= 79:
    print("Средний")
else:
    print("Высокий")

print("\n--- Дополнительное задание ---")
year = int(input("Введите год (от 1 до 9999): "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("да")
else:
    print("нет")
