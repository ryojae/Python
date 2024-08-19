# #no.1
# max = 0
# for i in range(0,5):
#     n= int(input('숫자를 입력해주세요:'))
#     if max<n:
#         max = n
# print(max)

# #no.2
# num = int(input('1~100 사이의 정수를 입력하세요:'))
# while 0>=num or num>100:
#     print('범위 밖입니다.')
#     num = int(input('1~100 사이의 정수를 입력하세요:'))
# print(num)

# #no.3
# n = int(input('정수: '))
# s=[]
# for i in range(1,n+1):
#     if n%i ==0:
#         s.append(i)
# print(s)

# #no.4
# import random
# n = int(input('횟수: '))
# s1=[]
# s2=[]
# for i in range(0,n):
#     if random.randint(0,1):
#         s1.append('앞')
#     else:
#         s2.append('뒤')
# per1 = len(s1)*100/n
# per2 = len(s2)*100/n
# print(per1,per2)

# #no.1
# def sum_under_100():
#     sum=0
#     while sum<100:
#         n = int(input('숫자: '))
#         sum += n
#     print(sum)
# sum_under_100()

# #no.2
# def password():
#     answer = 'ROKEY'
#     s = input('비밀번호: ')
#     while s!=answer:
#         print('잘못 입력')
#         s = input('비밀번호: ')
#     print('인증성공')
# password()

# #no.3
# def reverse():
#     s=input('문자열: ')
#     reversed=''
#     for i in range(len(s)-1,-1,-1):
#         reversed+=s[i]
#     print(reversed)

# reverse()

# #no.4
# import random
# def ran(n):
#     sum = 0
#     for i in range(0,n):
#         sum += random.randint(1,100)
#     print(sum)
# n=int(input('정수: '))
# ran(n)

# #no.5
# def chess():
#     for i in range(0,8):
#         for j in range(0,8):
#             if i % 2 ==0:
#                 print('# ',end='')
#             else:
#                 print(' #',end='')
#         print('\n')
# chess()

# #no.6
# def sumall(n):    
#     sum = 0
#     for i in range(1,n+1):
#         if n<=1:
#             break
#         sum += i
#     if n<=1:
#             print('잘못 입력하였습니다.')
#     else:
#         print(sum)
# n = int(input('정수: '))
# sumall(n)

# #no.7
# def star(n):
#     i=0
#     while i<n:
#         print('*',end='')
#         i+=1
# n = int(input('정수: '))
# star(n)

# #no.8
# import random
# def updonw():
#     answer = random.randint(1,100)
#     n= int(input('정수: '))
#     while n != answer:
#         if answer > n:
#             print('크다')
#         else:
#             print('작다')
#         n= int(input('정수: '))
#     print('정답')
# updonw()

# #no.9
# def gugudan(n):
#     if 1<=n<=9:
#         for i in range(1,10):
#             print(n,'*',i,'=',n*i)
# n = int(input('1과 9사이의 정수를 입력해주세요:'))
# gugudan(n)

# #no.10
# def sumstring(s):
#     sum = 0
#     for char in s:
#         if char.isdigit():
#             sum += int(char)
#     print(sum)
# s = input('문자열: ')
# sumstring(s)

# #no.11
# def multi(n):
#     i=1
#     m=1
#     while i<=n:
#         if i %2:
#             m*=i
#         i+=1
#     print(m)
# n=int(input('정수:'))
# multi(n)

# #no.12
# def Counting(s,word):
#     count =0
#     for char in s:
#         if char == word:
#             count += 1
#     print(count)
# s=input('문자열: ')
# word=input('특정 단어: ')
# Counting(s,word)

# #no.13
# def sum_n1_to_n2(n1,n2):
#     sum = 0
#     while n1<=n2:
#         sum+=n1
#         n1+=1
#     print(sum)
# n1, n2 =map(int,input('두개의 정수:').split())
# sum_n1_to_n2(n1,n2)

# #no.14
# def gugudan():
#     for i in range(2,10):
#         print(i,'단')
#         print('||',end='')
#         for j in range(0,10):
#             print(i,'*',j,'=',i*j,end='||')
#         print('\n')
# gugudan()

# #no.15
# def pyramid(n):
#     for i in range(0,n):
#         for j in range(n-1,i,-1):
#             print(' ',end='')
#         print('*',end='')
#         for j in range(0,i*2):
#             print('*',end='')
#         print('\n')
# n=int(input('정수: '))
# pyramid(n)

# #no.16
# def seperate(s):
#     s=s.split()
#     for char1 in s:
#         print(char1)
#         for char2 in char1:
#             print(char2)
# s=input('문자열: ')
# seperate(s)

# #no.17
# def sum_square(n):
#     for i in range (1,n+1):
#         for j in range(1,n+1):
#             print(i*j,end=' ')
#         print('\n')
# n = int(input('정수: '))
# sum_square(n)