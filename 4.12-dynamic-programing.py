#! /usr/bin/env python3


def dpmake_change(coin_value_list, change):
    min_coins = list(range(change+1))
    coins_used = list(range(change+1))

    for cents in range(change+1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents-j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    print(min_coins[change])
    return min_coins, coins_used

def result(change, min_coins, coins_used):
    if change == 0:
        return
    else:
        i = min_coins[change]
        coin_value = coins_used[change]
        change = change - coin_value
        print("第 {:^2} 枚硬币面值 {:^4} 元，余额 {:^4} 元".format(i,coin_value,change))
        result(change,min_coins,coins_used) 

def main():
    amnt = int(input("请输入找零数值："))
    coin_value_list = [1, 2, 5, 10, 20, 50, 100]
    min_coins, coins_used = dpmake_change(coin_value_list,amnt)
    result(amnt,min_coins,coins_used)
if __name__ == '__main__':
    main()
