# #no.1
# n='문자열의 길이를 확인해요...'.count('.')
# print(n)

# #no.2
# s='우리나라'
# if s.find('나') >0:
#     print(f'{s}에 \'나\'가 포함이 됩니다.')

# #no.3
# #(1)
# print('What a day!'.rindex('a'))
# #(2)
# print('What a day!'.rindex('a',0,5))

# #no.4
# s='Hello world'
# print(s[0:2])
# print(s[:-1])
# print(s[:])

# #no.5
# print('가helloh가나'.strip('가h나'))

# #no.8
# s=input('세 개 이상의 단어로 구성된 문자열을 입력하세요:').split()
# print('두 번째 단어는',s[1])

# #no.9
# s='Hello World'
# n=s.find(' ')
# print(s.index('o',n,len(s)))

# #no.10
# s='123456789'
# hol = []; jjak=[]
# for i in range(0,len(s)):
#     if int(s[i])%2:
#         hol.append(s[i])
#     else:
#         jjak.append(s[i])
# print('홀수\n',hol)
# print('짝수\n',jjak)

# #no.11
# x1, x2, x3 = input('3개의 16진수를 입력하세요:').split()
# h1, h2, h3 = int(x1,16), int(x2,16), int(x3,16)
# print(f'{x1},{x2},{x3} -> {h1},{h2},{h3}')

# #no.12
# s=input('파일 이름을 입력해주세요:')
# if s[len(s)-4:len(s)] == '.jpg':
#     s= s[0:-4]+'.png'
# print(s)

# #no.13
# s1=input('첫 번째 문자열을 입력해주세요:')
# s2 = input('두 번째 문자열을 입력해주세요:')
# if s2 in s1:
#     print('두 번째 문자열이 첫 번째 문자열에 들어있습니다.')
#     print(f'두 번째 문자열이 첫 번째 문자열의 {s1.index(s2)}번째 인덱스에 있습니다.')

# #no.14
# s = input('문자열을 입력해주세요:')
# reverse = s[::-1]
# if s == reverse:
#     print('팰린드롬입니다.')
# else:
#     print('팰린드롬이 아닙니다.')

# #no.16
# s1=input('첫 번째 문자열을 입력해주세요:')
# s2 = input('두 번째 문자열을 입력해주세요:')
# if sorted(s1) == sorted(s2):
#     print(f'{s1}, {s2}는 아나그램입니다.')

# #no.17
# state = input('섭씨>화씨인지 화씨>섭씨인지 입력하세요:')
# if '섭씨' in state[0:2]:
#     C=float(input('섭씨 몇도인가요?'))
#     F=C*(9/5)+32
#     print('화씨',F)
# elif '화씨' in state[0:2]:
#     F=float(input('화씨 몇도인가요?'))
#     C=(F-32)/(9/5)
#     print('섭씨',C)
# else:
#     print('잘못 입력했습니다.')

#no.18
s1 = input('첫 번째 문자열을 입력해주세요:')
s2 = input('두 번째 문자열을 입력해주세요:')
if sorted(s1)==sorted(s2):
    print(f'{s1}, {s2}은 순열입니다.')
else:
    print(f'{s1}, {s2} 순열이 아닙니다.')
    
# #no.19
# s = input('16진수 색상 코드를 입력해주세요:')
# r=int(s[0:2],16)
# g=int(s[2:4],16)
# b=int(s[4:6],16)
# color=[r,g,b]
# print(f'{color}')

# #no.20
# p1=input('가위,바위,보 중 하나를 입력해주세요:')
# p2=input('가위,바위,보 중 하나를 입력해주세요:')
# if p1 == 'rock' or p1 == '바위':
#     if p2 == 'rock' or '바위':
#         print('Draw.')
#     elif p2 == 'paper' or '보':
#         print('p2 Win')
#     elif pw == 'scissor' or '가위':
#         print('p1 Win')
#     else:
#         print('p2가 잘못 입력하였습니다.')
# elif p1 == 'paper' or '보':
#     if p2 == 'rock' or '바위':
#         print('p1 Win.')
#     elif p2 == 'paper' or '보':
#         print('Draw')
#     elif pw == 'scissor' or '가위':
#         print('p2 Win')
#     else:
#         print('p2가 잘못 입력하였습니다.')
# elif p1 == 'scissor' or '가위':
#     if p2 == 'rock' or '바위':
#         print('p2 Win.')
#     elif p2 == 'paper' or '보':
#         print('p1 Win')
#     elif pw == 'scissor' or '가위':
#         print('Draw')
#     else:
#         print('p2가 잘못 입력하였습니다.')
# else:
#     print('p1이 잘못 입력하였습니다.')