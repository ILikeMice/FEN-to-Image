from PIL import Image

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],  
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
]

usrinput = input("Please enter a FEN:")
usrinput = list(usrinput)
currentpos = 0
currentrow = 0
for i in usrinput:
    if i.isnumeric():
        currentpos += int(i)
        continue
    elif i != "/" and i != " ":
        board[currentrow][currentpos] = i
    currentpos += 1
    if i == "/":
        currentrow += 1
        currentpos = 0
    if i == " ":
        break

print(board)

boardimg = Image.open("./images/board.png").copy()


for i in range(8):
    for b in range(8):
        if board[i][b] and board[i][b].islower():
            piece = Image.open(f"./images/w{board[i][b]}.png")
            piece.resize((515//8, 515//8))
            boardimg.paste(piece, (((515//8)*b), (515//8)*i), piece)
        elif board[i][b] and board[i][b].isupper():
            piece = Image.open(f"./images/b{board[i][b].lower()}.png")
            piece.resize((515//8, 515//8))
            boardimg.paste(piece, (((515//8)*b), (515//8)*i), piece)

boardimg.save("output.png")

