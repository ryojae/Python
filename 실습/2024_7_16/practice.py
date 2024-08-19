# #no.3
# n=1
# while "":
#     print(n)
#     n+=1

# #no.4
# for i in range(7,1,-3):
#     print(i)

# #no.5
# def maximum():
#     max =0
#     for i in range(0,5):
#         n = int(input('숫자를 입력해주세요:'))
#         if max<n:
#             max=n
#     print('최댓값은',max,'입니다.')
# maximum()

#no.6
# #(1)
# i=100
# sum=0
# while i<=199:
#     sum += i
#     i +=1
# print(sum)
# #(2)
# i=100
# sum=0
# while i<=199:
#     if i%2 ==0:
#         sum += i
#     i +=1
# print(sum)
# #(3)
# i=100
# sum=0
# while i<=199:
#     if i%3 ==0:
#         sum += i
#     i +=1
# print(sum)

# #no.7
# def getSum(n):
#     i=100
#     sum=0
#     while i<=199:
#         if i%n ==0:
#             sum += i
#         i +=1
#     print(sum)

# for i in range(1,4):
#     getSum(i)

# #no.8
# def yaksu(n):
#     print(f'{n}의 약수:')
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end='  ')
#     print('\n')
# n = int(input('정수를 입력해주세요:'))
# yaksu(n)

# #no.9
# def yaksu(n):
#     print(f'{n}의 약수:')
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end='  ')
#     print('')
# n1, n2 = map(int,input('정수 두개를 입력해주세요:').split())
# for i in range(n1,n2+1):
#     yaksu(i)

#no.10
import random
def dice():
    double = []
    one, two, thr, fou, fiv, six = 0,0,0,0,0,0
    for i in range(0,5):
        n = random.randint(1,6)
        if n ==1:    one += 1
        elif n ==2:  two +=1
        elif n ==3:  thr +=1
        elif n==4:   fou +=1
        elif n==5:   fiv +=1
        else:        six +=1
    if one >1: print(f'1이 {one}개 중복됩니다.')
    if two >1: print(f'2가 {two}개 중복됩니다.')
    if thr >1: print(f'3이 {thr}개 중복됩니다.')
    if fou >1: print(f'4가 {fou}개 중복됩니다.')
    if fiv>1: print(f'5가 {fiv}개 중복됩니다.')
    if six>1: print(f'6이 {six}개 중복됩니다.')
dice()


# #no.11
# import random
# def ran():
#     i=1
#     while i<=10:
#         n=random.randint(1,6)
#         if n <=4:
#             print(n,end=', ')
#             i += 1
# ran()

# #mo.12
# def delete(s):
#     while s.find('\n') != -1:
#         s=s.strip('\n')
#     while s.find('.') !=-1:
#         s=s.strip('.')
#     while s.find('!')!=-1:
#         s=s.strip('!')
#     print(s)
# s = '...What a beautiful day!\n'
# delete(s)

# #no.13
# def over100():
#     i = 0
#     while i**3<=100:
#         i +=1
#     print(f'최초값은 {i}이고 그 값은 {i**3}입니다.')
# over100()

# #no.14
# i = 1000
# s=[]
# while i<=9999:
#     n1= i //1000
#     num= i%1000
#     n2=num//100
#     num = i %100
#     n3 = num//10
#     n4=num%10
#     if i == n1**4+n2**4+n3**4+n4**4:
#         s.append(i)
#     i +=1
# print(s)

# #no.15
# def prime(n):
#     pr1=0
#     for i in range(2,n):
#         if n%i==0:
#             pr1 +=1
#         i+=1
#     if pr1 ==0:
#         print('소수입니다.')
#     else:
#         print('소수가 아닙니다.')
# n=int(input('정수를 입력해주세요:'))
# prime(n)

# #no.16
# for n1 in range(1,10):
#     for n2 in range(1,10):
#         if (n1*10+n2)+(n2*10+n1) == 110:
#             print(f'n1={n1}, n2={n2}')

# #no.17
# import random
# def coin(n):
#     front=0; back =0
#     for i in range(0,n):
#         s = random.randint(0,1)
#         if s == 1:
#             front +=1
#         else:
#             back += 1
#     per1 =front*100/n
#     per2=back*100/n
#     print(f'{n}번')
#     print('앞면 확률:',per1)
#     print('뒷면 확률:',per2)
# coin(100)
# coin(1000)
# coin(10000)

# # no.18
# for i in range(1,11):
#     for j in range(1,9):
#         if i == 1:
#             print(f'{i} * n',end='\t')
#         else:
#             print(f'  {i*j}',end='\t')
#     print('')

# #no.19
# def compound_interest(principal, annual_interest_rate, years):
#     annual_interest_rate = annual_interest_rate / 100.0
    
#     for year in range(1, years + 1):
#         compound_total = principal * (1 + annual_interest_rate) ** year
#         total_interest = compound_total - principal
        
#         print(f"{year}년: 복리총액 {compound_total:,.0f}원, 총이자액 {total_interest:,.0f}원")
# principal = int(input("원금을 입력하세요 (원): "))
# annual_interest_rate = float(input("연이자율을 입력하세요 (%): "))
# years = int(input("투자기간을 입력하세요 (년): "))
# compound_interest(principal, annual_interest_rate, years)
