def solveable(p_idxs, k_idx, k_moved_to=None):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""
    #p_idxs = set of pawn location 
    #k_idx = tuple of knight location
    #p_capt = set of captured pawn locations (will be added onto per recursive call)
    if k_moved_to == None:
        k_moved_to = set()

    # 1) Base case - is the puzzle solved?
    if len(k_moved_to) == len(p_idxs): return True

    # 2) Find all valid_moves
    for i in valid_moves(k_idx):
        if (i in p_idxs) and (i not in k_moved_to): #if the move chosen in valid_moves(k_idx) will both capture a pawn and not be a repeated move  
            k_moved_to.add(k_idx)        
            #print(i) - i is the locations of pawns that were captured
            #print(k_moved_to) - p_capt will valid move chosen 
            
    # 3) Try all valid_moves
            if solveable(p_idxs, i, k_moved_to):
                return True

    # 4) If nothing worked in step 3, there's no solution with the knight in this position
    return False

def valid_moves(k_idx):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    valid_moves = set() #set to hold valids moves for knight
    l = list() #list to find limitless moves for knight
    x = k_idx[0] #x coordinate
    y = k_idx[1] #y coordinate
    
    #potential moves
    right_down = (x+2,y-1)
    right_up = (x+2,y+1)
    down_right = (x+1,y-2)
    down_left = (x-1,y-2)
    left_down = (x-2,y-1)
    left_up = (x-2,y+1)
    up_left = (x-1,y+2)
    up_right = (x+1,y+2)
    
    #adding to the list
    l.append(right_down)
    l.append(right_up)
    l.append(down_right)
    l.append(down_left)
    l.append(left_down)
    l.append(left_up)
    l.append(up_left)
    l.append(up_right)


    for i in l:
        if (i[0] >= 0) and (i[0] < 8) and (i[1] >= 0) and (i[1] < 8):   #checking through the list for valid moves
            valid_moves.add(i) #add valid moves to set -- valid_moves
            
    return valid_moves

        
