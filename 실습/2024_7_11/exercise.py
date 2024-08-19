# #if문
# s = input('단어 한 개를 입력하세요:')
# if s == 'hello':
#     print('사용자가 입력한 단어가 hello 입니다.')

# #no.1
# num = int(input('정수를 한개 입력해주세요:'))
# if num >= 5:
#     print('5보다 크거나 같습니다.')
# if num <5:
#     print('5보다 작습니다.')

# #no.2
# num = int(input('정수를 한 개 입력해주세요:'))
# if num>=10:
#     print('10보다 크거나 같습니다.')
# else:
#     if num>=5:
#         print('5보다 크거나 같지만 10보다 작습니다.')
#     else:
#         print('5보다 작습니다.')

# #no.3
# seat=input('구매할 좌석의 종류를 입력해주세요(VIP, S, A, B):')
# if seat=='VIP':
#     print('VIP 좌석의 경우 가격은 150000원입니다.')
# elif seat == 'S':
#     print('S 좌석의 경우 가격은 110000원입니다.')
# elif seat =='A':
#     print("A 좌석의 경우 가격은 90000원입니다.")
# elif seat == 'B':
#     print('B 좌석의 경우 가격은 70000원입니다.')
# else:
#     print('표에 없는 좌석이 입력되었습니다. 다시 입력해주세요.')

# #no.4
# tem, hum = input('온도와 습도를 입력해주세요:').split()
# tem=int(tem); hum=int(hum)
# if tem>=25 and hum >=70:
#     print('냉방 모드로 에어컨 작동')
# elif tem>=25 and hum < 70:
#     print('제습 모드로 에어컨 작동')
# else: print('에어컨 작동 중지')

# #no.5
# age = int(input('나이를 입력해주세요:'))
# if age>=20:
#     print('성인입니다.')
# else:
#     print('미성년자입니다.`')

# #no.6
# num=int(input('정수를 입력해주세요:'))
# if num%2:
#     print('홀수입니다.')
# else:
#     print('짝수입니다.')

# #no.7
# num= int(input('(점수를 입력하세요 (0-100) 사이의 정수:'))
# if num>90:
#     print('A')
# elif num>80:
#     print('B')
# elif num>70:
#     print('C')
# else:
#     print('F')

# #no.8
# celcius = float(input('섭씨 온도를 입력해주세요:'))
# if celcius<=0:
#     print('고체')
# elif celcius<100:
#     print('액체')
# else:
#     print('기체')

# #no.9
# grade = int(input('학년을 입력해주세요:'))
# if grade == 1:
#     print('초')
# elif grade ==2:
#     print('중')
# elif grade ==3:
#     print('고')
# else:
#     print('대')

# #no.10
# line1,line2,line3 = input('세변의 길이를 입력해주세요:').split()
# line1=float(line1); line2=int(line2); line3=int(line3)
# if line1==line2:
#     if line1 != line3:
#         print('이등변')
#     else:
#         print('정삼각형')
# elif line2 == line3:
#     print('이등변')
# else:
#     if line1 == line3:
#         print('이등변')
#     else:
#         print('일반')

# #no.11
# num1, num2 = input('두 개의 숫자를 입력해주세요:').split()
# num1 = int(num1); num2= int(num2)
# if not num1%num2:
#     print('첫번째 숫자는 두번째 숫자의 배수이다.')
# if (num1+num2)>=100:
#     print(num1+num2)

# #no.12
# str1 = input('첫번째 문자열을 입력해주세요:')
# str2= input('두번째 문자열을 입력해주세요:')
# if str1 == str2:
#     print('두개의 문자열이 같다.')
# if len(str1)==len(str2):
#     print('두개의 문자열 길이가 같다.')

# #no.13
# age, cureer= input('나이와 운전 경력을 입력해주세요:').split()
# if int(age)>=25 and int(cureer)>= 2:
#     print('가능')
# else:
#     print('불가능')

# #no.14
# price = int(input('구매 금액을 입력해주세요:'))
# if price>=100000:
#     print(price*0.9)
# elif price>=50000:
#     print(price*0.95)
# else:
#     print(price)

# #no.15
# password = input('8자 이상의 패스워드를 입력해주세요:')
# num=0; str2=0
# for char in password:
#     if char.isdigit():
#         num=1
#     else:
#         str2=1

# if num and str2:
#     print('숫자와 문자를 모두 포함')
# elif num and str2 ==0:
#     print('숫자만 있음')
# elif str2 and num ==0:
#     print('문자만 있음')

# #no.16
# age, sex = input('나이와 성별을 입력해주세요:').split()
# age = int(age)
# if age >20:
#     if sex == '남':
#         print('health')
#     elif sex =='여':
#         print('yoga')
#     else:
#         print('error')
# else: print('공부')

# #no.17
# time = int(input('주간 근무 시간을 입력해주세요:'))
# if time >= 40:
#     print(time*10000*1.5)
# else:
#     print(time*10000)

# #no.18
# password = input('8자리 이상의 비밀번호를 입력하세요:')
# num=0;big=0;small=0
# for char in password:
#     if char.isdigit():
#         num=1
#     elif char.isupper():
#         big=1
#     else:
#         small =1
# if num and big and small:
#     print('모두 포함')