sub1 = input("Название первого предмета: ")
lessons1 = int(input("Количество занятий в неделю: "))
time1 = int(input("Продолжительность одного занятия в минутах: "))

sub2 = input("Название второго предмета: ")
lessons2 = int(input("Количество занятий в неделю: "))
time2 = int(input("Продолжительность одного занятия в минутах: "))

weekly_hours = float(input("Доступное время на неделю в часах: "))

min1 = lessons1 * time1
hours1 = min1 / 60

min2 = lessons2 * time2
hours2 = min2 / 60

total_hours = hours1 + hours2
free_hours = weekly_hours - total_hours
four_weeks_hours = total_hours * 4

print("Нагрузка по предмету", sub1, ":", min1, "минут,", f"{hours1:.2f}", "часов")
print("Нагрузка по предмету", sub2, ":", min2, "минут,", f"{hours2:.2f}", "часов")
print("Остаток свободного времени в неделю:", f"{free_hours:.2f}", "часов")
print("Нагрузка за 4 недели:", f"{four_weeks_hours:.2f}", "часов")
