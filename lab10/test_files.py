from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum

with TemporaryDirectory() as directory:
    p = Path(directory) / "matrix.txt"

    p.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(p) == [[7, -1]]
    assert selected_sum([[7, -1]]) == 7

    p.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(p) == [[0]]
    assert selected_sum([[0]]) == 0

    p.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
    m = read_matrix(p)
    assert m == [[1, -2, 3], [4, 0, -6]]
    assert selected_sum(m) == 8

    bad_cases = [
        "",
        "0 3\n",
        "1 2\n1\n",
        "1 2\n1 x\n",
        "1 1\n5\n6\n",
    ]

    for bad_text in bad_cases:
        p.write_text(bad_text, encoding="utf-8")
        try:
            read_matrix(p)
        except ValueError:
            pass
        else:
            assert False, "Ошибка не обнаружена"

    missing_path = Path(directory) / "no_file.txt"
    try:
        read_matrix(missing_path)
    except FileNotFoundError:
        pass
    else:
        assert False, "FileNotFoundError не вызван"

print("Все проверки успешно пройдены")
