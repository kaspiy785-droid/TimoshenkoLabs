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
