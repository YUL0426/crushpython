코드)
alphabet_list=['a','b','c','d','e','f','g','h','i','j']

print(alphabet_list[0:5])
print(alphabet_list[4:])
#4번째 인덱스부터 끝까지
print(alphabet_list[1:])
#첫번째인덱스 부터 끝까지
print(alphabet_list[:1])
#첫번째 인덱스 전까지
print(alphabet_list[:4])
#4번째 인덱스 전까지

*출력결과
['a', 'b', 'c', 'd', 'e']
['e', 'f', 'g', 'h', 'i', 'j']
['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
['a']
['a', 'b', 'c', 'd']
