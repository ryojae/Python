# #no.3
# tem, hum = 26, 71
# if tem >=25:
#     if hum>=70:
#         print('에어컨을 켠다.')

# #no.4
# num = int(input('정수를 입력해주세요:'))
# if num >=10:
#     print('10이상입니다.')
# elif num>=5:
#     print('5이상 10미만입니다.')
# else:
#     print('5미만입니다.')

# #no.5
# if score >= 90:
#     print('A')
# elif score >=80:
#     print('B')
# elif score >=70:
#     print('C')
# else:
#     print('D')

# #no.7
# if 'o' in 'python':
#     print('o')
# else:
#     print('x')

# if not 27%3:
#     print('27은 3의 배수이다.')
# else:
#     print('27은 3의 배수가 아니다.')

# #no.8
# year, month, day = input('년/월/일을 정수 값으로 입력해주세요:').split()
# year, month, day=int(year), int(month), int(day)
# if month >12 or month <= 0:
#     print('없는 달입니다.')
# elif month == 2:
#     if day>28 or day<=0:
#         print('없는 날입니다.')
#     else:
#         print(f'{year}년 {month}월 {day}일은 적절한 날입니다.')
# elif month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
#     if day>31 or day<=0:
#         print('없는 날입니다.')
#     else:
#         print(f'{year}년 {month}월 {day}일은 적절한 날입니다.')
# else:
#     if day>30 or day<=0:
#         print('없는 날입니다.')
#     else:
#         print(f'{year}년 {month}월 {day}일은 적절한 날입니다.')

# #no.9
# time = float(input('근무시간을 입력해주세요:'))
# pay =12000
# if time >= 40:
#     print('급여는',time*pay*1.5)
# else:
#     print('급여는',time*pay)

# #no.10
# weight = float(input('우편물의 무게를 입력해주세요(g):'))
# if weight>50:
#     print('우체국에 문의하십시오.')
# elif weight>25:
#     print('우편요금은 450원입니다.')
# elif weight > 5:
#     print('우편요금은 430원입니다.')
# elif weight > 0:
#     print('우편요금은 400원입니다.')
# else:
#     print('잘못 입력하셨습니다.')

# #no.11
# ta = float(input('건구 온도를 입력해주세요:'))
# tw = float(input('습구 온도를 입력해주세요:'))
# Discomfort=(ta+tw)*0.72+40.6
# if Discomfort >=80:
#     print('모든 사람이 불쾌감을 느낌')
# elif Discomfort >=75:
#     print('반 정도의 사람이 불쾌감을 느낌')
# elif Discomfort >=68:
#     print('불쾌감을 나타내기 시작함')
# else:
#     print('모든 사람이 쾌적함을 느낌')

# #no.12
# a, b, c = input('a, b, c 값을 입력해주세요:').split()
# a, b, c = float(a), float(b), float(c)
# D= b**2-4*a*c
# if D >0:
#     print('해는 실수이고 2개의 다른 값이 존재함')
# elif D==0:
#     print('해는 실수이고 1개 값만 존재함')
# else:
#     print('해는 복소수이고 2개의 다른 값이 존재함')

# #no.13
# a, b, c = input('a, b, c 값을 입력해주세요(ax+by+c=0):').split()
# p1, p2 = input('점의 위치를 입력해주세여:').split()
# a, b, c, p1, p2= float(a), float(b), float(c), float(p1), float(p2)
# dist=(a*p1+b*p2+c)/((a**2+b**2)**(1/2))
# if dist <0:
#     dist *= -1
#     print(f'직선 {a}x+{b}y+{c}=0과 점 사이의 거리는 {dist}입니다.')
# else:
#     print(f'직선 {a}x+{b}y+{c}=0과 점 사이의 거리는 {dist}입니다.')

# #no.14
# s1, s2 = input('두 개의 직선의 기울기를 입력해주세요:').split()
# s1, s2 = float(s1), float(s2)
# if (s1 * s2) == -1:
#     print('두 직선은 직교한다.')
# elif s1 == s2:
#     print('두 직선은 평행한다.')
# else:
#     print('두 직선은 평행도 아니고 직교도 아닌 각을 이룬다.')

# #no.15
# seat=input('구매할 좌석의 종류를 입력해주세요(VIP, S, A, B):')
# seat=seat.upper()
# if seat=='VIP':
#     print('VIP 좌석의 경우 가격은 150000원입니다.')
# elif seat == 'S':
#     print('S 좌석의 경우 가격은 110000원입니다.')
# elif seat =='A':
#     print("A 좌석의 경우 가격은 90000원입니다.")
# elif seat == 'B':
#     print('B 좌석의 경우 가격은 70000원입니다.')
# else:
#     print('잘못 입력되었습니다.')

# #no.16
# import random
# num=[random.randrange(1,99),random.randrange(1,99),random.randrange(1,99)]
# max=0
# for i in range (0, len(num)-1):
#     if max<num[i]:
#         max=num[i]
# print(f'{num}중 가장 큰 수는 {max}입니다.')

# #no.17
# num = int(input('정수 하나를 입력해주세요:'))
# state = 0
# for i in range(2, num):
#     if num % i ==0:
#         state = 1

# if state == 0:
#     print(f'{num}은 소수입니다.')
# else:
#     print(f'{num}은 소수가 아닙니다.')

# #no.18
# h, w= input('당신의 키(cm)와 몸무게(kg)는?').split()
# h, w= float(h),float(w)
# print(f'키: {h:.1f}(cm), 몸무게: {w:.1f}(kg)')
# BMI=w/(h/100)**2
# if 40<=BMI :
#     print(f'BMI: {BMI:.1f} 고도비만')
# elif 35<= BMI <40:
#     print(f'BMI: {BMI:.1f} 중도비만')
# elif 30<=BMI<35:
#     print(f'BMI: {BMI}:.1f 비만')
# elif 25<=BMI<=30:
#     print(f'BMI: {BMI:.1f} 과체중')
# elif 18.5<=BMI<=25:
#     print(f'BMI: {BMI:.1f} 정상')
# elif BMI<=18.5:
#     print(f'BMI: {BMI:.1f} 저체중')

# #no.19
# interest = input('파이썬에 대한 관심도를 입력해주세요[없음, 조금, 보통, 많음, 매우 많음]:')
# if interest == '보통' or interest == '많음' or interest == '매우 많음':
#     efforts = input('기여도를 입력해주세요[상, 중, 하]:')
#     if efforts == '상':
#         print('예비 파이썬 고수')
#     elif efforts == '중':
#         print('에비 파이썬 중수')
#     elif efforts == '하':
#         print('노력 필요')
# elif interest == '없음' or interest == '조금':
#     print('파이썬에 대해 관심을 가져보세요.')
    
# #3차시 다이아몬드 그리기
# for i in range(0,7):
#     if i<4:
#         for j in range(3-i,0,-1):
#             print(' ',end='')
#         print('*',end='')
#         for j in range(0,i*2):
#             print('*',end='')
#     else:
#         for j in range(7-i,4):
#             print(' ',end='')
#         print('*',end='')
#         for j in range(i*2,12):
#             print('*',end='')        

#     print('\n')