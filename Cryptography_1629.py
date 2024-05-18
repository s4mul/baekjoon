import sys

def fastPow(under, upper, modu) -> int:
    if upper == 1:
        return under % modu
        
    res = fastPow(under, upper // 2, modu)
    
    if upper % 2 == 1:
        return ((res %  modu) * (res % modu) * (under%modu))%modu
    else:
        return ((res %  modu) * (res % modu))%modu



tmp = sys.stdin.readline().split()
A = int(tmp[0])
B = int(tmp[1])
C = int(tmp[2])

sys.stdout.write(str(fastPow(A, B, C)))
