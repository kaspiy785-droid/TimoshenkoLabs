import math

total = int(os.environ.get('STUDENTS', 0)) if 'os' in globals() else int(input("Количество студентов: "))
capacity = int(os.environ.get('CAPACITY', 0)) if 'os' in globals() else int(input("Мест в автобусе: "))

full_units = total // capacity
remains = total % capacity
total_units = (total + capacity - 1) // capacity

print("Полных", full_units, ", остаток", remains, ", всего", total_units)

print("\n--- Дополнительное задание (Окружность) ---")
radius = float(input("Введите положительный радиус: "))

length = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print("Длина окружности:", f"{length:.2f}")
print("Площадь круга:", f"{area:.2f}")
