x = int(input("2진수로 바꿀 숫자를 입력하세요:"))

result = ''             // slicing이 가능하므로 string으로

while True:
    if x % 2 == 0:
        result += '0'
    else:
        result += '1'
    x = x // 2
    if x == 1 or x == 0:
        result += str(x)
        print(result[::-1])
        break
        
#자릿수 더하기
def hap(n):
    if n == '':
        return 0
    else:
        return int(n[0]) + int(hap(n[1:]))

print(hap('2231'))
