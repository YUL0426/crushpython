코드1) Brute Force
def max_profit(stock_list):
    # 현재까지의 최대 수익
    max_profit_so_far = stock_list[1] - stock_list[0]

    # 한 번 사고 파는 모든 조합을 본다
    for i in range(len(stock_list) - 1):
        for j in range(i + 1, len(stock_list)):
            # i에서 사고 j에 파는 것이 현재까지의 최대 수익이라면 max_so_far을 바꾼다
            max_profit_so_far = max(max_profit_so_far, stock_list[j] - stock_list[i])

    return max_profit_so_far

시간복잡도 : O(n2)

내 코드와 비교)
  잘한점)
  max_profit_so_far과 같은 최대수익을 설정할 변수
  이중 for문 활용
  못한점)
  max_profit_so_far를 잘못 설정함 (stocklist[0]으로)
  이중 for문의 범위 잘못 설정 j문은 잘 설정 하였으나 문을 잘못 설정함
  
코드2)
def max_profit(stock_list):
    # 현재까지의 최대 수익
    max_profit_so_far = stock_list[1] - stock_list[0]

    # 현재까지의 최소 주식 가격
    min_so_far = min(stock_list[0], stock_list[1])

    # 주식 가격을 하나씩 확인한다
    for i in range(2, len(stock_list)):
        # 현재 파는 것이 좋은지 확인한다
        max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_so_far)

        # 현재 주식 가격이 최솟값인지 확인한다
        min_so_far = min(min_so_far, stock_list[i])

    return max_profit_so_far


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))
  
