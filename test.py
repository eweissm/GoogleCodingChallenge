# repeated structure... maybe turn this into a callable function to reduce size and make it generalized
majors.append(int(version_parameters[0]))

if len(version_parameters) > 1:
    minors.append(int(version_parameters[1]))
else:
    minors.append(0)

if len(version_parameters) > 2:
    revisions.append(int(version_parameters[2]))
else:
    revisions.append(0)

while bool(majors):
    major_indices = [i for i, x in enumerate(majors) if x == min(majors)]  # indices of all the minimum majors

    minor_subset = minors[major_indices]
    revisions_subset = revisions[major_indices]

    for i in sorted(major_indices, reverse=True):  # remove items which have been sorted
        del majors[i]
        del minors[i]
        del revisions[i]
