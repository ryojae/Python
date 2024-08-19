# #no.4
# def same_directory(dict1,dict2):
#     dict3={}
#     for k, v in dict1.items():
#         if k in dict2:
#             if v == dict2[k]:
#                 dict3[k]=v
#     return dict3
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dict2 = {'a': 1, 'b': 2, 'c': 4, 'e': 5}
# dict3 = same_directory(dict1,dict2)
# print(f'공통된 키-값 쌍: {dict3}')

# #no.6
# s1={1, 2, 3};s2={1, 2, 4, 5} 
# print(f's1과 s2의 합집합: {s1|s2}')
# print(f's1과 s2의 교집합: {s1&s2}')

# #no.7
# data={'이름':'김영희','전화번호':'010-1111-2222','성별':'여자','나이':22,'대학교':'한국대학교'}
# print(data)

# #no.8
# def common_char(str1,str2):
#     str1=str1.lower()
#     str2=str2.lower()
#     common=set()
#     for i in str1:
#         if i in str2:
#             common.add(i)
#     common.remove(' ')
#     return common
# str1 = "Hello World"
# str2 = "Python Programming"
# common=common_char(str1,str2)
# print('output')
# print(common)

# #no.9
# def find_price(s):
#     data ={'삼성에스디에스': 242000, '삼성전자': 67000, '엔씨소프트': 52000, '핸디소프트':5120, '골프존': 215000, '기아': 65000}
#     if s in data:
#         print(f'{s}: {data[s]}')
#     else:
#         print('주식 이름이 없습니다.')
# name = input('주식 이름?')
# find_price(name)

# #no.10
# books = {'파이썬 개론':['홍길동'],'Perfect C':['김영수','이동준'],
#          '컴퓨터 개론':['최한수','주용호','박해성']}
# name=input('책 이름: ')
# if name in books:
#     print(f'저자: {books[name]}')
# else:
#     print('책이 없습니다.')