# #no.1
# radius =5
# area = radius * radius * 3.14
# print('반지름이 %d인 원의 면적은 %.3f입니다.' % (radius, area))

# #no.6
# print('%8f' % 3.14)

# #no.7
# print('%10s' % '한글')

# #no.8
# address='서울시 종로구 홍지문 2 길'
# temperature = 24
# print(f'지역: {address}, 온도: {temperature}')

# #no.9
# p=3.1415
# print(f'원주율 * 2 = {p*2:.2f}입니다.')

# #no.10
# x1 = 1.23; x2 = 12.3; x3 = 123.456
# print(f'{x1: ^10.2f}\n{x2:^9.1f}\n{x3:^9.3f}')

# #no.11
# radius = float(input('원의 반지름을 입력해주세요:'))
# area = 3.14 * radius**2
# print(f'반지름: {radius}, 면적: {area}')

# #no.12
# import math
# RH, T = input('습도와 온도를 입력해주세요:').split()
# RH=int(RH); T=int(T)
# print(RH,T)
# Dew_point=243.12*(math.log(RH/100)+17.62*T/(243.12+T)) / (17.62-math.log(RH/100)+17.62*T/(243.12+T))
# print(f'이슬점은 {Dew_point}도입니다.')

#no.13
m1=5.972*10**24 #지구 질량
m2=7.36*10**22 #달 질량
dist=384400000 #지구와 달의 거리
G=6.674*10**(-11)
F= G*(m1*m2)/dist**2
print(f'달과 지구 사이의 만유인력은 {F}이다.')

# #no.14
# coffee_100g=10000
# coffee_weight=[200, 300, 400]
# for i in range(0,3):
#     print(f'커피 원두 {coffee_weight[i]}g 가격: {int(coffee_100g*coffee_weight[i]/100)}원')

# #no.15
# coffee_100g = 10000
# coffee_weight_base=100
# coffee_weight = coffee_weight_base
# price=coffee_100g
# for i in range(0,3):
#     coffee_weight += coffee_weight_base
#     price += coffee_100g
#     print(f'커피 원두 {coffee_weight}g 가격: {int(coffee_100g*coffee_weight/100)}원')

# #no.16
# year = 2022; name = '코다'
# print(f'{year}년 아카데미 영화제 작품상은 \"{name}\"이다')
# year = 2021; name ='노매브랜드'
# print(f'{year}년 아카데미 영화제 작품상은 \"{name}\"이다')
# year = 202; name='기생충'
# print(f'{year}년 아카데미 영화제 작품상은 \"{name}\"이다')

# #no.17
# coffee_100g=10000
# weight=200
# print('커피 원두 %dg 가격: %d원' %(weight,coffee_100g*weight/100))
# weight=300
# print('커피 원두 %dg 가격: %d원' %(weight,coffee_100g*weight/100))

# #no.18
# coffee_100g=10000
# weight=200
# print(f'커피 원두 {weight}g 가격: {int(coffee_100g*weight/100)}원')
# weight=300
# print(f'커피 원두 {weight}g 가격: {int(coffee_100g*weight/100)}원')

# #no.19
# weight, danga = input('원두 무게와 커피 원두 100g의 단가를 입력해주세요:').split()
# weight=float(weight); danga=int(danga)
# print(f'커피 원두 {weight}g의 가격은 {danga*weight/100}원 입니다.')

# #no.20
# hello ='world'
# print(f'{hello:^11}')
# print(f"{hello:*^11}")
# big_num =1234567890
# print(f'{big_num:,}')
# num=2343552.6516251625
# print(f'{num:,.3f}')