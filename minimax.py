MAX = 1000
MIN = -1000
def minimax(depth, nodeIndex, maximizingPlayer, values):
    if depth == 3:
        return values[nodeIndex]
        
    if maximizingPlayer:
        best = MIN
        for i in range(0,2):
            val = minimax(depth+1, nodeIndex *2 + i , False, values)
            best = max(best,val)
        return best
    else:
        best = MAX
        for i in range(0,2):
            val = minimax(depth+1, nodeIndex * 2 + i, True, values)
            best = min(best,val)
        return best

if __name__ == "__main__":
    values = [3,5,6,9,1,2,0,-1]
    print("The optimal value is: ", minimax(0,0,True, values))