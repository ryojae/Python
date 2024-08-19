# #no.2
# increment = lambda x: x + 1
# print(increment)

# #no.3
# n=int(input('정수:'))
# num=lambda x: x**2 if x %2 ==0 else x
# print(num(n))

# #no.4
# def abc():
#     return lambda x: x**2 if x%2==0 else x
# numbers = [1,2,3,4,5]
# result = map(abc(),numbers)
# print(list(result))

# #no.5
# numbers = [2,3,4,5,6,7]
# result = map(lambda x: x if x<3 else x*2 if x<6 else x*3, numbers)
# print(list(result))

# #no.6
# def calculate_elements(list1, list2):
#     lst=[]
#     for i in range(len(list1)):
#         if list1[i] % 2==0:
#             lst.append(list1[i]+list2[i])
#         else:
#             lst.append(list1[i]*list2[i])
#     return lst

# # 두 개의 리스트
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]

# # 함수 호출 및 결과 출력
# result = list(map(lambda x, y: x + y if x%2==0 else x*y,list1,list2))
# print(result)

# #no.7
# # 두 개의 리스트
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]

# # 함수 호출 및 결과 출력
# result = list(map(lambda x, y: x + y if x%2==0 else x*y,list1,list2))
# print(result)

# #no.8
# def filtering(words):
#     lst = []
#     for i in words:
#         if 'a' in i:
#             lst.append(i)
#     return lst
# words = ["apple", "banana", "cherry", "date",
#           "elderberry", "fig", "grape"]
# result=filtering(words)
# print(result)

# #no.9
# words = ["apple", "banana", "cherry", "date",
#           "elderberry", "fig", "grape"]
# result=list(filter(lambda x: 'a' in x, words))
# print(result)

# #no.10
# def prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return '소수가 아닙니다.'
#     return '소수입니다.'
# n=int(input('정수:'))
# print(prime(n))

#no.11
n=int(input('정수:'))
lst1 = []
lst2 = []
for i in range(2,n):
    lst1.append(n)
    lst2.append(i)
result = list(map(lambda x,i: 'X' if x%i ==0 else 'O',lst1,lst2))
if 'X' in result:
    print(f'{n}은 소수가 아닙니다.')
else:
    print(f'{n}은 소수입니다.')