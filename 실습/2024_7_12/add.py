# #no.1
# my_str = 'Hello, World!'
# print('String length.',len(my_str))
# print('Indexing.',my_str[:5])
# print('Replacement string.',my_str.replace("World","Python"))
# print('is alphanumeric.',my_str.isalnum())
# print('is alphaveetic.',my_str.isalpha())
# print('is digit.',my_str.isdigit())
# print('is numeric.',my_str.isnumeric())
# print('is lowercase.',my_str.islower())
# print('is uppercase.',my_str.isupper())
# print('Uppercase.',my_str.upper())
# print('Lowercase.',my_str.lower())
# print('Swap case.',my_str.swapcase())
# print('Count of \'l\'.',my_str.count('l'))
# print('Count of \'l\' from index 6 to 10.',my_str.count('l',6,10))

# #no.2
# my_str = "Hello, World!"
# fixed_width = 35
# print("String length:".ljust(fixed_width), len(my_str))
# print("Indexing:".ljust(fixed_width), my_str[:5])
# print("Replacement string:".ljust(fixed_width), my_str.replace("World", "Python"))
# print("Is alphanumeric:".ljust(fixed_width), my_str.isalnum())
# print("Is alphabetic:".ljust(fixed_width), my_str.isalpha())
# print("Is digit:".ljust(fixed_width), my_str.isdigit())
# print("Is numeric:".ljust(fixed_width), my_str.isnumeric())
# print("Is lowercase:".ljust(fixed_width), my_str.islower())
# print("Is uppercase:".ljust(fixed_width), my_str.isupper())
# print("Uppercase:".ljust(fixed_width), my_str.upper())
# print("Lowercase:".ljust(fixed_width), my_str.lower())
# print("Swap case:".ljust(fixed_width), my_str.swapcase())
# print("Count of 'l':".ljust(fixed_width), my_str.count('l'))
# print("Count of 'l' from index 6 to 10:".ljust(fixed_width), my_str.count('l', 6, 10))

# #no.3
# s='Hello,World!,How,are,you,doing,today?'
# print(s.replace(',',' '))

# #no.4
# my_var1 = input('변수명을 입력해주세요:')
# if (my_var1[0] == '_' or my_var1.isalpha()) and my_var1[1:len(my_var1)].isalpha:
#    print("Variable name is valid")
# else:
#    print("Variable name is invalid")

# #no.5
# my_password = input('비밀번호를 입력해주세요:')
# up1, low1, al, num =0, 0, 0, 0
# if 8<=len(my_password)<=30 and my_password.isalnum():
#     for i in range(0,len(my_password)):
#         if my_password[i].isupper():
#             up1 = 1
#         elif my_password[i].islower():
#             low1 = 1
#         if my_password[i].isalpha():
#             al = 1
#         elif my_password[i].isdigit():
#             num = 1
#     if up1 and low1 and al and num:
#         print('적합한 비밀번호 입니다.')
#     else:
#         print('잘못된 비밀번호 입니다.')
# else:
#     print('잘못된 비밀번호 입니다.')

# #no.6
# my_input = 'abcd'
# answer = "ABCD"
# if my_input.lower() == answer.lower():
#    print("Strings are equal")
# else:
#    print("Strings are not equal")

# #no.7
# my_str = "Heelo"
# my_str = my_str[:2] + 'l' + my_str[3:]
# print(my_str)

# #no.8
# my_str = "Helo"
# my_str = my_str[0:2]+'l'+my_str[2:]
# print(my_str)

# #no.9
# my_str = "Helllo"
# my_str = my_str[0:2]+my_str[3:]
# print(my_str)

# #no.10
# file_name = "hello.txt.py"
 
# # 파일 확장자명 출력
# print(file_name.split(".")[-1])

# #no.11
# s='Hello,World!,How,are,you,doing,today?'
# print(s.replace(',',' '))