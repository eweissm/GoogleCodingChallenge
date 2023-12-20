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

    prod = "1"
    for j in range(len(xs)):
        prod = multiply(prod, str(xs[j]))


    return prod




def multiply(num1, num2):
    # Convert the input numbers from strings to lists of integers
    num1 = [int(digit) for digit in num1][::-1]
    num2 = [int(digit) for digit in num2][::-1]

    # Initialize the result list with zeros
    result = [0] * (len(num1) + len(num2))

    # Multiply each digit in num2 with num1 and add the result to the appropriate position in the result list
    for i, digit2 in enumerate(num2):
        carry = 0
        for j, digit1 in enumerate(num1):
            product = digit1 * digit2 + carry + result[i + j]
            carry = product // 10
            result[i + j] = product % 10
        result[i + len(num1)] = carry

    # Remove leading zeros from the result list and convert it back to a string
    result = result[::-1]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return ''.join(str(digit) for digit in result)

print(solution([-3, 3, -7, 523, 87, 861,78413,4856]))