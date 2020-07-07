

def knapsack(tr, w):
    m = {}
    max_v = 0
    if tr == set() or w == 0:
        m[tuple(tr),w] = 0
        return 0
    elif (tuple(tr), w) in m:
        return m[(tuple(tr), w)]
    else:
        for t in tr:
            if w >= t[0]:
                v = knapsack(tr-{t}, w-t[0]) + t[1]
                max_v = max(v, max_v)
        m[(tuple(tr), w)] = max_v
        return max_v  # 如果当前背包容量小于任何一个weight，直接返回max_v = 0


tr = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}
max_w = 30
print(knapsack(tr, max_w))