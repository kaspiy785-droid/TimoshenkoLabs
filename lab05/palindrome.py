text = input("Введите текст: ")

clean_text = text.lower().replace(" ", "")

if clean_text == "":
    print("нет текста")
else:
    if clean_text == clean_text[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")

print("\n--- Дополнительное задание (Без обратного среза) ---")
is_palindrome = True
n = len(clean_text)

if clean_text == "":
    is_palindrome = False
else:
    for i in range(n // 2):
        if clean_text[i] != clean_text[n - 1 - i]:
            is_palindrome = False
            break

if is_palindrome:
    print("Палиндром")
else:
    print("Не палиндром")
