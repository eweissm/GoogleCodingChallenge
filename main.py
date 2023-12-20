# Challenge 4
# bomb babys

#problem has symmetry... it really doesnt matter if we are looking at M or F in any particular search...

# I definitely wrote an alpha-beta pruning algorithm before realizing that I was doing this problem backwards... dont hire me
def solution(M, F):
    n = 0
    SolvedState = 0

    while SolvedState == 0:
        if (M == F):
            if (M == 1):
                SolvedState = 1 # solved
            else:
                SolvedState = 2  # impossible
        else:
            n = n + 1

            if(M>F):
                M = M-F
            elif(M<F):
                F = F-M

    if SolvedState == 1:
        return str(n)
    else:
        return "impossible"

