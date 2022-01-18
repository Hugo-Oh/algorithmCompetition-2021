import sys

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

H = len(board)
W = len(board[0])

stack = []
answer = 0
for c in board:
    print(c)

for col in moves:
    for y in range(H):
        if board[y][col-1] != 0:
            if not stack:
                stack.append(board[y][col-1])
            else:
                if stack[-1] == board[y][col-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[y][col-1])
            board[y][col-1] = 0
            break

print(answer)




