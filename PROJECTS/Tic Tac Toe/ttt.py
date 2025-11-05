def print_board(board):
    print()
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("🎮 Welcome to Tic Tac Toe!")
    print("Enter your move as row and column (0, 1, or 2).")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn:")
        
        try:
            row = int(input("  Row (0-2): "))
            col = int(input("  Col (0-2): "))
            if board[row][col] != " ":
                print("⚠️  That spot is taken! Try again.\n")
                continue
        except (ValueError, IndexError):
            print("⚠️  Invalid input. Please use numbers between 0 and 2.\n")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🏆 Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()

# 🎮 Welcome to Tic Tac Toe!
# Enter your move as row and column (0, 1, or 2).

#    |   |
# ---+---+---
#    |   |
# ---+---+---
#    |   |

# Player X's turn:
#   Row (0-2): 01
#   Col (0-2): 1

#    |   |
# ---+---+---
#    | X |
# ---+---+---
#    |   |

# Player O's turn:
#   Row (0-2): 1
#   Col (0-2): 2

#    |   |
# ---+---+---
#    | X | O
# ---+---+---
#    |   |

# Player X's turn:
#   Row (0-2): 3
#   Col (0-2): 1
# ⚠️  Invalid input. Please use numbers between 0 and 2.


#    |   |
# ---+---+---
#    | X | O
# ---+---+---
#    |   |

# Player X's turn:
#   Row (0-2): 2
#   Col (0-2): 0

#    |   |
# ---+---+---
#    | X | O
# ---+---+---
#  X |   |

# Player O's turn:
#   Row (0-2): 0
#   Col (0-2): 0

#  O |   |
# ---+---+---
#    | X | O
# ---+---+---
#  X |   |

# Player X's turn:
#   Row (0-2): 0
#   Col (0-2): 2

#  O |   | X
# ---+---+---
#    | X | O
# ---+---+---
#  X |   |

# 🏆 Player X wins!
