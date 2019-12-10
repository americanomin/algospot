def get_number_of_ways(problem_board):
    total_count = sum([matrix_row.count(True) for matrix_row in problem_board])
    if ((total_count % 3) != 0) or total_count == 0:
        return 0

    for row_index, row in enumerate(problem_board):
        for column_index, column in enumerate(row):
            if column == False:
                continue
            if row[column_index+1] and problem_board[row_index+1][column_index]:
                # block_coordinate =
                row[column_index+1] = False
                problem_board[row_index+1][column_index] = False
                get_number_of_ways(problem_board)
            else:
                return 0

    return 1

if __name__ == '__main__':
    problem_boards = []
    for _ in range(int(input())):
        dimension = input().split()
        height = int(dimension[0])
        width = dimension[1]
        problem_board = []
        for _ in range(height):
            line = input()
            matrix_row = []
            for char in line:
                if char == "#":
                    matrix_row.append(False)
                else:
                    matrix_row.append(True)

            problem_board.append(matrix_row)

        problem_boards.append(problem_board)

    for problem_board in problem_boards:
        get_number_of_ways(problem_board)
