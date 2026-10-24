text = input("Введите текст: ")

replacements_count = text.count(":")
new_text = text.replace(":", "-")

print("Количество замен:", replacements_count)
print("Новая строка:", new_text)
