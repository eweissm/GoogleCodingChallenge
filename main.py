# Challenge 4
# bomb baby's

#problem has symmetry... it really doesnt matter if we are looking at M or F in any particular search...

# I definitely wrote an alpha-beta pruning algorithm before realizing that I was doing this problem backwards... dont hire me
def solution(M, F):
    M = int(M)
    F = int(F)
    n = 0
    SolvedState = 0

    while SolvedState == 0 and M > 0 and F > 0:
        if M == F:
            if M == 1:
                SolvedState = 1  # solved
            else:
                SolvedState = 2  # impossible
        else:
            n = n + 1

            if M > F:
                M = M-F
            elif M < F:
                F = F-M

    if SolvedState == 1:
        return str(n)
    else:
        return "impossible"

print(solution('4', '7')) #4
print(solution('1', '2')) #1
print(solution('1', '1')) #0
print(solution('2', '4')) #impossible
print(solution('1000', '101')) #1
