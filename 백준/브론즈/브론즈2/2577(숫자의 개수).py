a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))
for i in range(10):
    print(result.count(str(i)))
    
str함수를 이용하여 숫자->문자변환 / list함수 활용하여 각각의 문자를 요소로 가지는 리스트로 변환.    
