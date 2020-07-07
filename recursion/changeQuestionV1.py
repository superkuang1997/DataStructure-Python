def recMC(coinValueList, change):
    min_coins = change
    if change in coinValueList:
        return 1
    else:
        for value in [c for c in coinValueList if c < change]:
            coins = 1 + recMC(coinValueList, change - value)
            if coins < min_coins:
                min_coins = coins
        return min_coins


recMC([1, 5, 10], 60)