내 답안)
def find_same_number(some_list, start, end):
    # 필요한 경우, start와 end를 옵셔널 파라미터로 만들어도 됩니다.
    # 코드를 쓰세요
    # 시간복잡도가 O(n)을 넘기면 안되므로 for문 사용불가
    # 파라미터로 start와 end를 받으므로 퀵정렬을 생각해보자
    # 리스트가 1개인 경우는 리스트 그대로 반환
    start=some_list[0]
    end=some_list[-1]
    if some_list < 2:
        return some_list
    elif some_list >= 2:
        #start와 end가 있는데 for문을 안돌리고 풀 수 잇나?
        for start in (len(some_list)):
            for end in (2, len(some_list)):
                #end가 for문을 돌며라고 생각했지만 돌 수가 있나 
                

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

모범답안)
def find_same_number(some_list, start = 1, end = None):
    if end == None:
        end = len(some_list)
    # end가 빈변수라면, some_list의 길이를 초기화시킴
    
    # 반복 요소를 찾으면 리턴한다
    if start == end:
        return start
    #여기까지했다
    
    # 중간 지점을 구한다
    mid = (start + end) // 2
    #이건 못했다
    # 왼쪽 범위의 숫자를 센다. 오른쪽은 리스트 길이에서 왼쪽 길이를 빼면 되기 때문에 세지 않는다
    left_count = 0

    for element in some_list:
        if start <= element and element <= mid:
            left_count += 1
            
    # 왼쪽과 오른쪽 범위중 과반 수 이상의 숫자가 있는 범위 내에서 탐색을 다시한다
    if left_count > mid - start + 1:
        return find_same_number(some_list, start, mid)

    return find_same_number(some_list, mid + 1, end)

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

시간복잡도)
인풋 리스트의 길이를 n이라고 했을 때, 탐색 범위를 줄일 때마다 리스트의 모든 요소 n개를 돌면서 두 개의 범위 안에 있는 자연수의 갯수를 세고 있습니다.
한 번 리스트를 돌 때마다 시간 복잡도는 O(n)입니다.

범위의 크기는 n/2에서 시작해서 계속 반으로 줄어듭니다. 최악의 경우 범위가 자연수 하나가 되는 데까지 O(lg(n))가 걸리죠.

범위가 줄어들 때마다 O(n)의 작업을 하고, 범위는 최악의 경우 총  O(lg(n))번 줄어들기 때문에 최종 시간 복잡도는 O(nlg(n))이 됩니다.

잘한점)
#start와 end를 파라미터로 받는데, 현재 print에 전해줄 값이 없으므로 start와 end값을 정해준건 잘했다

못한점))
 # 중간 지점을 구한다
    mid = (start + end) // 2
    #이건 못했다
    
새로 알게된 점)
6.2 빈 변수 만들기
변수를 만들 때 x = 10과 같이 할당할 값을 지정해주었습니다. 그럼 값이 들어있지 않는 변수는 만들 수 없을까요?

값이 들어있지 않은 빈 변수를 만들려면 None을 할당해주면 됩니다.

>>> x = None
>>> x
변수의 값을 출력하면 아무 것도 나오지 않습니다. 이제 print로 출력해봅니다.

>>> print(x)
None
print로 변수 x의 값을 출력해보면 None이 나옵니다. 파이썬에서 None은 아무것도 없다는 것을 나타내는 자료형입니다. 보통 다른 언어에서는 널(null)이라고 표현합니다.
