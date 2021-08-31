초기답안)
def trapping_rain(buildings):
    # 코드를 작성하세요
    # 옆건물이랑 비교해서 작으면 더하고 크거나같으면, 넘어간다
    water = 0
    for i in (len(buildings)):
        for j in (i, len(buildings)):
            if buildings[i] >= buildings[j]:
                i += 1
            else:
                water += (buildings[j] - buildings[i])
    return water


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

모범답안) Brute Force
def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0
    
    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i+1:])
    
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)
    
        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])
    
    return total_height
  
  느낀점)
  1, 그렇구나.....
  
  모범답안2)
  def trapping_rain(buildings):
    total_height = 0 # 총 갇히는 비의 양을 담을 변수
    n = len(buildings)

    # 각각 왼쪽 오른쪽 최대값 리스트 정의
    left_list = [0] * n
    right_list = [0] * n
    # 왜와이?
    
    # buildings 리스트 각 인덱스 별로 왼쪽으로의 최댓값을 저장한다
    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i-1], buildings[i-1])
                
    # buildings 리스트 각 인덱스 별로 오른쪽으로의 최댓값을 저장한다
    right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i+1], buildings[i+1])

    # 저장한 값들을 이용해서 총 갇히는 비의 양을 계산한다
    for i in range(1, n-1):
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(right_list[i], left_list[i])

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

느낀점)
1, 내가 아직 슬라이싱을 잘 못한다
