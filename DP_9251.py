a = input()
b = input()
metrixSubsequence = [[0 for _ in range(len(b) + 1)] for __ in range(len(a) + 1)]
Max = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            metrixSubsequence[i+1][j+1] = metrixSubsequence[i][j] + 1
            if metrixSubsequence[i+1][j+1] > Max:
                Max = metrixSubsequence[i+1][j+1]
        else:
            metrixSubsequence[i+1][j+1] = max(metrixSubsequence[i+1][j],metrixSubsequence[i][j+1])
print(Max)
