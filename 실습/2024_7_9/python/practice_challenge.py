# #no.1
# num=float(input('실수를 입력하세요:'))
# print(f'반올림 결과: {num:.1f}')

# #no.2
# num=float(input('실수를 입력하세요:'))
# print('반올림 결과:', round(num,1))

# #no.3
# import math
# x1,y1=1,2
# rad=math.radians(30)
# x2=x1+15*math.cos(rad)
# y2=y1+15*math.sin(rad)
# print(f'결과 좌표: ({x2:.2f},{y2:.2f})')

# #no.4
# x1, y1=1, 2
# x2, y2=4,6
# distance=((x2-x1)**2+(y2-y1)**2)**(1/2)
# print(f'거리: {distance:.2f}')

# #no.5
# def sum_numbers_in_variables(*args):
#     total_sum = 0
#     for value in args: #for 반복문
#         if isinstance(value, str) and value.isdigit():
#             total_sum += int(value)
#     return total_sum

# var1 = '123'; var2='abc'; var3='456';var4=789
# print(sum_numbers_in_variables(var1,var2,var3,var4))

# #no.7
# import calendar
# def print_month_calendar(year, month):
#     # 요일 이름
#     days = ["월", "화", "수", "목", "금", "토", "일"]
#     # 해당 월의 1일이 시작하는 요일 (0: Monday, 6: Sunday)
#     start_day = calendar.weekday(year, month, 1)
#     # 해당 월의 전체 일수
#     total_days = calendar.monthrange(year, month)[1]
#     # 달력 출력
#     print(f"{month} {year}")
#     print(" ".join(days))
#     # 첫 주 앞쪽 공백 출력
#     print("   " * start_day, end="")
#     # 날짜 출력
#     day = 1
#     while day <= total_days:
#         print(f"{day:2} ", end="")
#         start_day += 1
#         if start_day == 7:  # 한 주가 끝나면 줄바꿈
#             start_day = 0
#             print()
#         day += 1
#     # 마지막 줄 바꿈
#     if start_day != 0:
#         print()
# # 사용자 입력 받기
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# # 달력 출력
# print_month_calendar(year, month)

# #no.8
# #시간 입력 받기
# hour,minute=input('시간을 입력하세요 (예: 2시간 30분 -> 2 30):').split()

# #정수형 변환
# hour=int(hour); minute=int(minute)

# #분으로 변환
# total_minute=hour*60+minute

# #출력
# print(f'총 {total_minute}분 입니다.')

# #no.9
# #문자열에서 합 구하는 함수 선언
# def sum_in_sentence(sentence):
#     total_sum=0
#     for char in sentence:
#         if char.isdigit():
#             total_sum += int(char)
#     return total_sum
        

# #문자열 입력
# sentence=input('문자열을 입력해주세요:')

# #결과 출력
# result=sum_in_sentence(sentence)
# print('모든 숫자의 합:',result)

#no.10
#변수 선언
total_sum=0

#반복문 1~100
for i in range(1,101):
    #조건문 3의 배수 또는 5의 배수
    if i %3==0 or i%5==0:
        total_sum +=i
        
#결과 출력
print('결과:',total_sum)

