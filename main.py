#challenge 5
# Stairs

#n in range 3 to 200
# rules:
#   Each type of staircase should consist of 2 or more steps.
#   No two steps are allowed to be at the same height - each step must be lower than the previous one.
#   All steps must contain at least one brick.
#   A step's height is classified as the total amount of bricks that make up that step.\

# Me: lets do some gun coding challenges
# Google: what if we make them do discrete math
# Me:
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠶⠖⠒⠛⠛⠛⠒⠶⢦⣤⣤⡶⠶⠶⠶⠶⠶⢶⣶⣦⣤⣴⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣴⣤⣤⣴⡶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠉⠙⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠛⠉⠀⠀⢀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢿⡀⠀⠀⠀⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠙⠻⣷⣄⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢠⣴⠟⠉⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⣷⣄⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠐⣼⡟⠋⠀⠈⢻⣇
# ⠀⠀⠀⠀⠀⢠⣾⠟⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⠀⠀⠀⠸⣿
# ⠀⠀⠀⠀⢠⣿⠇⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⢠⡞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⣼⡏
# ⠀⠀⠀⠀⢸⣿⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣤⠶⠛⠛⠋⠉⠙⠛⠓⠶⣤⡀⠀⢸⡇⠀⠀⣠⣤⣴⠶⠶⠟⠛⠻⠶⢾⣿⣤⡀⠛⢹⣇
# ⠀⠀⠀⣰⡿⠋⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠈⢷⣀⠀⠀⠀⠀⠀⢀⣤⡶⠟⠋⠁⠀⠀⠀⣀⣀⣀⣀⣀⠀⠀⠈⠻⣦⡘⣷⡾⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣼⡏
# ⠀⠀⢰⣿⠃⠀⠀⠀⠀⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠶⣤⣠⣴⠟⠁⢀⣀⣤⡶⠾⠛⠋⠉⠁⠀⠉⠉⠛⢶⣄⠀⢹⣿⠋⣀⣠⣶⠾⠟⠛⠋⠉⠉⠛⠛⠷⣦⣀⠀⢹⣿⠃
# ⠀⠀⢸⣿⠀⠀⠀⠀⠀⠸⣧⡀⠀⠀⠀⠀⢀⣠⣤⣶⠾⠿⠟⢛⣉⣤⡴⠾⠛⠉⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣼⣿⠿⠛⣹⠃⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠙⢷⣆⣿⠀
# ⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠙⠳⣤⣄⣀⣴⡿⠋⠉⠀⣠⡶⠛⠛⡫⠁⠀⠀⢀⡴⠛⢻⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠸⡿⠃⠀⢰⠁⠀⣤⠞⠛⢿⣿⣿⣶⡄⠀⠀⠀⠀⢹⣇⠀
# ⠀⠀⣠⣿⠃⠀⠀⠀⠀⠀⠀⢀⣠⣽⡿⠋⠀⠀⠀⣰⣿⠀⠀⠀⡇⠀⠀⠀⣿⡀⢀⣼⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⢀⣿⣀⣀⡀⠀⢰⣧⣀⣠⣾⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⠀
# ⠀⢸⣿⡇⠀⠀⠀⠀⠀⣀⣾⡿⠛⠁⠀⠀⠀⠀⣸⠟⢻⣆⠀⠀⢳⡀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣀⣴⠾⠛⠉⢉⣿⢿⣿⣾⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⣾⠇⠀
# ⠀⠈⠻⣿⣦⣤⣀⣀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠙⢷⣄⡀⠙⢤⡀⠈⠻⠿⣿⣿⡿⠿⠋⠀⠀⢀⣼⣟⣁⠀⠀⠰⣟⠀⠀⠈⠻⣿⣿⡿⠿⠟⠛⠁⠀⠀⠀⢀⣾⢷⡄⠀
# ⠀⠀⠀⠈⢙⣿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠉⠻⢶⣤⣄⣀⡀⠀⠠⠀⢀⣀⡀⠠⣤⣾⢿⣿⣿⡄⠀⠀⠙⢷⣄⣀⣠⣿⠻⣷⣀⣀⣀⣀⣠⣤⡾⠟⠁⣸⡏⠀
# ⠀⠀⠀⢠⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⠀⠀⠀⠀⠈⠉⠛⠛⠛⠒⠶⠶⠶⠶⠿⢻⣿⣾⣿⣿⣷⡄⠀⠀⠀⠈⣿⠋⠙⣶⣿⠋⠉⠉⠉⠉⠀⣀⣤⣾⡏⠀⠀
# ⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠉⠉⠉⠙⠳⢦⣄⡀⠀⠀⠀⠀⠀⠘⣿⡘⣿⣿⣿⣿⣷⣤⣀⠀⠘⠷⠾⢻⡿⠀⠀⠀⣀⠀⠀⠁⠀⠙⣿⡄⠀
# ⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠰⣦⣀⠀⠀⠀⠈⠙⠛⠶⢶⣤⣄⣀⣹⣷⣜⠻⣿⣿⣿⣿⣿⣿⠀⢀⣴⣿⠶⠞⠛⠉⠉⠙⣷⠀⠀⠀⢹⣿⠀
# ⠀⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⢿⣄⠀⠉⠻⢿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠿⣶⣤⣭⣭⣤⡴⠾⠟⠋⠀⠀⠀⠀⠀⣀⣴⡿⠀⠀⠀⢸⣿⠀
# ⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⡀⠀⠛⢦⣄⡀⠀⠈⠉⠛⠛⠶⠶⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⡴⠶⠾⢿⡟⠉⠀⠀⠀⠀⣸⡿⠀
# ⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢦⣄⠀⠉⠻⢶⣤⣄⣀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠙⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠀⠀⠀⢀⣼⠇⠀⠀⠀⠀⢀⣿⠃⠀
# ⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠶⠶⠶⠶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⠶⠶⠶⠿⠛⠁⠀⠀⠀⠀⢀⣿⠇⠀⠀
# ⠀⢸⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠏⠀⠀⠀
# ⠀⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⢠⡟⠀⠈⢻⡛⠻⢦⣄⡀⢀⣀⣀⡀⠀⣀⡴⠞⢻⡏⠀⠀⣿⣿⣧⠀⠀⠀⠀⠀⣀⣤⣾⣿⣇⠀⠀⠀⠀
# ⢠⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠙⣎⢷⣄⣀⣼⣇⣀⠀⢨⣿⣿⡉⠉⢹⣿⠛⠁⣀⣤⡷⢤⠴⢻⠀⣿⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
# ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣾⣇⣠⡏⣠⡭⢭⡀⢻⣍⢉⣻⣇⣈⣙⣾⡿⣿⣟⡉⣹⢁⡤⠒⢦⡀⠓⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀
# ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢰⡏⠀⠀⣹⠄⢙⡯⠉⣿⣭⣍⣀⣴⣟⠉⠉⠉⢸⡄⠀⢀⣷⡴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
# ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿clown⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⢷⠟⢦⢶⣋⣀⣭⣴⣿⣿⣿⣿⣿⣿⣿⣷⣤⣛⡀⠙⠛⠋⡯⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
# ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
def solution(a):
    SolutionList = zeros(a+1)
    SolutionList[0] = 1
    SolutionList[1] = 1

    for n in range(2, a+1):
        print("n:"+str(n))
        for k in range(a, n-1, -1):
            print("k:"+str(k))
            SolutionList[k] += SolutionList[k-n]

    for j in range(3, a+1):
        SolutionList[j]-=1

    print(SolutionList)
    return SolutionList[a]
def zeros(n):
    zeroslist = [0] * n
    return zeroslist


print(solution(10))
