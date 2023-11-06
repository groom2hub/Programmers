# https://school.programmers.co.kr/learn/courses/30/lessons/120866

def solution(board):
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                if j > 0 and board[i][j-1] != 1:
                    board[i][j-1] = 2
                if j < len(board[i]) - 1 and board[i][j+1] != 1:
                    board[i][j+1] = 2
                
                if i > 0:
                    if j > 0 and board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                    if j < len(board[i]) - 1 and board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                
                if i < len(board) - 1:
                    if j > 0 and board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2
                    if j < len(board[i]) - 1 and board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2
    
    for i in board:
        answer += i.count(0)
    
    return answer