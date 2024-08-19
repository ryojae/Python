# #no.1
# def counter(number=0):
#     current = number
#     while True:
#         x = yield current
#         if x is None:
#             x =1
#         current += x
# count = counter(10)
# print(next(count))
# print(count.send(5))
# print(count.send(3))
# print(next(count))

# #no.2
# def repeat_task():
#     while True:
#         x= yield
#         print(x)
# a=repeat_task()
# next(a)
# a.send('hi')

# #no.3
# import re
# if re.match('^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$',input('이메일:')):
#     print('valid')
# else:
#     print('invalid')

# #no.4
# import re

# def number(s):
#     pattern=r'^\(\d{3}\) \d{3}-\d{4}$'
#     if re.match(pattern,s):
#         return 'Valid'
#     else:
#         return 'Invalid'
# print(number('(123) 456-7890'))
# print(number('123-456-7890'))

# #no.5
# import re
# def rm_html(html):
#     pattern=r'<[^>]+>'
#     text = re.sub(pattern,'',html)
#     return text
# html_content='<html><head><title>Test</title></head><body>Hello,world!</body></html>'
# print(rm_html(html_content))

# #no.6
# import re

# def passwordcheck(password):
   
#         if re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d].{7,}$',password):
#             return 'valid'
#         else:
#             return 'invalid'
        
# print(passwordcheck('Password1234'))
# print(passwordcheck('Passwor1'))

#no.7
import re

def parse_url(url):
    pattern = r'^(https?):\/\/([^:/\s]+)(?::(\d+))?'
    match = re.match(pattern, url)
    if match:
        return {
            "protocol": match.group(1), 
            "host": match.group(2),
            "port": match.group(3)
        }
    else:
        return "Invalid URL"

# 함수 호출 및 출력
print(parse_url("http://example.com:8080")) 
# {'protocol': 'http', 'host': 'example.com', 'port': '8080'}

print(parse_url("https://example.com")) 
# {'protocol': 'https', 'host': 'example.com', 'port': None}
