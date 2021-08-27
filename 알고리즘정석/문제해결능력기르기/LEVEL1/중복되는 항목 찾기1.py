문제)
(N + 1)의 크기인 리스트에, 1부터 N까지의 임의의 자연수가 요소로 할당되어 있습니다. 

그렇다면 어떤 수는 꼭 한 번은 반복되겠지요.

예를 들어 [1, 3, 4, 2, 5, 4]와 같은 리스트 있을 수도 있고, [1, 1, 1, 6, 2, 2, 3]과 같은 리스트가 있을 수도 있습니다. 
(몇 개의 수가 여러 번 중복되어 있을 수도 있습니다.)

이런 리스트에서 반복되는 요소를 찾아내려고 합니다.

중복되는 어떠한 수 ‘하나’만 찾아내도 됩니다.
즉 [1, 1, 1, 6, 2, 2, 3] 예시에서 1, 2를 모두 리턴하지 않고, 1 또는 2 하나만 리턴하게 하면 됩니다.

중복되는 수를 찾는 시간 효율적인 함수를 설계해보세요.

답안1)
def find_same_number(some_list):
    # 코드를 쓰세요
    for i in range(1, len(some_list)):
     some_list.remove(i)
    return some_list[0]

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

내코드와 유사한 답안2)
def find_same_number(some_list):
    # 가능한 모든 조합을 다 돌면서 반복 요소가 있는지 확인하고 있으면 해당 요소를 리턴한다
    for i in range(len(some_list)):
        for j in range(i + 1, len(some_list)):
            if some_list[i] == some_list[j]:
                return some_list[i]


내 코드)
def find_same_number(some_list):
    # 코드를 쓰세요
    i=0
    j=0
    num=0
    for i in some_list:
        for j in some_list:
            if some_list[i] == some_list[j]:
                num=some_list[i]
    return num    

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

결과)
3
5
4
아마 내가 지금 구한건 i와 j로 두번 돌리는데 위치가 같은 값을 반환하는 코드를 짜서 3,5,4로 결과가 반환되는 듯 하다.
그렇다면
위치가 아니라 값이 같게 해야한다
