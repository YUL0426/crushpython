def merge(list1, list2):
    i = 0
    j = 0
    #반복문을 위한 변수 두 개 설정
    
    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1과 list2를 돌면서 merged_list에 항목 정렬
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 항목이 있으면 정렬 리스트에 추가
    if i == len(list1):
        merged_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list
        
    
# 합병 정렬
def merge_sort(my_list):

    if len(my_list) < 2:
        return my_list
     #base케이스로, 리스트 크기가 1이라면 바로 반환
        
    mid = len(my_list)//2
    #중간값 설정(리스트를 반으로 나누기 위해 리스트 크기의 중간값을 변수로 선언해줍니다.)
    return merge(merge_sort(my_list[:mid]), merge_sort(my_list[mid:]))
    #merge의 역할은 나눠진 두 리스트의 요소를 비교하여 정렬하는 것이고 merge_sort의 역할은 하나의 리스트를 두 부분으로 나눈 후 정렬하는 것입니다.
    #참고로 이 부분은 재귀 함수의 recursive case와 같습니다.
    #recursive case with 위에서 작성한 merge함수
# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
