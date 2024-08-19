# #no.2
# import re  # 정규표현식을 사용하여 문자열 검색, 매칭, 치환 등의 작업을 수행할 수 있게 해주는 모듈

# # 테스트할 문장 목록
# sentences = [
#     "I love programming in Python.",
#     "JavaScript is a versatile language.",
#     "The Python snake is a non-venomous species."
# ]

# # 정규표현식 패턴
# pattern = r'Python'

# # 문장 판별
# for sentence in sentences:
#     if re.search(pattern, sentence):
#         print(f"'Python' found in: \"{sentence}\"")
#     else:
#         print(f"'Python' not found in: \"{sentence}\"")

#no.4
import re
 
text = "alice@example.com 이 첫 번째 이메일이고, 다음은 bob.smith@mail.co.uk 입니다."
 
# 일반 문자열로 이메일 패턴을 정의
pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
 
# match 메소드를 이용해 문자열의 시작에서 패턴에 매칭되는지 확인
match =re.match(pattern,text)

if match:
    print(match.group())
else:
    print("문자열의 시작 부분에 이메일이 없습니다.")

# #no.5
# import re

# text = "Hello, how are you today? Hello, I'm fine."
# # 일반 문자열로 'Hello'로 시작하는지 확인하는 패턴 정의
# pattern = r'^Hello'

# # match 메소드를 이용해 문자열의 시작에서 패턴에 매칭되는지 확인
# # Write your code here
# match = re.match(pattern,text)

# if match:
#     print("문자열은 'Hello'로 시작합니다.")
# else:
#     print("문자열은 'Hello'로 시작하지 않습니다.")

# #no.6
# import re
# text = "This is a sample text with the word 'sample' in it."
# pattern = r"'sample'"
# match = re.search(pattern,text)
# if match:
#     print(match.group())
#     print('문자열 안에 \'sample\'이 들어있습니다.')
# else:
#     print('문자열 안에 \'sample\'이 없습니다.')

# #no.7
# import re
# text = "오늘의 날짜는 2023-06-28이고, 내일은 2023-06-29입니다."

# # 일반 문자열로 날짜 형식 패턴 정의
# pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'

# # findall 메소드를 이용해 모든 패턴 매칭을 찾음
# matches = re.findall(pattern, text)

# if matches:
#     print("찾은 날짜들:", matches)
# else:
#     print("날짜 형식을 찾을 수 없습니다.")

# #no.8
# import re
 
# text = "다음 사람들에게 이메일을 보내세요: alice@example.com, bob.smith@mail.co.uk, charlie123@domain.org."
 
# pattern = r'[a-zA-Z0-9.]+@[a-zA-Z.]+\.[a-zA-Z]{2,}'

# emails = re.findall(pattern,text)

# print(emails)

# #no.9
# import re
# text = "상품의 가격은 19.99달러와 100.0달러, 0.99달러 입니다."

# pattern = r'\d+\.\d+'

# match = re.findall(pattern,text)
# print(match)

# #no.10
# import re
 
# text = "<html><head><title>Test</title></head><body><h1>Header</h1><p>Paragraph</p></body></html>"

# pattern = r'<[^>]+>'

# match = re.findall(pattern,text)

# print(match)

# #no.11
# import re
# def check_password_strength(password):
#     # 최소 8자 이상, 숫자와 특수문자를 포함하는지 확인하는 정규표현식
#     pattern = r'^(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{8,}$'
#     if re.match(pattern,password):
#         return True
#     else:
#         return False

# # 테스트
# password1 = "StrongPassword123!"
# print(f"Password '{password1}' is strong: {check_password_strength(password1)}")

# newPswd = input('\n패스워드를 입력하세요: ')
# if check_password_strength(newPswd):
#     print('안전한 패스워드입니다.')
# else:
#     print('패스워드의 기준에 맞지 않습니다')


# #no.12
# import re

# text = "Hello! @world! This is 2024. @#$%^&*"

# pattern = r'[!@#$%^&*]+'

# sub = re.sub(pattern,'', text)
# print(sub)