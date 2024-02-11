def is_valid_square(p, loc):
    return p in 'abcdefgh' and 1 <= loc <= 8
def get_new_p(p, increment):
    ps = 'abcdefgh'
    index = ps.index(p)
    new_index = index + increment
    if 0 <= new_index < len(ps):
        return ps[new_index]
    else:
        return None

def king_moves(p, loc):
    moves = []
    for df in range(-1, 2):
        for dr in range(-1, 2):
            if df == 0 and dr == 0:
                continue
            new_p = get_new_p(p, df)
            new_loc = loc + dr
            if new_p and is_valid_square(new_p, new_loc):
                moves.append(new_p + str(new_loc))
    return moves

def line_moves(p, loc, p_step, loc_step):
    moves = []
    for i in range(1, 8):
        new_p = get_new_p(p, p_step * i)
        new_loc = loc + loc_step * i
        if not new_p or not is_valid_square(new_p, new_loc):
            break 
        moves.append(new_p + str(new_loc))
    return moves

def queen_moves(p, loc):
    moves = []
    for df in range(-1, 2):
        for dr in range(-1, 2):
            if df == 0 and dr == 0:
                continue
            moves.extend(line_moves(p, loc, df, dr))
    return moves
def bishop_moves(p, loc):
    moves = []
    p_increments = [1, 1, -1, -1]
    loc_increments = [1, -1, 1, -1]

    for i in range(4):
        moves.extend(line_moves(p, loc, p_increments[i], loc_increments[i]))
    return moves

def rook_moves(p, loc):
    moves = []
    p_increments = [1, -1, 0, 0]
    loc_increments = [0, 0, 1, -1]

    for i in range(4):
        moves.extend(line_moves(p, loc, p_increments[i], loc_increments[i]))
    return moves

def knight_moves(p, loc):
    moves = []
    p_increments = [2, 2, -2, -2, 1, 1, -1, -1]
    loc_increments = [1, -1, 1, -1, 2, -2, 2, -2]

    for i in range(8):
        new_p = chr(ord(p) + p_increments[i])
        new_loc = loc + loc_increments[i]
        if is_valid_square(new_p, new_loc):
            moves.append(new_p + str(new_loc))
    return moves

def pawn_moves(p, loc):
    if loc == 8:
        return []  # Pawns can't move from the 8th loc
    return [p + str(loc + 1)]


def earl_moves(p, loc):
    moves = []
    p_increments = [2, 2, -2, -2, 1, 1, -1, -1]
    loc_increments = [1, -1, 1, -1, 2, -2, 2, -2]

    for i in range(8):
        df = p_increments[i]
        dr = loc_increments[i]
        new_p = chr(ord(p) + df)
        new_loc = loc + dr
        if is_valid_square(new_p, new_loc):
            extra_p = chr(ord(new_p) + df)
            extra_loc = new_loc + dr
            if is_valid_square(extra_p, extra_loc):
                moves.append(extra_p + str(extra_loc))
    return moves

def position(piece, loc):
    if len(loc) != 2 or not loc[0].isalpha() or not loc[1].isdigit():
        return []

    p, loc = loc[0].lower(), int(loc[1])
    if not is_valid_square(p, loc):
        return []

    piece = piece.lower()
    if piece == 'king':
        return king_moves(p, loc)
    elif piece == 'queen':
        return queen_moves(p, loc)
    elif piece == 'rook':
        return rook_moves(p, loc)
    elif piece == 'bishop':
        return bishop_moves(p, loc)
    elif piece == 'knight':
        return knight_moves(p, loc)
    elif piece == 'pawn':
        return pawn_moves(p, loc)
    elif piece == 'earl':
        return earl_moves(p, loc)
    else:
        return []





piece=input("piece:")

loc=input("loc:")
print(position(piece,loc))
