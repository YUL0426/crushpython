문제)
이미 sublist_max 함수를 각각 Brute Force과 Divide and Conquer 방식으로 작성했는데요. 

Brute Force로 풀었을 때는 시간 복잡도가O(n2)

Divide and Conquer를 사용했을 때는 O(nlgn)였습니다.
이번 과제에서는 시간 복잡도를 

O(n)로 한 번 더 단축해보세요!

내 생각)
O(n)으로 뭔가 원큐에 처리해야하는 문제인 것 같애서 for문을 떠올리는 것 까지는 성공했다.
일단 코드를 좀 써봤어야했는데 빠르게 포기한게 문제다.

코드)
def sublist_max(profits):
    max_profit_so_far = profits[0]  # 반복문에서 현재까지의 부분 문제의 답
    max_check = profits[0]  # 가장 끝 요소를 포함하는 구간의 최대 합
    #Q)위 두개의 변수 차이를 잘 모르겠음, 주석을 보면 차이가 있긴하지만 결국 profits[0]인데..
    #가아니라 max_profit_so_far이 있어야 return을 통해 돌려줄 수도 있고, 최대값 비교도 가능함
    
    # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
        max_check = max(max_check + profits[i], profits[i])
        #profits[i]를 profits[0]에 계속 더해가며 비교  
        # 최대 구간 합을 비교를 통해 정한다
        max_profit_so_far = max(max_profit_so_far, max_check)
        #결국 profits[0]과의 비교
        
    return max_profit_so_far


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))

알게된 점)
변수설정을 같게 해도 주석을 통해 차이를 보일 수 있으며,
같은 변수설정도 비교를 위해 할 수 있음
