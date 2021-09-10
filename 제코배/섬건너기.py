import datetime

오늘시간 = datetime.datetime.today()
대기인원 = 14000605

def solution(대기인원):
    일년일수 = 0
    for i in range(10, 0, -1):
        일년일수 += 2**i
    년 = (대기인원 // 1200) // 일년일수
    남은일수 = (대기인원 // 1200) % 일년일수

    월별일수누적값 = 0
    월 = 0
    for i in range(10, 0, -1):
        차감일 = 월별일수누적값
        월별일수누적값 += 2**i
        월 += 1
        if 월별일수누적값 > 남은일수:
            break

    일 = 남은일수 - 차감일
    최종남은인원 = 대기인원 % 1200
    시 = 최종남은인원 // 100 + 9

    출발분 = [25, 40, 55, 70, 85, 100]
    해당시간에남은인원 = 최종남은인원 % 100 + 1
    for i in 출발분:
        if i > 해당시간에남은인원:
            분 = 출발분.index(i) * 10
            break
    if 최종남은인원 % 100 ==99:
        시 += 1
        분 = 0

    if(오늘시간.minute + 분 > 60):
        분 = (오늘시간.minute + 분) - 60
        시 += 1

    return f'{년} 년 {월}월 {일}일 {시}시 {분}분 출발'
solution(대기인원)
