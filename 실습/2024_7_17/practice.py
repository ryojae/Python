# #no.3
# lst2 = list()
# print(lst2)

# #no.4
# for ch in ["hello"]:
#       print(ch)


# #no.6
# print("He is not my type, \tthanks".split(" \t"))
# print("He is not my type, \tthanks".split(" ", 2))
# print("He is not my type, \tthanks".split("t"))

# #no.8
# my = (1, 2)
# my.append([3, 4])

# #no.10
# my_list = [1,2,3,4]
# print(type(my_list))
# my_list=tuple(my_list)
# print(type(my_list))
# my_list=list(my_list)
# print(type(my_list))

# #no.11
# def yaksu(n):
#     yak=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             yak.append(i)
#     print(f'{n}의 약수 개수: {len(yak)}')
# for i in range(2,21):
#     yaksu(i)

# #no.12
# myList=[1,2,2,3,4,4,5]
# myList=set(myList)
# print(myList)

# #no.13
# def yaksu(n1,n2):
#     for i in range(n1,n2+1):
#         yak =[]
#         for j in range(1,i+1):
#             if i%j ==0:
#                 yak.append(j)
#         print(f'{i}의 약수: {yak}')
# yaksu(10,16)

# #no.14
# def orm(l1,l2):
#     l = l1+l2
#     l=sorted(l)
#     print(f'{l1}+{l2} 후 오름차순 정령은 {l}입니다.')
# l1=[1,5,8,10,14]
# l2=[2,4,5,9]
# orm(l1,l2)

# #no.15
# def make_lsit(n):
#     l=[]
#     for i in range(0,n):
#         l.append(int(input(f'정수 {i+1}:')))
#     return l
# l = make_lsit(int(input('정수 n개:')))
# print(l)

# #no.16
# def createDivisorList(n):
#     l=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             l.append(i)
#     print(f'정수 {n}의 약수는 {l}입니다.')
#     return l

# n=int(input('정수를 입력해주세요:'))
# if 1<=n<=1000:
#     l=createDivisorList(n)
#     print(f'정수 {n}의 모든 약수의 합은 {sum(l)}입니다.')

# #no.17
# def make_tuple(n):
#     t=[]
#     for i in range(1,n+1):
#         t.append(int(input(f'정수 {i}:')))
#     return tuple(t)
# n=int(input('정수:'))
# t = make_tuple(n)
# print(t)

# #no.18
# import math
# def calcAndPrintArea(t):
#     for i in range(0,len(t)):
#         if t[i] == '사각형':
#             print(f'{t[i]}의 넓이는 {t[i+1]*t[i+2]}입니다.')
#         elif t[i] == '원':
#             print(f'{t[i]}의 넓이는 {math.pi*(t[i+1]**2):.2f}입니다.')
# t = ('사각형',30,20,'원',10,'사각형',20,40,'사각형',10,10,'원',20)
# calcAndPrintArea(t)

# #no.19
# data =[[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# Sum = []
# rSum=[]
# for i in range(0,3):
#     total = sum(data[i])
#     Sum.append(total)
#     total = 0
#     for j in range(0,3):
#         total += data[j][i]
#     rSum.append(total)

# print(f'각 행의 합은 {Sum}입니다.')
# print(f'각 열의 합은 {rSum}입니다.')

#no.20
def Second(l):
    second =[]
    for i in l:
        j=sorted(i)
        second.append(j[1])
    return second

# 행렬의 크기를 입력받습니다.
n = int(input("행과 열의 수를 입력하세요: "))

# 빈 행렬을 만듭니다.
matrix = []

# 행렬의 각 행을 입력받아 리스트에 저장합니다.
print("행렬의 각 행을 입력하세요:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 입력받은 행렬을 출력합니다.
print("입력받은 행렬:")
for row in matrix:
    print(row)

l=Second(matrix)
print(l)

# #no.21
# lst=[[1,2],[3,4],[5,6],[7,8]]
# for i in lst:
#     print(i[0],' ',i[1])
# l1=[]
# l2=[]
# for i in lst:
#     l1.append(i[0])
#     l2.append(i[1])
# print('')
# for i in l1:
#     print(i,end='  ')
# print('')
# for i in l2:
#     print(i,end ='  ')
# print('')

# #no.22
# import random
# ran =[]
# for i in range(0,10):
#     ran.append(random.randint(1,99))
# print(ran,type(ran))
# ran = tuple(ran)
# print(ran,type(ran))
# ran = list(ran)
# print(f'전체의 합: {sum(ran)}, 최대값: {max(ran)}, 최소값: {min(ran)}, 평균값: {sum(ran)/len(ran)}')

# #no.23
# def triangle_dot(t1, t2, t3):
#     l=[list(t1),list(t2),list(t3)]
#     return l

# def traingle_area(l):
#     a = ((l[0][0]-l[1][0])**2+(l[0][1]-l[1][1])**2)**(1/2)
#     b = ((l[1][0]-l[2][0])**2+(l[1][1]-l[2][1])**2)**(1/2)
#     c = ((l[2][0]-l[0][0])**2+(l[2][1]-l[0][1])**2)**(1/2)
#     s = (a+b+c)/2
#     return (s*(s-a)*(s-b)*(s-c))**(1/2)
# t1 = map(int,input('삼각형의 꼭지점 좌표를 입력해줘: ').split())
# t2 = map(int,input('삼각형의 꼭지점 좌표를 입력해줘: ').split())
# t3 = map(int,input('삼각형의 꼭지점 좌표를 입력해줘: ').split())
# l = triangle_dot(t1,t2,t3)
# print(f'{traingle_area(l):.1f}')