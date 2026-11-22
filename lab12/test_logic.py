from logic import validate_records, add_record, find_records, set_completed, delete_record, statistics

records = []
assert statistics(records) == {
    "total": 0,
    "completed": 0,
    "uncompleted": 0,
    "total_amount": 0,
    "by_category": {}
}

r1 = add_record(records, "  Python  ", "учёба", 4)
r2 = add_record(records, "Python", "практика", 2)
assert r1["id"] == 1
assert r1["title"] == "Python"
assert r1["completed"] is False
assert r2["id"] == 2

found = find_records(records, "py")
assert len(found) == 2
assert find_records(records, "   ") == []
assert find_records(records, "SQL") == []

assert set_completed(records, 2, True) is True
assert records[1]["completed"] is True
assert set_completed(records, 999, True) is False

stats = statistics(records)
assert stats == {
    "total": 2,
    "completed": 1,
    "uncompleted": 1,
    "total_amount": 6,
    "by_category": {"практика": 2, "учёба": 4}
}

assert delete_record(records, 1) is True
assert delete_record(records, 999) is False
assert len(records) == 1
assert records[0]["id"] == 2

r3 = add_record(records, "Базы данных", "учёба", 3)
assert r3["id"] == 3

bad_cases = [
    {"id": 1},
    [{"id": True, "title": "A", "category": "B", "amount": 1, "completed": False}],
    [{"id": 1, "title": "A", "category": "B", "amount": True, "completed": False}],
    [{"id": 1, "title": "A", "category": "B", "amount": -1, "completed": False}],
    [{"id": 1, "title": "   ", "category": "B", "amount": 1, "completed": False}],
    [
        {"id": 1, "title": "A", "category": "B", "amount": 1, "completed": False},
        {"id": 1, "title": "C", "category": "D", "amount": 2, "completed": True}
    ]
]

for bad in bad_cases:
    try:
        validate_records(bad)
    except ValueError:
        pass
    else:
        assert False, "Ошибка валидации не обнаружена"

print("Все тесты логики пройдены успешно")
