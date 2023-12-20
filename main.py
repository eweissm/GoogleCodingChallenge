## challenge 2

# take a list of integers and find the subset which returns the highest product
#  remove integers that will be useless for now (i.e. 0) ... hold on to the negatives on the side
# if we have an even num of neg values --> add the negative values back to the list
#else, we will remove smallest magnitude neg and then

def solution(xs):

    negativeValues = [i for i in xs if i < 0]
    xs = [i for i in xs if i > 0]

    if len(negativeValues) % 2 != 0:
        negativeValues.sort()
        del negativeValues[-1]

    xs = xs+negativeValues

    if bool(xs):
        prod = 1
        for j in range(len(xs)):
            prod = prod*xs[j]
    else:
        prod = 0

    return str(prod)


print(solution([-1, -1]))
print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([0,0,0,0]))