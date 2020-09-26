def create_matrix(n):
    rows, columns = [int(x) for x in input(f'Enter matrix{n} dimension: ').split()]

    matrix = []
    for row in range(rows):
        row_elements = [int(x) for x in input(f'Enter row {row + 1} elements: ').split()][:columns]
        matrix.append(row_elements)
    return matrix


matrix1 = create_matrix(1)
matrix2 = create_matrix(2)

print(f'Matrix 1 => {matrix1}')
print(f'Matrix 2 => {matrix2}')
