def matrix():
    Matr = []
    with open("matrix.txt") as file_matrix:
        for line in file_matrix:
            row = [int(num) for num in line.strip().split(',')]
            Matr.append(row)
    return Matr

def matrix_sum():
    Matr = matrix()
    total_sum = sum(sum(row) for row in Matr)
    return total_sum

def matrix_max():
    Matr = matrix()
    max_value = max(max(row) for row in Matr)
    return max_value

def row_sums():
    Matr = matrix()
    row_sum_list = [sum(row) for row in Matr]
    return row_sum_list

if __name__ == "__main__":
    print("Matrix:", matrix())
    print("Matrix Sum:", matrix_sum())
    print("Matrix Max:", matrix_max())
    print("Row Sums:", row_sums())
