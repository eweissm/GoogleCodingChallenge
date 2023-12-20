# Challenge 3
# Elevator maintenance


def solution(l):  # dont hate me...im an aerospace engineer... not a coder
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(l)-1):
            version_parameters = DeliminateVersionCode(l[i])
            version_parameters_next = DeliminateVersionCode(l[i+1])

            # if next is before current then flip
            if version_parameters[0] > version_parameters_next[0] or\
                    (version_parameters[0] == version_parameters_next[0] and version_parameters[1] > version_parameters_next[1]) or\
                    (version_parameters[0] == version_parameters_next[0] and version_parameters[1] == version_parameters_next[1] and version_parameters[2] > version_parameters_next[2]) or\
                    (version_parameters == version_parameters_next and len(l[i]) > len(l[i+1])):
                l[i], l[i+1] = l[i+1], l[i]
                sorted = False
    return l

def DeliminateVersionCode(code):
    version_parameters = code.split(".")
    if len(version_parameters) == 2:
        version_parameters.append("0")
    if len(version_parameters) == 1:
        version_parameters= version_parameters + ["0", "0"]
    version_parameters = [eval(i) for i in version_parameters]
    return version_parameters

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
