# #no.5
# num = 13
# if num >10 and num % 5 == 3 and num // 4 ==3:
#     print('Hello')

# #no.7
# num =int(input('정수를 입력해주세요:'))
# state = num % 2
# if state:
#     print('홀수입니다.')
# else:
#     print('짝수입니다.')

# #no.8
# a, b, c, d= map(int,input('정수 네개를 입력해주세요:').split())
# if a > b and a>c and a>d:
#     max =a
# elif b>a and b>c and b>d:
#     max=b
# elif c>a and c>b and c>d:
#     max=c
# elif d>a and d>b and d>c:
#     max=d
# print('가장 큰수는 %d입니다.' % max)

# #no.9
# a, b, c, d= map(int,input('정수 네개를 입력해주세요:').split())
# num = [a,b,c,d]
# for i in range (0, len(num)-1):
#     for j in range (0,len(num)-1-i):
#         if num[j]<num[j+1]:
#             t=num[j]
#             num[j]=num[j+1]
#             num[j+1]=t     
# print(f'큰 순서로 정렬하면 {num} 입니다.')

# #no.10
# year = int(input('연도를 입력하세요:'))
# month = int(input('월을 입력해주세요:'))

# if year > 0 and 1<=month<=12:
#     print('True')
# else:
#     print('False')

# #no.11
# num=int(input('4자리 정수를 입력하시오:'))
# if num<1000 or num>9999:
#     print('잘못 입력하셨습니다. 4자리 연도를 입력해주세요.')
# else:
#     first=num//100
#     last = num%100
#     print('첫 두자리 : ',first)
#     print('마지막 두자리 : ',last)

#no.12
import math
year, M, D = map(int,input('연도, 월, 날짜를 입력해주세요:').split())
Y1=year%100; Y2=year//100
date = (Y1+math.floor(Y1/4)-2*Y2+math.floor(Y2/4)+math.floor((13*(M+1))/5)+D)%7
if date ==1:
    today = '일요일'
elif date ==2:
    today = '월요일'
elif date ==3:
    today ='화요일'
elif date ==4:
    today = '수요일'
elif date ==5:
    today ='목요일'
elif date ==6:
    today = '금요일'
else:
    today ='토요일'
print(f'{year}년 {M}월 {D}일은 {today}입니다.')