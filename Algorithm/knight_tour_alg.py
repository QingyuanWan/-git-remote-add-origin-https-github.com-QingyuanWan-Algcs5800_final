def solve_knights_tour(board, x, y, move_count):
    """Recursively attempt to solve the Knight's Tour problem using backtracking."""
    """This code come from https://medium.com/@davidlfliang/intro-python-algorithms-knights-tour-problem-ab0a27a5728c"""

    size = len(board)
    
    if move_count == size * size:
        return True
    
    knight_moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    for dx, dy in knight_moves:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y, board):
            board[new_x][new_y] = move_count
            if solve_knights_tour(board, new_x, new_y, move_count + 1):
                return True
            board[new_x][new_y] = -1
    return False


def create_init_table(sizem, sizen):
    """Pass m, n for create initial tabel with m*n with every -1 fill in"""
    chase_board = []
    for m in range(sizem):
        for n in range(sizen):
            chase_board[m][n] = -1
    
    

def main():
    
    size = 8  # Size of the chessboard
    board = initialize_board(size)
    
    start_x, start_y = 0, 0  # Starting position of the knight
    board[start_x][start_y] = 0  # Initialize the starting position with the first move
    
    if solve_knights_tour(board, start_x, start_y, 1):
        print("Solution found!")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()