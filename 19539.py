import sys
input = sys.stdin.readline

N = int(input())

tar = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
#일단 합이 3의 배수여야 함.

for i in range(N):
    cnt1 += tar[i] % 2
    cnt2 += tar[i] // 2

while cnt1 > 0 and cnt2 > 0:
    print("1")
    if cnt1 <= cnt2:
        cnt2 -= cnt1
        cnt1 = 0
    else:
        cnt1 -= cnt2
        cnt2 = 0

    if cnt1 == 0:
        cnt2 %= 3
    
if cnt1 == cnt2 == 0:
    print("YES")
else:
    print("NO")