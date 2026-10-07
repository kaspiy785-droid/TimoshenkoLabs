last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст: "))
subject = input("Введите любимый предмет: ")
hours = float(input("Введите количество часов подготовки в неделю: "))

age_after_4_years = age + 4
hours_total = hours * 4
hours_per_day = hours / 7

print("Карточка студента")
print(first_name, last_name)
print("Возраст через 4 года:", age_after_4_years)
print("Группа:", group)
print("Город:", city)
print("Любимый предмет:", subject)
print("Время подготовки за 4 недели:", f"{hours_total:.2f}")
print("Среднее время в день:", f"{hours_per_day:.2f}")
