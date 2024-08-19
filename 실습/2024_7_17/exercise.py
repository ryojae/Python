# #no.1
# def sumlist():
#     s= input('세 개의 숫자를 입력해주세요:').split()
#     print(s)
#     sum = 0
#     for i in s:
#         sum += int(i)
#     print(sum)
# sumlist()

# #no.2
# def max_min():
#     number =[]
#     number.append(int(input('첫번째 숫자를 입력해주세요:')))
#     number.append(int(input('두번째 숫자를 입력해주세요:')))
#     number.append(int(input('세번째 숫자를 입력해주세요:')))
#     print(f'최댓값: {max(number)}, 최솟값: {min(number)}')
# max_min()

# #no.3
# def return_tuple(name,age):
#     return name,age
# name = input('이름을 입력해주세요:')
# age = input('나이를 입력해주세요:')
# str1= input('').split()
# data=return_tuple(name,age)
# print(data)
# print(type(data))
# print(type(str1))

# #no.4
# def save_tuple():
#     n1 = int(input('첫 번째 숫자를 입력해주세요:'))
#     n2 = int(input('두 번째 숫자를 입력해주세요:'))
#     n3 = int(input('세 번째 숫자를 입력해주세요:'))
#     number = n1,n2,n3
#     print(number,type(number))
#     print(number[0],number[2])
# save_tuple()

# #no.5
# n1 = int(input('첫 번째 숫자를 입력해주세요:'))
# n2 = int(input('두 번째 숫자를 입력해주세요:'))
# n3 = int(input('세 번째 숫자를 입력해주세요:'))
# number = n1,n2,n3
# print(sum(number),max(number),min(number))

# #no.6
# s= input('문자열:').split()
# print(tuple(s))

# #no.7
# s1 = [1, 2, 3]
# s2 = [2, 3, 4]
# t1 = (1, 2, 3)
# t2 = (2, 3, 4)
# l=[s1,t1]
# t=(s2,t2)
# print(l,'\n',t)

# #no.8
# l=[1,2,3,]
# s=(4,5,6,)
# n=int(input('숫자:'))
# if n in l or s:
#     print('있음')

# #no.9
# number = input('여러 개의 숫자:').split()
# print(number)
# number.reverse()
# print(number)

# #no.10
# t = 1,2,3,4,5,6
# print(t[1:4])

# #no.11
# l = [[1,2],[3,4],[5,6]]
# new_list =[]
# for s1 in l:
#     for s2 in s1:
#         new_list.append(s2)
# print(new_list)

# #no.12
# n=input('숫자들을 입력하세요(공백으로 구분):').split()
# for i in range(0,len(n)):
#     n[i]=int(n[i])
# print(tuple(n))

# #no.13
# n=input('숫자들을 입력하세요(공백으로 구분):').split()
# for i in range(0,len(n)):
#     n[i]=int(n[i])
# print(list(set(n)))

# #no.14
# n = int(input('정수:'))
# l = [1,2,3,4,5]
# print(l*n)

# #no.15
# a,b,c=1,2,3
# t= a,b,c
# print( t)
# print(a,b,c)

# #no.16
# n = list(map(int,input('여러개의 숫자(공백 구분):').split()))
# print(sorted(n))

# #no.17
# t = 10,20,30,40,50
# for i in t:
#     if i>30:
#         print(i)

t= (1,2,[3,4,5])
print(t)
t[2][2] = 6
print(t)