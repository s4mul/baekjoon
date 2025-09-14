N, S = map(int, input().split())
Seq = list(map(int, input().split()))
aqq = [0 for _ in range(N + 1)]

#N^2 = timeout
#N or N log N

s = 1
e = 1
for i in range(1, N + 1):
    aqq[i] = Seq[i  - 1] + aqq[i -1]

Min = 100001
while(e < len(aqq)):

    if aqq[e] - aqq[s - 1] >= S:
        Min = min(Min, e - s + 1)
        s = s + 1
    else:
        e = e + 1

print(0 if 100001 == Min else Min)


