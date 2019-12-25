def has_jump_way(point, game_board):
    global memorize_jump_history

    x_point = point[0]
    y_point = point[1]

    if (y_point > max_y_point) or (x_point > max_x_point):
        return False

    if memorize_jump_history[y_point][x_point]:
        return memorize_jump_history[y_point][x_point]

    if x_point == len(game_board[y_point]) - 1 and (y_point == len(game_board) - 1):
        memorize_jump_history[y_point][x_point] = True
        return True

    point = game_board[y_point][x_point]

    right_move_point = (x_point + point, y_point)
    right_result = has_jump_way(right_move_point, game_board)

    if right_result:
        memorize_jump_history[y_point][x_point] = True
        return True

    down_move_point = (x_point, y_point + point)
    down_result = has_jump_way(down_move_point, game_board)

    if down_result:
        memorize_jump_history[y_point][x_point] = True
        return True

    memorize_jump_history[y_point][x_point] = False

    return False


if __name__ == "__main__":
    tc = input()
    result_list = []

    for i in range(int(tc)):
        memorize_jump_history = []
        board_list = []
        board_height = int(input())

        for _ in range(board_height):
            board = [int(height) for height in input().split(" ")]
            memorize_jump_history.append([ None for _ in range(len(board))])
            board_list.append(board)

        max_y_point = board_height - 1
        max_x_point = len(board_list[0]) - 1

        result_list.append(has_jump_way((0, 0), board_list))

    for result in result_list:
        if result:
            print("YES")
        else:
            print("NO")
