def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
        
def is_safe(board, row, col, n, row_lookup, slash_code, backslash_code):
    return(
        not row_lookup[row] and
        not slash_code[row + col] and
        not backslash_code[row - col + n -1]
    )

def solve_n_queens_util(board,col, n, row_lookup, slash_code, backslash_code):
    if col == n:
        return True
        
    for row in range(n):
        if is_safe(board, row, col, n, row_lookup, slash_code, backslash_code):
            board[row][col] = 1
            row_lookup[row] = slash_code[row + col] = backslash_code[row - col + n - 1] = 1
            
            if solve_n_queens_util(board, col+1, n, row_lookup, slash_code, backslash_code):
                return True
                
            board[row][col] = 0
            row_lookup[row] = slash_code[row + col] = backslash_code[row - col + n - 1] = 0
            
    return False
    
def solve_n_queens(n):
    board = [[0] * n for i in range(n)]
    row_lookup = [0] * n
    slash_code = [0] * (2 * n - 1)
    backslash_code = [0] * (2 * n - 1)
    
    if not solve_n_queens_util(board, 0, n, row_lookup, slash_code, backslash_code):
        print("Solution does not exist")
        return
    
    print_solution(board)
    
n = 8
solve_n_queens(n)