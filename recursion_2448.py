def star(basic):
    res = []
    height = len(basic)
    for i in range(height* 2):
        res.append("1")

    for i in range(0,height):
        res[i + height] = basic[i]+" "+basic[i]
    
    for i in range(0,height):
        res[i] = " "*(height) + basic[i] + " "*(height)
        
    
    
    return res

N = int(input())
basic = ["  *  "," * * ","*****"]
N = N/3
k = 0
while N > 1:
    N //= 2
    k += 1

for i in range(k):
    basic = star(basic)

for i in basic:
    print(i)
