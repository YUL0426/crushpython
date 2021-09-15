*)Bronze 1

코드1) 시간초과 뜸
num = int(input())
check = num
new_num = 0
temp = 0
count = 0
#사이클 길이 출력을 위한 변수
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)

코드저자의설명) 출처 : https://elrion018.tistory.com/39
깊이 생각할 것 없이 문제 내용을 충실히 반영하면 되는 문제였다. 
다만, '먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자릿수로 만들고, 각 자리의 숫자를 더한다.'라고 나와있는데 코드 작성 시 반영할 필요가 없다. 
예를 들어서 주어진 수가 10보다 작은 3이라고 가정하자. 10을 곱하지 않고 3을 그대로 사용했을 시 어차피 1의 자릿수이기에 더할 필요 없이 3을 그대로 사용한다. 
10을 곱해서 30으로 만들어 사용했을 시 각 자리의 수를 더하게 된다. 그래봐야 3+0 = 3 이므로 10을 곱하지 않은 이전 값과 동일하게 된다. 그러니 무시해주면 된다.
 이 문제는 // 연산자와 % 연산자를 잘 사용해야 하는 문제이다. 
a//b은 a를 b로 나눈 몫을 반환하게 된다.
a%b는 a를 b로 나눈 후 그 나머지를 반환하게 된다. 
// 연산과 % 연산에서 b를 10으로 두면 a의 10의 자리 숫자(10으로 나눈 몫은 결국 10의 자릿수이기 때문에)와 a의 1의 자리 숫자(10으로 나눈 다음 나머지는 결국 1의 자릿수이기 때문에)를 구할 수 있게 된다.

=>굳이 문자열로 숫자를 안받고 연산자를 잘 활용하여 문제를 풀 수 있다

코드2) 시간초과 뜸
num = int(input())
temp = num
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    temp = (b*10) + c

    cnt += 1
    if(temp == num):
        break

print(cnt)

코드3)내가 찾고있던 문자열을 활용한 코드
n = input()
num = n
cnt = 0

while 1:
    if len(num) == 1:
        #문자열의 길이가 1이라면
        num = "0" + num
        #문제에서 먼저 "주어진 수가 10보다 작다면 앞에 0을 붙여 두자리 수로 만들고"라는 조건이 있으므로
    plus = str(int(num[0]) + int(num[1]))
    num = num[-1] + plus[-1]
    cnt += 1
    if num == n:
        print(cnt)
        break
