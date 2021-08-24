#tabulation이므로 데이터를 저장시켜 놓을 표(table)필요

배운점)
1. tabulation이라 하면 가장 먼저 표가 필요하다
2.


의문인점)
1. for j in range(1, i // 2 + 1): -< 여기서 왜 i // 2+1 인가...
for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

코드)
def max_profit(price_list, count):
    # 개수별로 가능한 최대 수익을 저장하는 리스트
    # 새꼼달꼼 0개면 0원
    profit_table = [0]

    # 개수 1부터 count까지 계산하기 위해 반복문
    for i in range(1, count + 1):
        # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
        if i < len(price_list):
            profit = price_list[i]
        # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
        else:
            profit = 0
        # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
        
        # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)

    return profit_table[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
