210918코드)
n = int(input())
cnt = 0

for i in range(1, n+1):
 if i <= 99:
  cnt += 1

 else:
  nums = list(map(int, str(i)))
  if nums[0] - nums[1] == nums[1] - nums[2]:
   cnt += 1

print(cnt)

210914코드)
num = int(input())
hansu = 0

for n in range(1, num + 1):
    if n <= 99:  # 1부터 99까지는 모두 한수
        hansu += 1

    else:
        nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2]:  # 등차수열 확인
            hansu += 1

print(hansu)

진짜 알고 싶었던 숫자를 자릿수대로 분리하는 법을 알았다.
nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
