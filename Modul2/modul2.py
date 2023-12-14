import random

create_board = lambda width, height: [[' ' for _ in range(width)] for _ in range(height)]

def draw_board(board, piece_pos, goal_pos):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (row, col) == piece_pos:
                print('A', end=' ')
            elif (row, col) == goal_pos:
                print('O', end=' ')
            else:
                print('.', end=' ')
        print()

generate_positions = lambda width, height: ((pos // width, pos % width) for pos in random.sample(range(width * height), 2))

def move_piece(board, piece_pos, direction):
    row, col = piece_pos
    if direction == 'w' and row > 0:
        piece_pos = (row - 1, col)
    elif direction == 's' and row < len(board) - 1:
        piece_pos = (row + 1, col)
    elif direction == 'a' and col > 0:
        piece_pos = (row, col - 1)
    elif direction == 'd' and col < len(board[row]) - 1:
        piece_pos = (row, col + 1)
    return piece_pos


def main():
    try:
            
        width = int(input("Enter the board matrix width: "))
        height = int(input("Enter the board matrix height: "))
        board = create_board(width, height)
        piece_pos, goal_pos = generate_positions(width, height)
        draw_board(board, piece_pos, goal_pos)

        for _ in range(3):
            regenerate = input("New Position (Y/N)? ").lower()
            if regenerate == "y":
                board = create_board(width, height)
                piece_pos, goal_pos = generate_positions(width, height)
                draw_board(board, piece_pos, goal_pos)
            elif regenerate == "n":
                break
            else:
                break

        print("Welcome to the game!")
        print("Move the 'A' piece to the 'O' goal to win.")
        win = False
        while True:
            
            draw_board(board, piece_pos, goal_pos)
            direction = input("Enter the movement direction (w/s/a/d): ")

            for move in direction:

                if move not in ['w', 's', 'a', 'd']:
                    print("Invalid movement direction. Use w/s/a/d.")
                    continue

                piece_pos = move_piece(board, piece_pos, move)

                if piece_pos == goal_pos:
                    draw_board(board, piece_pos, goal_pos)
                    print("Congratulations, you win!")
                    win = True
                    break
            if win:
                break
            elif not win:
                print("Sorry, you lose.")
            break
    except ValueError:
        print("Board width and height must be numeric.")

if __name__ == "__main__":
    main()