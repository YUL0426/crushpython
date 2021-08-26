문제)
특정 기간 중 수익이 가장 큰 구간을 찾아내는 함수 sublist_max를 작성해 보려고 합니다.
Brute Force 방법을 이용해서 이 문제를 한 번 풀어봅시다!
함수 설명
우선 함수 sublist_max는 파라미터로 리스트 profits를 받는데요. profits에는 며칠 동안의 수익이 담겨 있습니다. 예를 들어서 profits가 [7, -3, 4, -8]이라면 첫 날에는 7달러를 벌었고, 둘째 날에는 3달러를 잃었고, 셋째 날에는 4달러를 벌었고, 마지막 날에는 8달러를 잃은 거죠.
sublist_max 함수는 profits에서 최대 수익을 내는 구간의 수익을 리턴합니다.
profits가 [7, -3, 4, -8]이라면 무엇을 리턴해야 할까요? profits에서 가장 많은 수익을 낸 구간은 [7, -3, 4]입니다. 이 구간에서 낸 수익은 8달러이니, 8을 리턴하면 되겠죠!
만약 profits가 [-2, -3, 4, -1, -2, 1, 5, -3]이라면? profits에서 수익이 가장 큰 구간은 [4, -1, -2, 1, 5]입니다. 이 구간에서 낸 수익은 7달러이니, 7을 리턴하겠죠?



코드1)
def sublist_max(profits):
    max_profit = profits[0]  # 최대 수익, 받는 리스트의 첫 번째 값을 일단 초기 설정

    for i in range(len(profits)):
        # 인덱스 i부터 j까지 수익의 합을 보관하는 변수
        total = 0

        for j in range(i, len(profits)):
          #i부터 리스트를 또 돈다.
            # i부터 j까지 수익의 합을 계산
            total += profits[j]

            # i부터 j까지 수익의 합이 최대 수익이라면, max_profit 업데이트
            max_profit = max(max_profit, total)

    return max_profit


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))


코드2)
def sublist_max(profits):
    sum_max = profits[0]

    for i in range(len(profits)):
        for j in range(len(profits)):
            sum_max = max(sum(profits[i:j + 1]), sum_max)
    #Q함수 sum
    return sum_max


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
