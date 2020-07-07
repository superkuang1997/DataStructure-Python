# 增加记录最优解的表（记忆化/函数值缓存），消除重复计算

def recMC(coinValueList, change, Record):
    min_coins = change
    if change in coinValueList:
        Record[change] = 1  # 因为charge不为0, 故Record[0]始终为0
        return 1
    elif Record[change] > 0:
        return Record[change]
    else:
        for value in [c for c in coinValueList if c < change]:
            coins = 1 + recMC(coinValueList, change - value, Record)
            if coins < min_coins:
                min_coins = coins
                Record[change] = min_coins
        return min_coins


recMC([1, 5, 10], 60, [0] * 61)