def main(matrix, target):
    last_raw = 0
    for i in range(0, len(matrix)):
        if matrix[i][0] > target:
            return target in matrix[last_raw]
        last_raw = i
    return target in matrix[last_raw]

if __name__ == "__main__":
    matrix = [[1]]
    target = 1
    print(main(matrix, target))