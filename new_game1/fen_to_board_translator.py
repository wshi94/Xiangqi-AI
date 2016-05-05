fen = "4ka3/4a4/r2r5/5P3/C1b6/RN7/P1p6/9/4A4/2B1KAB2 b"

current_location = [0, 0]
board = [['.']*9 for _ in range(10)]

for c in fen:
    if c >= '1' and c <= '9':
        current_location[0] += int(c)
    elif c == '/':
        current_location[1] += 1
        current_location[0] = 0
    elif c == ' ':
        break
    else:
        current_location[0] += 1
        print(current_location)

print(current_location)
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end = ' ')
    print()