import sys

def order(mod, perent, tree):
    if mod == 0:
        sys.stdout.write(perent)
    if tree[perent][0] != ".":
        order(mod, tree[perent][0], tree)
    if mod == 1:
        sys.stdout.write(perent)
    if tree[perent][1] != ".":
        order(mod, tree[perent][1], tree)
    if mod == 2:
        sys.stdout.write(perent)


tree = {}
size = int(sys.stdin.readline())
for i in range(size):
    perent, left, right = sys.stdin.readline().split()
    tree[perent] = [left,right]

for i in range(3):
    order(i, "A", tree)
    sys.stdout.write("\n")
