# #no.2
# lst=[]
# for i in range(1,101):
#     lst.append(i)
# find_num = int(input('정수:'))
# print(find_num in lst)

# #no.4
# list_1=[1,2,3]
# tup_1=(4,5,6)
# list_1+=list(tup_1)
# print(list_1)

# #no.6
# my_tuple=(1,2,3,4,5)
# rm_element= int(input('삭제할 요소:'))
# new_tuple=tuple([i for i in my_tuple if i != rm_element])
# print(new_tuple)

# #no.7
# alp= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# #a)
# print(alp[1:5])
# #b)
# print(alp[-1:-6])
# #c)
# print(alp[:])
# #d)
# print(alp[1::2])
# #e)
# print(alp[-2:-10:-3])
# #f)
# print(alp[3:-1:2])

# #no.8
# alp= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# del alp[3]
# print(alp)

# #no.9
# alp= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# alp.clear()
# print(alp)

# #no.10
# def is_Palindrome(s):
#     if s == s[::-1]:
#         print(f'{s}는 Palindrome 입니다.')
#     else:
#         print(f'{s}는 Palindrome이 아닙니다.')
# s= input('단어:')
# is_Palindrome(s)

# #11
# data = '잣밤배귤감'
# lst=[]
# for i in data:
#     lst.append(i)
# lst_orm=sorted(lst)
# lst_nerim=sorted(lst,reverse=True)
# print('오름차순')
# print(lst_orm)
# print('내림차순')
# print(lst_nerim)

#no.12
strings = ["mango", "apple", "banana", "cherry",
            "date", "fig", "apple", "banana"]
string = list(set(strings))
print(sorted(string))