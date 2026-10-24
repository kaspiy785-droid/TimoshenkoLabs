text = input("Введите строку: ")

words = text.split()
valid_count = 0

for word in words:
    clean_word = word.strip(".,!?:;-").lower()
    if clean_word != "":
        if clean_word.startswith("a") or clean_word.startswith("а"):
            print(clean_word)
            valid_count += 1

if valid_count == 0:
    print("Нет совпадений")

print("Количество:", valid_count)
