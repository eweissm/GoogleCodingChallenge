## challenge 2

# take a list of integers and find the subset which returns the highest product

import math

def solution(xs):

    negativeValues = []

#remove integers that will be useless for now (i.e. 0) ... hold on to the negatives on the side
    for i in range(len(xs)):
        if xs[i]==0:
            del xs[i]
        elif xs[i]<0:
            negativeValues.append(xs[i])
            del xs[i]

    if len(negativeValues) % 2 == 0:  # if we have an even num of neg values --> add the negative values back to the list
        xs.append(negativeValues)
    elif len(negativeValues)>0:
        negativeValues.sort()
        del negativeValues[0]
        xs.append(negativeValues)

    return str(math.prod(xs))
