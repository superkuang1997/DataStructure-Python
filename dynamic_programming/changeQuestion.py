"""
找零问题
"""


def dpMC(coinValueList, change):
    RecordNum = [0] * (change + 1)
    RecordValue = [0] * (change + 1)
    for value in range(1, 1 + change):  # 遍历所有问题规模
        min_coins = value  # 初始化
        new_coin = 1
        for face_value in [c for c in coinValueList if c <= value]:
            if RecordNum[value - face_value] + 1 < min_coins:
                min_coins = RecordNum[value - face_value] + 1
                new_coin = face_value
        RecordNum[value] = min_coins
        RecordValue[value] = new_coin
    return RecordNum[change], RecordValue

# 回溯子问题的最优解


def printCoins(coinsUsed, change):
    """
    retrace the route of optimal solution
    for example:
                21 → 20 → 10 → 0
    """
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


num, coinsUsed = dpMC([1, 5, 10, 21, 25], 63)
printCoins(coinsUsed, 63)