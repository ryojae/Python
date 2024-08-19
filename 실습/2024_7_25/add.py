# #no.1
# even=[i for i in range(2,11,2)]
# print(even)

# #no.2
# s=[i**2 for i in range(10) if i%2==1]
# print(s)

# #no.3
# mylist = [1, 5, 1, 7, 1]
# mylist[mylist.count(1)] = 70
# mylist[len(mylist) - 1] = 80
# mylist.insert(1, 50)
# print(mylist)

# #no.4
# import random
# lst=[random.randint(1,99) for i in range(0,10)]
# print(f'1에서 99까지의 난수 10개의 리스트 :{lst}')
# print(f'정렬된 리스트: {sorted(lst)}')
# print(f'내림차순으로 정렬된 역순 리스트: {sorted(lst,reverse=True)}')

# #no.5
# korean = ('정렬', '문자', '내포' , '사전')
# english = ('sorting', 'text', 'comprehension', 'dictionary')
# s=input('한국말:')
# if s in korean:
#     for i in range(0,len(korean)):
#         if korean[i] == s:
#             print(f'영어: {english[i]}')
# else:
#     print('해당 내용이 없습니다.')

#no.6
data = [[1, 2, 3],
        [4, 5, 6],               
        [7, 8, 9] ]
rsum=[]
csum=[]
for i in data:
    rsum.append(sum(i))
for i in zip(*data):
    csum.append(sum(i))
# for i in data:
#     rsum.append(sum(i))
#     for k in range(0,len(i)):
#         csum[k]= csum[k]+i[k]

print(f'각 행의 합: {rsum}')
print(f'각 열의 합: {csum}')

# #no.7
# m = [[1, 2], [3, 4], [5, 6], [7, 8]]
# transpose = [[row[i] for row in m] for i in range(len(m[0]))]
# print(transpose)

# #no.8
# from random import sample
# A = set(sample(list(range(1, 21)), 5))
# B = set(sample(list(range(1, 21)), 5))
# union = A|B
# combine = A&B
# diff_A_B=A-B
# diff_B_a=B-A
# comp_A=set(range(1,21))-A
# comp_B=set(range(1,21))-B
# print(f'집합 A: {A}')
# print(f'집합 B: {B}')
# print(f'합집합: {union}')
# print(f'교집합: {combine}')
# print(f'차집합(A-B): {diff_A_B}')
# print(f'차집합(B-A): {diff_B_a}')
# print(f'여집합 A: {comp_A}')
# print(f'여집합 B: {comp_B}')