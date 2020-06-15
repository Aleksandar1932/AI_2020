def read_matrix():
    N = int(input())
    input_matrix = []
    for i in range(0, N):
        line = str(input())
        row = []
        for token in line.split("   "):
            row.append(str(token))
        input_matrix.append(row)

    return input_matrix


def cal_mines(matrix, i, j, n):
    if matrix[i][j] == "-":
        suma = 0
        for line in range(max(0, i - 1), min(n, i + 2)):
            for col in range(max(0, j - 1), min(n, j + 2)):
                if (matrix[line][col] == "#"):
                    suma = suma + 1;
        return suma
    else:
        return "#"


if __name__ == '__main__':
    matrix1 = read_matrix()
    N1 = len(matrix1)
    new_mat = [cal_mines(matrix1, i1, j1, N1) for i1 in range(0, N1) for j1 in range(0, N1)]

    for i in range(0, N1 * N1):
        if (i + 1) % N1 == 0:
            print(f"{new_mat[i]}", end='')
            print()
        else:
            print(f"{new_mat[i]}   ", end='')
