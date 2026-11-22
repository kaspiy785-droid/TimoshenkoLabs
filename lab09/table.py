def row_sums(matrix):
    result = []
    for row in matrix:
        result.append(sum(row))
    return result

def column_sums(matrix):
    if len(matrix) == 0:
        return []
    cols = len(matrix[0])
    result = [0] * cols
    for row in matrix:
        for c in range(cols):
            result[c] += row[c]
    return result

def diagonal_pattern(size):
    matrix = []
    for r in range(size):
        row = []
        for c in range(size):
            if r == c:
                row.append(0)
            elif r < c:
                row.append(1)
            else:
                row.append(2)
        matrix.append(row)
    return matrix

def transform(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for val in row:
            if val < 0:
                new_row.append(0)
            else:
                new_row.append(val)
        new_matrix.append(new_row)
    return new_matrix
