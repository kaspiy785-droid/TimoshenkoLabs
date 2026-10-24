def sum_digits(number):
    n = abs(number)
    if n == 0:
        return 0
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    words = text.split()
    return " ".join(words).lower()

def select_numbers(numbers, threshold):
    result = []
    for x in numbers:
        if x > threshold:
            result.append(x)
    return result

def is_palindrome(text):
    clean = "".join(text.split()).lower()
    if clean == "":
        return False
    return clean == clean[::-1]
