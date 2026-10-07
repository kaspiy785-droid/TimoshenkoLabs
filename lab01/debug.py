print("Фрагмент А")
first = "2"
second = "3"
print("Тип до:", type(first), type(second))
result_a = int(first) + int(second)
print("Тип после:", type(result_a))
print("Результат:", result_a)

print("Фрагмент Б")
age_input = input("Возраст: ")
print("Тип до: <class 'str'>")
age = int(age_input)
print("Тип после:", type(age))
print("Результат:", age - 1)

print("Фрагмент В")
first_num = 4
second_num = 7
third_num = 10
print("Тип до:", type(first_num), type(second_num), type(third_num))
average = (first_num + second_num + third_num) / 3
print("Тип после:", type(average))
print("Результат:", f"{average:.1f}")
