import json
from pathlib import Path
from tempfile import TemporaryDirectory
from analysis import validate_todos, completion_counts, top_users, select_tasks

sample_todos = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]
sample_copy = [item.copy() for item in sample_todos]

validate_todos(sample_todos)
counts = completion_counts(sample_todos)
assert counts == {5: 2, 10: 2}
assert top_users(counts) == [5, 10]

selected_5 = select_tasks(sample_todos, 5)
assert [t["id"] for t in selected_5] == [1, 2, 5]
assert select_tasks(sample_todos, 999) == []

validate_todos([])
assert completion_counts([]) == {}
assert top_users({}) == []
assert select_tasks([], 5) == []

only_false = [{"id": 1, "userId": 1, "title": "Тест", "completed": False}]
assert completion_counts(only_false) == {1: 0}
assert top_users({1: 0}) == []

single_leader = {3: 5, 1: 2}
assert top_users(single_leader) == [3]

bad_datasets = [
    {"id": 1},
    [
        {"id": 1, "userId": 1, "title": "A", "completed": True},
        {"id": 1, "userId": 2, "title": "B", "completed": False},
    ],
    [{"id": 1, "title": "A", "completed": True}],
    [{"id": 1, "userId": 1, "title": "A", "completed": "false"}],
    [{"id": True, "userId": 1, "title": "A", "completed": True}],
]

for bad in bad_datasets:
    try:
        validate_todos(bad)
    except ValueError:
        pass
    else:
        assert False, "Ошибка валидации не обнаружена"

with TemporaryDirectory() as tmp:
    out_file = Path(tmp) / "out.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(selected_5, f, ensure_ascii=False, indent=2)
    with open(out_file, "r", encoding="utf-8") as f:
        restored = json.load(f)
    assert restored == selected_5

assert sample_todos == sample_copy

print("Все проверки успешно пройдены")
