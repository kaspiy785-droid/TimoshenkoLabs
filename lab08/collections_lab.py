def word_counts(text):
    counts = {}
    for raw_word in text.split():
        word = raw_word.strip(".,!?:;").lower()
        if word != "":
            counts[word] = counts.get(word, 0) + 1
    return counts

def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")

def common_topics(first, second):
    return sorted(set(first) & set(second))

def all_topics(first, second):
    return sorted(set(first) | set(second))

def record_and_pair_demo():
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6
    record["completed"] = False
    pair = (record["title"], record["hours"])
    title, hours = pair
    print(title, hours)

def totals_by_category(records):
    totals = {}
    for item in records:
        cat = item["category"]
        totals[cat] = totals.get(cat, 0) + item["amount"]
    return totals

def titles_in_category(records, category):
    titles = []
    for item in records:
        if item["category"] == category:
            titles.append(item["title"])
    return titles

def sorted_category_totals(records):
    totals = totals_by_category(records)
    return sorted(totals.items(), key=lambda x: (-x[1], x[0]))

if __name__ == "__main__":
    text = input("Введите текст: ")
    counts = word_counts(text)
    print_word_counts(counts)

    record_and_pair_demo()

    study_records = [
        {"title": "Лекция по Python", "category": "теория", "amount": 2},
        {"title": "Лабораторная работа 8", "category": "практика", "amount": 4},
        {"title": "Чтение документации", "category": "самоподготовка", "amount": 3},
        {"title": "Практикум по словарям", "category": "практика", "amount": 2},
        {"title": "Семинар по структурам", "category": "теория", "amount": 2},
    ]

    totals = totals_by_category(study_records)
    for cat in sorted(totals):
        print(f"{cat}: {totals[cat]}")

    search_cat = input("Введите категорию для поиска: ")
    print(titles_in_category(study_records, search_cat))
    print(sorted_category_totals(study_records))
