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
            negativeValues.append(abs(xs[i]))
            xs[i] = 1

    if len(negativeValues) % 2 != 0:
        negativeValues.sort()
        del negativeValues[0]
    xs = xs+negativeValues

    xs = remove_items(xs, 1)

    if bool(xs):
        prod = 1
        for j in range(len(xs)):
            prod = prod*xs[j]
    else:
        prod = 0

    return str(prod)

def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

print(solution([-3, 3, -7, 523, 87, 861,78413,4856]))
print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, -4, -5]))
print(solution([0,0,0,0]))