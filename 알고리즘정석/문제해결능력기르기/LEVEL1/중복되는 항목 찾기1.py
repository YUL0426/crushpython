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
시간복잡도 : 이렇게 하면 인풋 리스트의 길이가 n이라고 할 때, <인풋 리스트 길이에 비례하는 이중 중첩 반복문 사용하기 때문에> 시간 복잡도는 
O(n2)가 되겠네요. 
쉽게 생각해 낼 수 있고 무조건 답을 구할 수 있습니다.
하지만 문제의 조건이 시간 효율적인 함수를 작성하는 것이었는데요, 
O(n2)은 그다지 효율적인 방법 같지는 않군요.
모든 조합을 다 확인해보는 것보다 효율적인 방법을 생각해봅시다
          
코드3)
여러 개의 요소를 저장할 수 있는 도구는 리스트와 사전이 있는데요. 둘 중 어떤 것을 쓰는지 크게 중요하지는 않지만 사전을 사용해볼게요. 

아래 리스트에 반복되는 요소가 있는지 확인하고 싶다고 생각해봅시다. 중복되는 요소를 담을 사전 elements_seen_so_far = {}가 있다고 가정하겠습니다.
[1, 2, 4, 2, 5, 3]
0 번 째 요소 1이 사전에 있는 key인지 확인합니다(이미 본 요소인지). 처음 보는 요소이기 때문에 사전에 추가해줍니다. 
(elements_seen_so_far[1] = True)
1 번 째 요소 2도 마찬가지로 사전에 추가합니다.
2 번 째 요소 4도 마찬가지로 사전에 추가합니다.
3 번 째 요소 2는 elements_seen_so_far에 이미 있는 key기 때문에 2를 리턴합니다.
시간 복잡도는 가능한 요소의 조합들을 다 보는는
O(n2)보다 효율적인 O(n)로 풀 수 있습니다.

def find_same_number(some_list):
    # 이미 나온 요소를 저장시켜줄 사전
    elements_seen_so_far = {}

    for element in some_list:
        # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
        if element in elements_seen_so_far:
            return element

        # 해당 요소를 사전에 저장시킨다
        elements_seen_so_far[element] = True

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

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
