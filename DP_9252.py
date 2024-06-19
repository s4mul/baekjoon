a = input()
b = input()
metrixSubsequence = [[0 for _ in range(len(b) + 1)] for __ in range(len(a) + 1)]
Max = 0
cor = (0,0)
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            metrixSubsequence[i+1][j+1] = metrixSubsequence[i][j] + 1
            if metrixSubsequence[i+1][j+1] > Max:
                Max = metrixSubsequence[i+1][j+1]
                cor = (i + 1, j + 1)
        else:
            metrixSubsequence[i+1][j+1] = max(metrixSubsequence[i+1][j],metrixSubsequence[i][j+1])

print(Max)
if Max != 0:
    LCS = []
    x, y = cor
    while len(LCS) < Max:
        if(metrixSubsequence[x][y] == metrixSubsequence[x-1][y]):
            x = x - 1
        elif(metrixSubsequence[x][y] == metrixSubsequence[x][y-1]):
            y = y - 1
        else:
            LCS.append(a[x-1])
            y = y - 1
            x = x - 1
    LCS.reverse()
    LCS = ''.join(LCS)
    print(LCS)
