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

