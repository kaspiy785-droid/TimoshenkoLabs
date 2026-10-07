first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print("Исходные названия:", first_room, "и", second_room)

temp = first_room
first_room = second_room
second_room = temp

print("После изменения:", first_room, "и", second_room)
