def max_profit(price_list, count):
    #최대 이익을 구하기 위한 max_profit함수
    price = [0]
    num = 0

    for i in range(1, len(price_list)):
    #price_list만큼의 for문
        price.append(price_list[i] // i)
    while count != 0:
    #판매할 개수만큼 while문
        price.reverse()
    #큰가격부터 하기 위한 reverse(?)
        max_map = len(price) - 1 - price.index(max(price))
        #???한 변수 max_map
        price.reverse()
        if max_map <= count:
            num += price_list[max_map] * int(count / (max_map))
            count = count % (max_map)
        price[max_map] = 0
    return num


print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
