def check_win(board, player):
    
    # 가로 확인
    for row in board:
        if all(r == player for r in row):
            return True
        
    # 세로 확인
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # 대각선 확인
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def solution(board):
    countO = sum(b.count("O") for b in board)
    countX = sum(b.count("X") for b in board)
    
    # O, X 표시 개수 차이가 1 초과는 나올 수 없음, X가 더 많을 수 없음
    if countO < countX or countO - countX > 1 :
        return 0
    
    # 선공, 후공 중 이긴 사람이 있는지 검사
    Owin = check_win(board, "O")
    Xwin = check_win(board, "X")
        
    if Owin and Xwin:
        return 0
    
    if Owin and countO != countX + 1:
        return 0
    
    if Xwin and countO != countX:
        return 0
   
    return 1