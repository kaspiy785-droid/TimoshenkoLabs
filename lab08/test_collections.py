from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
    sorted_category_totals,
)

assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}

t1 = ["python", "sql", "python"]
t2 = ["sql", "git"]
assert common_topics(t1, t2) == ["sql"]
assert all_topics(t1, t2) == ["git", "python", "sql"]
assert common_topics([], t2) == []
assert all_topics([], t2) == ["git", "sql"]

records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
records_copy = [r.copy() for r in records]

assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert totals_by_category([]) == {}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert sorted_category_totals(records) == [("основное", 7), ("дополнительное", 2)]
assert records == records_copy

study_records = [
    {"title": "Лекция по Python", "category": "теория", "amount": 2},
    {"title": "Лабораторная работа 8", "category": "практика", "amount": 4},
    {"title": "Чтение документации", "category": "самоподготовка", "amount": 3},
    {"title": "Практикум по словарям", "category": "практика", "amount": 2},
    {"title": "Семинар по структурам", "category": "теория", "amount": 2},
]
assert totals_by_category(study_records) == {"теория": 4, "практика": 6, "самоподготовка": 3}
assert titles_in_category(study_records, "теория") == ["Лекция по Python", "Семинар по структурам"]

print("Все проверки успешно пройдены")
