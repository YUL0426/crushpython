코드1) 시간복잡도O(y)
def power(x, y):
    total = 1
    
    # x를 y번 곱해 준다
    for i in range(y):
        total *= x
    
    return total
  
코드2) 시간복잡도 o(logy)
def power(x, y):
    if y == 1:
        return x  
    if y%2 == 0:
        return power(x*x, y/2)
    else:
        return x * power(x*x, (y-1)/2)
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
