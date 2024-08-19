# #no.1
# z1=4+3j; z2=2-5j
# print(f'({z1})+({z2})=({z1+z2})')

# #no.2
# name = 'David'
# age = 30
# print(f'My name is {name} and I am {age} years old.')
# print('My name is {name} and I am {age} years old.'.format(name= name, age= age))

# #no.3
# num=int(input('6 자리가 넘는 정수를 입력해주세요:'))
# divide_num=1000
# print('%d 을(를) %d 으로 나눈 결과는 %.2f 입니다.' %(num, divide_num, num/divide_num))

# #no.4
# for i in range (0,7):
#     if i<=3:
#         for j in range(0,i*4+1):
#             print('*',end='')
#     else:
#         for j in range(i*4,25):
#             print('*',end='')
#     print('\n')

# #no.5
# won = int(input('원금을 입력하세요:'))
# ija_year = int(input('연 이자율을 입력하세요(%):'))
# year = int(input('기간을 입력하세요:'))

# ija_month=ija_year/12/100
# amount=won*(1+ija_month)**(year*12)

# print(f'원금 {won}원, 연 이자율 {ija_year}%, 기간 {year}년일 때 복리는 {amount:.3f}원입니다.')

# #no.6
# battery=[30, 50, 20, 80, 10]
# battery_min=100
# for i in range(0,5):
#     if battery_min>battery[i]:
#         battery_min=battery[i]
#         min_index=i
# print(f'배터리셀의 잔여 용량 중 가장 적은 셀의 인덱스는 {min_index} 입니다.')