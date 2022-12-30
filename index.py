import itertools

n = m = 0
decisionMatrix = []
weights = []
permutations = []
attributValues = []
alternativeValues = []

def qualiflex():
    # input part
    with open("input.txt") as f:
        n, m = list(map(int, f.readline().split()))
        for i in range(m):
            line = f.readline()
            decisionMatrix.append(list(map(float, line.split())))
        weights = list(map(float, f.readline().split()))
    # 1. The initial permutation of alternatives
    initPerm = list(itertools.permutations([i+1 for i in range(m)], m))

    print("Initial permutations: ", initPerm)

    # 2. The initial ranking of alternatives
    initRank = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r = 1
            for k in range(m):
                if decisionMatrix[i][j] < decisionMatrix[k][j]:
                    r += 1
            initRank[i][j] = r
    print("Initial rank: ", initRank)

    # 3, 4. The dominant and submissive values & The permutations values of attributes
    for perm in initPerm:
        values = []
        for i in range(n):
            value = 0
            for j in range(m):
                for k in range(m):
                    if k > j:
                        a = perm[j] - 1
                        b = perm[k] - 1
                        if decisionMatrix[a][i] == decisionMatrix[b][i]:
                            continue
                        if decisionMatrix[a][i] < decisionMatrix[b][i]:
                            value -= 1
                        else:
                            value += 1
            values.append(value)
        attributValues.append(values)
    print("Permutation values of attributes:", attributValues)

    #5. The permutation values of alternatives
    for attribute in attributValues:
        s = 0
        for i in range(n):
            s += attribute[i] * weights[i]
        alternativeValues.append(round(s, 3))
    print("Permutation values of alternatives:", alternativeValues)

    #6. The final ranking of alternatives
    mx = -1e9
    finalRanking = []

    for i in range(len(initPerm)):
        alternative = alternativeValues[i]
        if alternative > mx:
            mx = alternative
            finalRanking = initPerm[i]
    print("Fianl ranking is: ", finalRanking)

qualiflex()