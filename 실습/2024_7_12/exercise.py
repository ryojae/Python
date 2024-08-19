# #no.1
# s='Beautiful.Image.png'
# n=s.rfind('.')
# print(s[0:n])

# #no.2
# s=input('파일 이름을 입력해주세요:')
# n=s.find('.')
# if n == -1:
#     print(s)
# else:
#     print(s[0:n])

# #no.3
# s= input('두 개 이상의 단어를 입력해주세요:')
# s=s.strip()
# n=s.find(' ')
# print('첫번째 문자:',s[0:n],'두번째 문자:',s[n+1:len(s)])

# #no.4
# s=input('파일 이름을 입력해주세요:')
# if s[len(s)-4:len(s)] == '.png':
#     s= s[0:-4]+'.jpg'
# print(s)

# #no.5
# s = input('문자열을 입력해주세요:')
# reverse = s[::-1]
# print(reverse)

# #no.6
# s = input('문자열을 입력해주세요:')
# s= s.upper()
# print(s)

# #no.7
# s, rem=input('문자열과 제거할 문자를 입력해주세요:').split()
# print(s)
# print(rem)
# while s.find(rem)!=-1:
#     a= s.replace(rem,'')
#     s=a
# print(s)

# #no.8
# s = input('문자열을 입력해주세요:')
# s=s.strip()
# print(s)

# #no.9
# s = input('문자열을 입력해주세요:')
# n = len(s.split())
# print(n)

# #no.10
# s, word = input('문자열과 특정 단어를 입력해주세요:').split()
# print(s.count(word))

# #no.11
# s.swapcase()

# #no.12
# s[0].upper

# #no.13
# split(), 각단어[0].upper

# #no.14
# s=input()
# word=s.encode('utf-8')
# print(word)

# #no.15
# s=input()
# word=s.encode('utf-8')
# print(word)
# # word=eval(word)
# word2=word.decode()
# print(word2)

# #no.16
# import urllib.parse
# s=input('')
# url=urllib.parse.quote(string=s)
# print(url)

# #no.17
# import urllib.parse
# s=input('')
# url=urllib.parse.quote(string=s)
# print(url)
# url=urllib.parse.unquote(string=url)
# print(url)

# #no.18
# s = input()
# word=s.encode().hex()
# print(word)

# #no.19
# s = input()
# word=s.encode().hex()
# print(word)
# word=bytes.fromhex(word).decode()
# print(word)