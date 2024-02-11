from dataclasses import dataclass

@dataclass
class MyStruct:
    row: int
    col: int


def ReturnAsMatrix(pos):
    NumberToLetter = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    
    letter = pos[0].upper()
    number = pos[1]
    
    try:
        row = NumberToLetter[letter]
    except KeyError:
        row = -1

    col = int(number)
    
    myPos = MyStruct(row, col)
    
    return myPos
def ReturnAsNormal(pos):
    NumberToLetter = {1:'A',  2:'B', 3:'C',  4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}

    letter = pos.row
    number = pos.col
    
    try:
        row = NumberToLetter[letter]
    except KeyError:
        row = 'Z'

    col = str(number)
    myPos = row+col

    return myPos
def ErrorHandling(piece,specialLoc):
    return (piece=="PAWN" or piece== "KNIGHT" or piece== "BISHOP" or piece== "KING" or piece== "ROOK" or piece== "QUEEN" or piece=="EARL") and specialLoc.col>0 and specialLoc.col<9 and specialLoc.row>0 and specialLoc.row<9
def ReturnPosibleMovesbyPiece(piece)->MyStruct:
    if piece =="PAWN":
            # return positionPAWN(specialLoc)
            moves=[(0, 1)]
    if piece =="KING":
            moves = [(-1, -1), (-1, 0), (-1, 1), 
             (0, -1), (0, 1), 
             (1, -1), (1, 0), (1, 1)]
            # return positionKING(specialLoc)
    if piece =="KNIGHT":
            moves =[(2, -1), (2, 1), (-2, 1), (-2, -1),
             (1, 2), (-1, 2),(1, -2), (-1, -2),
             ]
            # return positionKNIGHT(specialLoc)
    if piece=="ROOK":
            moves =[(0, 1), (0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),(0, 8),
             (0, -1), (0, -2),(0, -3),(0, -4),(0, -5),(0, -6),(0, -7),(0, -8),
             (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
             (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0), (-8, 0)

             ]
            # return positionROOK(specialLoc)
    if piece=="BISHOP":
            moves=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), 
             (-1, -1), (-2, -2), (-3, -3), (-4,- 4), (-5, -5), (-6, -6), (-7, -7), (-8, -8),
             (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7), (-8, 8),
             (1, -1), (2, -2), (3, -3), (4,- 4), (5, -5), (6, -6), (7, -7), (8, -8)

             ]
            # return positionBISHOP(specialLoc)
    if piece=="QUEEN":
            moves = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), 
             (-1, -1), (-2, -2), (-3, -3), (-4,- 4), (-5, -5), (-6, -6), (-7, -7), (-8, -8),
             (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7), (-8, 8),
             (1, -1), (2, -2), (3, -3), (4,- 4), (5, -5), (6, -6), (7, -7), (8, -8),
             ]+[(0, 1), (0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),(0, 8),
             (0, -1), (0, -2),(0, -3),(0, -4),(0, -5),(0, -6),(0, -7),(0, -8),
             (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
             (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0), (-8, 0)

             ]
    if piece=="EARL":
            moves =[(4, -1), (4, 1), (-4, 1), (-4, -1),
             (1, 4), (-1, 4),(1, -4), (-1, -4),
             ]
    return moves
            # return positionQUEEN(specialLoc)
#so earl goes like Knightk but like long L 4 forward and 1 to each side
def position ( piece , loc ) :
    piece=piece.upper()
    specialLoc=ReturnAsMatrix(loc)
    
    if ErrorHandling(piece,specialLoc) and len(loc)==2:
        moves = ReturnPosibleMovesbyPiece(piece)
    
    else:
        print("Wrong Input")
        return[]
    
    answerList = []

    for move in moves:
        newRow = specialLoc.row + move[0]
        newCol = specialLoc.col + move[1]

        if 1 <= newRow <= 8 and 1 <= newCol <= 8:
            new_pos_str=ReturnAsNormal(MyStruct(newRow, newCol))
            
            answerList.append(new_pos_str)

    return answerList
    

print("Hello, if you want to test by yourself please write 1.\nIf you want autoTest by pieces I made for testing click 2.\nType anything else to exit.")

inp = int(input('Your entry:'))
if(inp==1):
    print("1")
    piece=input("Name of piece (it is case insensitive no worries):")
    loc=input("loc of piece (in format of A2)(it is case insensitive no worries):")
    print(position(piece,loc))

elif(inp==2):
    print(position("PAWN","A1"))
    print(position("PAWN","A7"))
    print(position("PAWN","e5"))
    print(position("PaWN","H1"))
    print(position("PawN","H7"))

    print("-----KING")
    print(position("KING","A1"))
    print(position("king","A7"))
    print(position("King","e5"))
    print(position("KING","H1"))
    print(position("King","H7"))

    print("-----KNIGHT")
    print(position("KNIGHT","A1"))
    print(position("knight","A7"))
    print(position("KniGHT","e5"))
    print(position("Knight","H1"))
    print(position("KNIGHT","H7"))

    print("-----ROOK")
    print(position("ROOK","A1"))
    print(position("ROOK","A7"))
    print(position("ROOK","e5"))
    print(position("ROOK","H1"))
    print(position("ROOK","H7"))
    print("-----BISHOp")
    print(position("BISHOp","A1"))
    print(position("BISHOp","A7"))
    print(position("BISHOp","e5"))
    print(position("BISHOp","H1"))
    print(position("BISHOp","H7"))
    print("-----Queen")
    print(position("Queen","A1"))
    print(position("Queen","A7"))
    print(position("Queen","e5"))
    print(position("Queen","H1"))
    print(position("Queen","H7"))
    print("-----EARL")
    print(position("EARL","A1"))
    print(position("EARL","A7"))
    print(position("EARL","e5"))
    print(position("EARL","H1"))
    print(position("EARL","H7"))      
else:
    exit()



# print(position("PawN","Z7"))
# print(position("PawN","C9"))








# print(position("PAWN","H8"))