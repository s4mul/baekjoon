import sys
input = sys.stdin.readline
N, M = map(int, input().split())

alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
res = dict()
for i in range(N, M + 1):
    if i >= 10:
        res[i] =  alp[i // 10] + alp[i % 10]
    else:
        res[i] = alp[i]

res1 = sorted(res.items(), key = lambda x:x[1])

size = 0
for i in res1:
    size += 1
    print(i[0], end=" ")
    if size % 10 == 0:
        print()