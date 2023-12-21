#challenge 5
# Stairs

#n in range 3 to 200
# rules:
#   Each type of staircase should consist of 2 or more steps.
#   No two steps are allowed to be at the same height - each step must be lower than the previous one.
#   All steps must contain at least one brick.
#   A step's height is classified as the total amount of bricks that make up that step.
def solution(n):
    prev_f_list = []

    for i in range(1, n+1):
        f = 0

        if i<3:
            f = 0
        elif i == 3:
            f = 1
        else:
            if i%2 == 0:
                A = int(i / 2 - 1)
            else:
                A = int(i/ 2)

            #print("A:"+str(A))
            #print("i:" + str(i))
            for j in range(1,A+1): #1 to A
                #print("j:"+str(j))
                f += max(1 + int(prev_f_list[i-j-1] / 2) - (j-1),1)


        prev_f_list.append(f)
        print(prev_f_list)

    return prev_f_list[n-1]

print(solution(10))