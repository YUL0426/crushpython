def select_stops(water_stops, capacity):
    # 약수터 위치 리스트
    stop_list = []

    # 마지막 들른 약수터 위치
    last = 0

    for i in range(len(water_stops)):
        # i 지점까지 갈 수 없으면, i - 1 지점 약수터를 들른다
        if water_stops[i] - last > capacity:
            stop_list.append(water_stops[i - 1])
            #stop_list에 append한다
            last = water_stops[i - 1]

    # 마지막 약수터는 무조건 간다
    stop_list.append(water_stops[-1])

    return stop_list


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))




My code)
def select_stops(water_stops, capacity):
    water=[]
    for i in len(water_stops):
        while capacity != 0:
            capacity -= water_stops[i]
            if capacity ==0:
                water.append(water_stops[i])
    return water            
        

# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))

시간 복잡도
인풋 water_stops의 길이를 n이라고 합시다.
함수 select_stops는 n에 비례하는 반복문이 하나 있기 때문에, 시간 복잡도는O(n)입니다.

