#no.1
# def yoon(year):
#     return year% 400 == 0 or (year%4 ==0 and year % 100 !=0)
# year = int(input('0보다 큰 정수 한개를 입력해주세요:'))
# if year <= 0:
#     print('잘못 입력했습니다.')
# else:
#     s=yoon(year)
#     if s:
#         print('윤년입니다.')
#     else:
#         print('운년이 아닙니다.')

# #no.2
# def second_word(s):
#     s=s.strip()
#     word = s.split()
#     return word[1]

# s = input('두 개 이상의 단어가 있는 문자열을 입력해주세요:')
# word = second_word(s)
# print(word)

# #no.3
# def CompareScores(score1, score2, score3, order = True):
#     if order:
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
#                 pint(score3,score2,score1)
#     else:
#         if score1 < score2 and score1<score3:
#             if score2<score3:
#                 print(score1,score2,score3)
#             else:
#                 print(score1,score2,score3)
#         elif score2 < score1 and score2 < score3:
#             if score1<score3:
#                 print(score2,score1,score3)
#             else:
#                 print(score2,score3,score1)
#         else:
#             if score1 <score2:
#                 print(score3,score1,score2)
#             else:
#                 pint(score3,score2,score1)

# print('내림차순')
# CompareScores(85,80,90)
# print('오름차순')
# CompareScores(85,80,90,False)

# #no.4
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)

# n=int(input('정수 한개를 입력해주세요:'))
# print(sum(n))

# #no.5
# def add_numbers(n1,n2):
#     return n1+n2
# n1,n2 =map(int,input('두 개의 정수를 입력해주세요:').split())
# result = add_numbers(n1,n2)
# print(result)

# #no.5-1
# def revers(s):
#     return s[::-1]
# s=input('문자열을 입력해주세요:')
# print(revers(s))

# #no.6
# def Upper(s):
#     return s[0].upper()+s[1:]
# s = input('문자열을 입력해주세요:')
# print(Upper(s))

# #no.7
# def holjjak(s):
#     print(len(s))
#     if len(s) % 2 == 0:
#         return '짝수입니다'
#     else:
#         return '홀수입니다'
# s = input('문자열을 입력해주세요:')
# print(holjjak(s))

# #no.8
# def long(s1,s2):
#     if len(s1)>len(s2):
#         return s1
#     elif len(s1)<len(s2):
#         return s2
#     else:
#         return '길이가 같습니다.'
# s1 = input('첫번째 문자열을 입력해주세요:')
# s2 = input('두번째 문자열을 입력해주세요:')
# print(long(s1,s2))

# #no.9
# def Count(s, char):
#     return s.count(char)
# s=input('문자열을 입력해주세요:')
# char = input('특정문자를 입력해주세요:')
# print(f'"{char}"문자의 개수:',Count(s,char))

# #no.10
# def change(s):
#     return s.swapcase()
# s=input('문자열:')
# print(change(s))

# #no.11
# def classify(n):
#     if n > 0:
#         return '양수입니다.'
#     elif n==0:
#         return '0입니다.'
#     else:
#         return '음수입니다.'
# n=int(input('숫자:'))
# print(classify(n))

# #no.12
# def in_hundread(n):
#     if 1<=n<=100:
#         return '1과 100 사이에 있다.'
#     else:
#         return '1과 100 사이에 없다.'
# n=int(input('숫자'))
# print(in_hundread(n))

# #no.13
# def sachik(n1,n2,s):
#     if s == '+':
#         return n1+n2
#     elif s=='-':
#         return n1-n2
#     elif s=='*':
#         return n1*n2
#     elif s=='/':
#         return n1/n2
#     else:
#         return '잘못입력했습니다.'
# n1=int(input('첫 번째 숫자를 입력하세요:'))
# n2=int(input('두 번째 숫자를 입력하세요:'))
# s=input('수행할 연산을 입력하세요(+,_,*,/):')
# print(sachik(n1,n2,s))

# #no.14
# def sumaverage(n1,n2,n3):
#     sum = n1+ n2 +n3
#     average = sum/3
#     if average >=50:
#         return sum, average, '평균이 50이상입니다.'
#     else:
#         return sum, average, '평균이 50미만입니다.'
# n1,n2,n3=map(int,input('세개의 숫자를 입력해주세요:').split())
# total, avg, msg = sumaverage(n1,n2,n3)
# print(f'합: {total}, 평균: {avg}, 메시지: {msg}')

# #no.15
# import re
# def extract(s):
#     numbers= re.findall(r'\d+',s)
#     for i in range(0,len(numbers))
# print(numbers)