# #no.2
# def add(num1, num2, num3):
#     return num1 + num2 + num3
 
# print(add(2, 3, 5))
# print(add(2, num3 = 5, num2 = 3))
# # print(add(2, num3 = "5", num2 = "3"))
# print(add(2, num2 = 3, 5))
# print(add(num1 =2,num2=3,num3=5))
# print(add(num3=2,num1=3,num2=5))

# #no.3
# print(2, 3, sep = ",")

# #no.4
# num = 3
# def printNum3():
#     print(num)
#     num = 5
#     print(num)
# printNum3()

# #no.5
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)

# n=int(input('정수 한개를 입력해주세요:'))
# print(sum(n))

# #no.6
# import math
# def dew(humid,temperature):
#     d1 = math.log(humid / 100)
#     d2 = (17.62 * temperature) / (243.12 + temperature)
#     dew_point = (243.12 * (d1 + d2)) / (17.62 - (d1 + d2))
#     return dew_point
# h, t = map(int,input('습도와 온도를 입력해주세요:').split())
# print(f'이슬점은 {dew(h,t):.2f}입니다.')

# #no.7
# def PrintDate(year,month,day):
#     m=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
#        'August', 'September', 'October', 'November','December']
#     if month<=12 and year>0 and 0<day<=30 :
#         print('Year:',year)
#         print('Month:',m[month])
#         print('Day:',day)
#     else:
#         print('날짜를 잘못 입력하였습니다.')
# PrintDate(2022,8,1)
# PrintDate(2022,9,20)
# PrintDate(2022,3,3)

# #no.8
# def Count_word(s):
#     word=s.split()
#     return len(word)
# s=input('문자열을 입력해주세요:')
# print(Count_word(s))

# #no.10
# def getWord(s,num):
#     s=s.split()
#     return s[num-1]
# print(getWord('A beautiful day',1))
# print(getWord('A beautiful day',3))

# #no.11
# def yoon(year):
#     return year% 400 == 0 or (year%4 ==0 and year % 100 !=0)
# year = int(input('0보다 큰 정수 한개를 입력해주세요:'))
# if year <= 0:
#     print('잘못 입력했습니다.')
# else:
#     if yoon(year):
#         print('윤년입니다.')
#     else:
#         print('운년이 아닙니다.')

# #no.12
# def getSecondWord(s):
#     s = s.strip()
#     pos1=s.find(' ')
#     pos2=s.find('\t')
#     pos3=s.find('\n')
#     p1=max(pos1,pos2,pos3) +1
#     s2=s[p1:]
#     pos1=s2.find(' ')
#     pos2=s2.find('\t')
#     pos3=s2.find('\n')
#     p2=max(pos1,pos2,pos3)
#     if p2 ==-1:
#         p2 = len(s)
#     else:
#         p2 += p1
#     return s[p1:p2]
# s= input('두 개 이상의 단어가 있는 문자열을 입력해주세요:')
# print(getSecondWord(s))

# #no.13
# def CompareScores(score1, score2, score3, order = '내림차순'):
#     if order == '내림차순':
#         if score1 >= score2 and score1>=score3:
#             if score2>=score3:
#                 print(score1,score2,score3)
#             else:
#                 print(score1,score2,score3)
#         elif score2 >= score1 and score2 >= score3:
#             if score1>=score3:
#                 print(score2,score1,score3)
#             else:
#                 print(score2,score3,score1)
#         else:
#             if score1 >=score2:
#                 print(score3,score1,score2)
#             else:
#                 print(score3,score2,score1)
#     else:
#         if score1 < score2 and score1<score3:
#             if score2<score3:
#                 print(score1,score2,score3)
#             else:
#                 print(score1,score3,score2)
#         elif score2 < score1 and score2 < score3:
#             if score1<score3:
#                 print(score2,score3,score1)
#             else:
#                 print(score2,score1,score3)
#         else:
#             if score1 <score2:
#                 print(score3,score2,score1)
#             else:
#                 print(score3,score1,score2)

# order = input('오름차순과 내림 차순 중 하나를 골라주세요:')
# score1, score2, score3 = map(int, input('세명의 성적을 입력해주세요:').split())
# if order == '내림차순':
#     CompareScores(score1,score2,score3)
# else:
#     CompareScores(score1,score2,score3,order)

# #no.14
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)

# n=int(input('정수 한개를 입력해주세요:'))
# print(sum(n))

# #no.15
# def gcd(m,n):
#     if m==n:
#         return m
#     elif m>n:
#         return gcd(m-n,n)
#     else:
#         return gcd(m,n-m)
# print(gcd(12,4))
# print(gcd(12,18))

# #no.16
# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     return reverse_string(s[1:]) + s[0]

# input_string = "hello"
# reversed_string = reverse_string(input_string)
# print(f"Original: {input_string}")
# print(f"Reversed: {reversed_string}")

# #no.17
# def hello(*names):
#       for each in names: #names 내의 모든 요소들을 순서대로 참조하는 순환문
#             print('안녕, {}!'.format(each))
 
# hello('민정')
# hello('David','Veronica','Paul')
# hello('방탄소년단','블랙핑크')

#no.18
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n=int(input('정수 한개를 입력해주세요:'))
print(factorial(n))