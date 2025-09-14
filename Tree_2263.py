#divide tree into root nodes in subtree,

import sys
sys.setrecursionlimit(10 ** 6)

def get_subtree_root(idx, root, post_st, in_st, in_ed):#ed -> 0 base -> n - 1

    if in_ed - in_st == 0:
        ans.append(str(root))
        return #leaf
    if in_ed - in_st < 0:
        return #null

    piv = idx[root]#중위 기준 루트 위치 찾기
    left_len = piv - in_st
    right_len = in_ed - piv

    ans.append(str(root))

    if left_len > 0:
        left_root = post[post_st + left_len - 1]
        get_subtree_root(idx, left_root, post_st, in_st, piv - 1)


    if right_len > 0:
        right_root = post[post_st + left_len + right_len - 1]
        get_subtree_root(idx, right_root, post_st + left_len, piv + 1, in_ed)

#7 4 2 5 1 3 8 6 9/ 7 4 5 2 8 9 6 3 1
#0 1 2 3 4 5 6 7 8  0 1 2 3 4 5 6 7 8
# 8 9 6 3
n = int(input())

inorder = list(map(int, input().split()))
post = list(map(int, input().split()))
index_in = dict()
ans = []
for i in range(n):
    index_in[inorder[i]] = i

get_subtree_root(index_in,post[-1], 0, 0, n - 1)

print(" ".join(ans))

