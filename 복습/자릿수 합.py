내 코드)
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
   #basecase
   if n < 10:
       return n
    #recursive case
    #파라미터로 받은 n의 자릿수를 안다면,,, 1000,100,10과같이
    #계속 나눈 몫끼리 더하면 되겠지만 자릿수를 모른다면..?
    #
    if n > 10:
        return sum_digits
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

모범답안)
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # base case 
    if n < 10:
        return n
    #recursive case 
    return (n % 10) + sum_digits(n //10)
    #n이 한 자릿수일 경우에는 바로 답을 알고 리턴했지만, n이 한 자릿수보다 큰 경우에는 바로 답을 구하지 못하기 때문에 부분 문제를 풀어야 함.
    #예를 들어 n이 12345인 경우를 생각해 봅시다. 12345의 각 자릿수의 합을 구하기 위해서, 우리가 풀어야 할 부분 문제는 무엇일까요?
    #1234512345의 자릿수 합을 구하기 위해서는, 가장 마지막 자릿수인 55에 12341234의 자릿수 합을 더해주면 되는데요. 1234의 자릿수 합을 구하는 문제는 많이 익숙한 형태입니다.
    #1234의 자릿수 합을 구하는 것은 sum_digits(1234)입니다. 바로 우리가 찾던 “같은 형태의 더 작은 부분 문제"인 거죠.
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

잘한점)
1, basecase설정을 잘했다

못한점)
1, recursivecase를 잘 못구함

시간복잡도)
인풋 n의 자릿수 개수를 d로 표현하겠습니다. 예를 들어 nn이 15273이면 d는 5입니다.
우선 sum_digits 함수의 base case 부분은 O(1), n % 10도 마찬가지다. 그럼 sum_digits가 재귀적으로 몇 번 호출되는지만 알면 되겠네요.
따라서 sum_digits는 약 d번 호출되는 셈이죠.

sum_digits의 시간 복잡도는 O(d)입니다.
