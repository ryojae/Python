# #no.1
# print('no.1\n')
# coffee_100g=10000
# print('커피 원두 200g 가격: ',coffee_100g*2,'원',sep='')
# print(f'커피 원두 300g 가격: {coffee_100g*3}원')
# print(f'커피 원두 400g 가격: {coffee_100g*4}원')

# #no.2
# print('no.2\n')
# coffee=10000
# coffee += 10000
# print('커피 원두 200g 가격: ',coffee,'원',sep='')
# coffee += 10000
# print(f'커피 원두 300g 가격: {coffee}원')
# coffee += 10000
# print(f'커피 원두 400g 가격: {coffee}원')

# #no.3
# print('no.3\n')
# year = 2022; name = '코다'
# print('%d년 아카데미 영화제 작품상은 \"%s\"가 받았다'% (year, name))
# year = 2021; name ='노매브랜드'
# print('%d년 아카데미 영화제 작품상은 \"%s\"가 받았다'% (year, name))
# year = 202; name='기생충'
# print('%d년 아카데미 영화제 작품상은 \"%s\"가 받았다'% (year, name))

# #no.4
# print('no.4\n')
# coffee_100g=10000
# weight=200
# price=coffee_100g*weight/100
# print('커피 무게: %d, 가격: %d' % (weight, price))

# weight=300
# price=coffee_100g*weight/100
# print('커피 무게: %d, 가격: %d' % (weight, price))

# #no.5
# print('no.5\n')
# year = 2022; name = '코다'
# print(f'{year}년 아카데미 영화제 작품상은 \"{name}\"이다')
# year = 2021; name ='노매브랜드'
# print(f'{year}년 아카데미 영화제 작품상은 \"{name}\"이다')
# year = 202; name='기생충'
# print(f'{year}년 아카데미 영화제 작품상은 \"{name}\"이다')

# #no.6
# print('no.6\n')
# price_1kg=int(input('사과 1kg의 단가를 입력해주세요:'))
# weight=float(input('사과의 무게를 입력해주세요(kg 단위):'))
# price=price_1kg*weight
# print(f'사과 {weight}kg의 가격은 {price}입니다.')

# #no.7
# print('no.7\n')
# width, height=input('직사각형의 가로 길이와 세로 길이리를 입력해주세요:').split()
# width=float(width); height=float(height)
# area=width*height
# print(f'넓이는 {area}입니다.')

# #no.8
# print('no.8\n')
# celcius=float(input('섭씨 온도를 입력해주세요:'))
# F=celcius*9/5+32
# print(f'화씨 {F} 입니다.')

# #no.9
# garo, sero, height = input('직육면체의 가로, 세로, 높이를 입력해주세요:').split()
# garo=float(garo);sero=float(sero);height=float(height)
# volume= garo*sero*height
# print(f'부피는 {volume}입니다.')

# #no.10
# print('no.10\n')
# num1, num2, num3 = input('세개의 숫자를 입력해주세요:').split()
# num1 = float(num1); num2=float(num2);num3=float(num3)
# average=(num1+num2+num3)/3
# print(f'세 숫자의 평균은 {average}이다.')

# #no.11
# print('no.11\n')
# bottom, height= input('삼각형의 밑변과 높이를 입력해주세요:').split()
# area=bottom*height/2
# print(f'삼각형의 넓이는 {area}이다.')

# #no.12
# print('no.12\n')
# won,iyul,year=input('원금과 연이율 그리고 기간을 입력해주세요:').split()
# won=float(won); iyul=float(iyul); year=float(year)
# ija=won*iyul*year
# print(f'이자는 {ija}입니다.')

# #no.13
# print('no.13\n')
# sec=int(input('초 단위의 시간을 입력해주세요:'))
# hour=sec//3600
# min=(sec%3600)//60
# sec=(sec%3600)%60
# print(f'{hour}시 {min}분 {sec}초 이다.')

# #no.14
# print('no.14\n')
# won=float(input('원화를 입력해주세요:'))
# dollar, yuro, en= input('달러, 유로, 엔화의 환율을 입력해주세요:').split()
# dollar=float(dollar); yuro=float(yuro); en=float(en)
# do = dollar*won; yu= yuro*won; e=en*won
# print(f'{won}원은 {do}달러이고 {yu}유로이고 {e}엔이다.')