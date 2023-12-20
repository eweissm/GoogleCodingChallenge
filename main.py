## challenge 2

# take a list of integers and find the subset which returns the highest product
#  remove integers that will be useless for now (i.e. 0) ... hold on to the negatives on the side
# if we have an even num of neg values --> add the negative values back to the list
#else, we will remove smallest magnitude neg and then


def solution(xs):

    negativeValues = []
    for i in range(len(xs)):
        if xs[i] == 0:
            xs[i] = 1
        elif xs[i] < 0:
            negativeValues.append(xs[i])
            xs[i] = 1

    if len(negativeValues) % 2 != 0:
        negativeValues.sort()
        del negativeValues[-1]
    xs = xs+negativeValues

    prod = 1.
    for j in range(len(xs)):
        prod = prod*xs[j]

    return str(int(prod))

print(solution([-1000, 0, -1000, 23, 24, 24, 151,984,444,464,859,848, 888,0,]))