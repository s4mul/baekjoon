def rec(x, y, N, sen):
    rang = [sen - (N * 2), sen + N * 2]
    if x < rang[0] or y < rang[0] or rang[1] < x or rang[1] < y:
        print(" ", end="")
    elif x == rang[0] or x == rang[1] or y == rang[0] or y == rang[1]:
        print("*", end="")
    else:
        rec(x, y, N - 1, sen)
        

    
#0 2 4 
    
N = int(input()) - 1
for i in range(1 + 4 * (N)):
    for j in range(1 + 4 * (N)):
        rec(i,j,N , 2 * (N))
    print()


