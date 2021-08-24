배운점)

의문점)
 1.i = start
   b = start
   start를 동시에 두 개나 설정이 가능한가...?
2. b가 뭘까?
코드)
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
  #리스트 값 확인과 기준점 이하 값들의 위치를 찾아주는 변수 정의
    # 코드를 작성하세요.
    i = start
    b = start
    p = end
    
    #i는 start, p는 end이므로 리스트안을 다 돌 때까지 반복
    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list,i,b)
            b += 1
        i += 1 
    
    swap_elements(my_list, b, p)
    p = b 
    
    return p
# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
