# Google Foobar coding challenge
## Chalenge 1: Braille Translation
# I compressed the braille into binary and then we spit out the answer


def solution(input_string):
    brailleDictionary = {
        " ": 0, "a": 32, "b": 48, "c": 36, "d": 38, "e": 34, "f": 52, "g": 54, "h": 50, "i": 20, "j": 22,
        "k": 40, "l": 56, "m": 44, "n": 46, "o": 42, "p": 60, "q": 62, "r": 58, "s": 28, "t": 30, "u": 41,
        "v": 57, "w": 23, "x": 45, "y": 47, "z": 43}

    OutputStr = ""
    for x in input_string:
        if x.isupper():
            OutputStr = OutputStr + "000001"
        elif x == " ":
            OutputStr = OutputStr + "000000"
        OutputStr=OutputStr + str(format(brailleDictionary[x.lower()],'b'))
    return OutputStr

print(solution("A "))