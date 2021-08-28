def merge_sort(my_list):
  #base case
  if len(my_list) < 2:
    return my_list
  
  #my_list를 반반씩 나눈다(divide)
  leftside = merge_sort(my_list[:len(my_list)//2])
  rightside = merge_sort(my_list[len(my_list)//2:])
  
  return merge(left_helft, right_half)


def merge_sort(my_list):
    # base case
    if len(my_list) < 2:
        return my_list

    # my_list를 반씩 나눈다(divide)
    left_half = merge_sort(my_list[:len(my_list)//2])    # 왼쪽 반
    right_half = merge_sort(my_list[len(my_list)//2:])   # 오른쪽 반

    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다
    # 위 알고리즘의 max()부분과 일치
    return merge(left_half, right_half) 
