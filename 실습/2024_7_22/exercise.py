# #no.1
# sentences = """Lorem ipsum dolor sit amet, consectetuer
# adipiscing elit.
# Maecenas porttitor congue massa.
# Fusce posuere, magna sed pulvinar ultricies, purus lectus
# malesuada libero, sit amet
# commodo magna eros quis urna.
# Nunc viverra imperdiet enim.
# """
# lowerSentences = sentences.lower()
# d={}
# for i in lowerSentences:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for k,v in d.items():
#     if k =='\n':
#         k='NEWLINE'
#     elif k =='\t':
#         k='TAB'
#     elif k==' ':
#         k='SPACE'
#     print(f'{k}:{v}',end=', ')

# #no.2
# def save_name_and_age():
#     name=input('이름을 입력해주세요:')
#     age = int(input('나이를 입력해주세요:'))
#     person={'name':name,'age':age}
#     print(person)
#     print(type(person))
# save_name_and_age()

# #no.3
# def find_key():
#     d={'1':2,'name':'홍길동'}
#     finding=input('찾는 키를 입력해주세요:')
#     if finding in d:
#         print(d[finding])
#     else:
#         print('X')
# find_key()

# #no.4
# n=map(int,input('숫자를 입력해주세요:').split())
# d=set(n)
# print(d)

# #no.5
# d={'1':2,'2':3,'3':4}
# k, v = input('키와 값을 입력해주세요:').split()
# d[k]=v
# print(d)

# #no.6
# d={'1':2,'2':3,'3':4}
# k = input('삭제할 키를 입력해주세요:')
# if k in d:
#     del(d[k])
#     print(d)
# else:
#     print('error')

# #no.7
# d={'1':2,'2':3,'3':4}
# print(list(d.keys()))
# print(list(d.values()))

# #no.8
# d={'1':2,'2':3,'3':4}
# for k,v in d.items():
#     print(f'{k}의 값은 {v}입니다.')

# #no.9
# dict1={'name':'Alice','age':30}
# dict2={'city':'New York','country':'USA'}
# dict1.update(dict2)
# print(dict1)

# #no.10
# dict1={'name':'Alice','age':30}
# key = input('키를 입력해주세요:')
# value = dict1.get(key,'Not Found')
# print(f'{key}: {value}')

# #no.11
# data = {'Alice':25,'Bob':19,'Cathy':34,'Dan':20}
# new_data={}
# for k,v in data.items():
#     if v>20:
#         new_data[k]=v
# print(new_data)

# #no.12
# set={1,2,3}
# n=int(input())
# set.add(n)
# print(set)

# #no.13
# set1={1,2,3,4,5}
# n=int(input())
# try:
#     set1.remove(n)
#     print(set1)
# except:
#     print('없습니다')

# #no.14
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1&set2)
# print(set1.intersection(set2))

# #no.15
# s1={1,2,3}
# s2={3,4,5}
# print(s1|s2)
# print(s1.union(s2))

# #no.16
# s1={1,2,3,4,5}
# s2={4,5,6,7}
# print(s1-s2)
# print(s1.difference(s2))

# #no.17
# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1^s2)
# print(s1.symmetric_difference(s2))

# #no.18
# s= input('Input:')
# data={}
# while s!='Stop':
#     if s in data:
#         data[s]+=1
#     else:
#         data[s]=1
#     s= input('Input:')
# print(data)

#no.19
# n=list(map(int,input('Input').split()))
# print(set(n))
# data={}
# for i in n:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# print(data)

# def remove_duplicates_and_count():
#     numbers = map(int, input("숫자들을 공백으로 구분하여 입력하세요:").split())
#     number_dict = {}
#     for number in numbers:
#         if number in number_dict:
#             number_dict[number] += 1
#         else:
#             number_dict[number] = 1
#             unique_numbers = set(number_dict.keys())
#     print("고유 숫자:", unique_numbers)
#     print("각 숫자의 카운트:", number_dict)
# # 함수 호출
# remove_duplicates_and_count()

# #no.20
# s1= set(input('Input1:'))
# s2= set(input('Input2:'))
# print(sorted(s1&s2))

#no.21