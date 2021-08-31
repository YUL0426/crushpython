미쳐버린 초안)
def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    # 사람이라면 : 1) 전체리스트를 보고 2) 항목하나하나 더해보며 3) search_sum이 나오는지 계산해본다
    for i in range(len(sorted_list)):
        for j in range(2, len(sorted_list)):
            if (i + j) == search_sum:
                return True
            else:
                return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))

잘한점)
for문을 두번  돌려 합같으면 바로 리턴한다는 점에서 답에 근사했음

못한점)
하지만
첫 째, 이중for문 중 j문 i가 1이라는 보장이 없으므로 i부터 시작했어야했고
둘 째, i와 j는 리스트를 돌며 몇 번째 리스트인지를 구하는 변수이므로 sorted_list[i] + sorted_list[j]로 풀었어야함

새로 알게 된 점)
친절하게 else문까지 쓸 필요없다. 그냥 바로 아님말고(return False)박기

두 번째 안) 문제에 있는 탐색에 집중해보자
#꼭 두개의 합, 세 개의 합이 search_sum을 구하게 할 수는 없다. 고로 sum_in_list를 계속 활용할 수 있어야 함
def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    # 사람이라면 : 1) 전체리스트를 보고 2) 항목하나하나 더해보며 3) search_sum이 나오는지 계산해본다 
    # 먼저 basecase
    if sorted_list < 2:
        if sorted_list[0] == search_sum:
            return True
        else:
            return False
    
    if sorted_list <

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))

모범답안) Brute Force 버전
def sum_in_list(search_sum, sorted_list):
    for i in range(len(sorted_list)):
        for j in range(i, len(sorted_list)):
            if sorted_list[i] + sorted_list[j] == search_sum:
                return True
    return False
시간복잡도)
그런데 인풋 리스트의 길이가 n이라고 할 때, Brute Force 접근법을 이용해서 문제를 풀면 시간 복잡도가 O(n&2)가 됩니다. 
지금은 괜찮지만 리스트가 길이가 커질수록 더 비효율적이겠네요.

*인풋 리스트가 정렬되었다는 점을 이용해서 문제를 해결할 수 있지 않을까요?

모범답안2) 이진탐색 버전
def sum_in_list(search_sum, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low < high:
        candidate_sum = sorted_list[low] + sorted_list[high]

        if candidate_sum == search_sum:  # 합이 찾으려는 숫자일 때
            return True

        if candidate_sum < search_sum:  # 합이 찾으려는 숫자보다 작을 때
            low += 1

        else:  # 합이 찾으려는 숫자보다 클 때
            high -= 1

    # 찾는 조합이 없기 때문에 False 리턴
    return False


# 테스트
print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))

새로 알게된 점) 
1, 파라미터로 받는 변수 재설정
