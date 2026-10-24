text = input("Введите текст: ")

old_len = len(text)
words = text.split()
normalized_text = " ".join(words)
new_len = len(normalized_text)
word_count = len(words)

print("Исходная длина:", old_len)
print("Новая длина:", new_len)
print("Нормализованный текст:", normalized_text)
print("Количество слов:", word_count)
