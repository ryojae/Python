# #no.4
# import os
# print('현재 주소:',os.getcwd())

# #no.5
# with open('data.txt','w') as f:
#     f.write('Hello\nThis is data\n이 파일은 utf-8형식으로 저장했습니다.\n')
# with open('data.txt') as f:
#     s = f.read()
#     print(s)

#no.7
with open("data.txt") as f:
      for line in f:
            print(line.strip())
f.close()

# #no.8
# with open('data.txt','a') as f:
#     f.write('Here comes to the end')
# with open('data.txt') as f:
#     s=f.read()
#     print(s)

# #no.9
# with open("python.utf8.txt", encoding = 'utf-8') as f:
#       s = f.read()
#       print(s)

# #no.10
# with open('data.txt') as f:
#     s= f.readlines()
# name = input('파일 이름:')
# with open(name,'w') as f:
#     for i in s:
#         f.write(i)
# with open(name) as f:
#     s= f.read()
#     print(s)

# #no.11
# with open('data.txt') as f1:
#     s1= f1.readlines()
# with open('data2.txt','w') as f2:
#     for i in s1:
#         f2.write(i)
# with open('data2.txt') as f3:
#     s2=f3.readlines()
# s=s1+s2
# with open('data3.txt','w') as f4:
#     for i in s:
#         f4.write(i)

# #no.12
# with open('data3.txt') as file:
#     s = input('검색할 문자열: ')
#     lines = file.readlines()
#     for i, line in enumerate(lines):
#         if s in line:
#             print(f'{i+1}번째 라인: {line}')

# #no.13
# with open('data3.txt') as file:
#     s= file.readlines()
#     for i in s:
#         print(i,end='')

# #no.14
# with open('data3.txt') as file1:
#     find_result=False
#     s1 = file1.readlines()
#     search_text = input('찾는 문자열을 검색하세요')
#     result=[]
#     for i, line in enumerate(s1):
#         if search_text in line:
#             result.append(line)
#             find_result = True
#     if find_result == False:
#             print('검색 단어가 파일에 없습니다.')
# if len(result)>0:
#     save_file_name=input('저장할 파일 이름을 입력하세요')
#     with open(save_file_name,'w') as file2:
#         for line in result:
#             file2.write(line)

# #no.15
# with open('data1.txt') as file1:
#     lst1=file1.readlines()
#     data1=[]
#     for i in lst1:
#         n = i.strip()
#         data1.append(int(n))
# with open('data2.txt') as file2:
#     lst2=file2.readlines()
#     data2=[]
#     for i in lst2:
#         n = i.strip()
#         data2.append(int(n))
# data = sorted(data1+data2)
# with open('data3.txt','w') as file3:
#     for i in data:
#         file3.write(f'{i}')
#         file3.write('\n')

# #no.16
# import math
# with open('shapes.txt') as file:
#     s = file.readlines()
#     for i in range(0,len(s)):
#         if s[i].strip('\n')=='사각형':
#             w=abs(int(s[i+1].strip('\n'))-int(s[i+3].strip('\n')))
#             h=abs(int(s[i+2].strip('\n'))-int(s[i+4].strip('\n')))
#             print(f'사각형의 넓이는 {w*h}입니다.')
#         elif s[i].strip('\n')=='삼각형':
#             a = ((int(s[i+1].strip('\n'))-int(s[i+3].strip('\n')))**2+(int(s[i+2].strip('\n'))-int(s[i+4].strip('\n')))**2)**(1/2)
#             b = ((int(s[i+3].strip('\n'))-int(s[i+5].strip('\n')))**2+(int(s[i+4].strip('\n'))-int(s[i+6].strip('\n')))**2)**(1/2)
#             c = ((int(s[i+5].strip('\n'))-int(s[i+1].strip('\n')))**2+(int(s[i+6].strip('\n'))-int(s[i+2].strip('\n')))**2)**(1/2)
#             s_area = (a+b+c)/2
#             area = (s_area*(s_area-a)*(s_area-b)*(s_area-c))**(1/2)
#             print(f'삼각형의 넓이는 {area:.2f}입니다.')
#         elif s[i].strip('\n') == '원':
#             area_circle = math.pi * (int(s[i+1].strip('\n')))**2
#             print(f'원의 넓이는 {area_circle:.2f}입니다.')

# #no.17
# text_name = input('텍스트 파일의 이름을 입력하세요:')
# with open(text_name) as file1:
#     s= file1.readlines()
# with open('copy.txt','w') as file2:
#     for i in s:
#         file2.write(i)

# #no.18
# name = input('파이썬 코드 파일 고르세요')
# new_name='new_'+name
# with open(name) as file1:
#     s= file1.readlines()
# with open(new_name,'w') as file2:
#     for i in s:
#         code=i.lstrip('#')
#         file2.write(code)

# #no.19
# name = input('텍스트 파일 이름을 입력해주세요:')
# with open(name) as file:
#     s = file.readlines()
# word=[]
# for i in s:
#     a=i.split()
#     for i in a:
#         word.append(i)
# print(f'단어의 갯수는 {len(word)}입니다.')

#no.20
import csv
with open('data1.csv') as file1:
    c1=csv.reader(file1)
    with open('data2.csv') as file2:
        c2=csv.reader(file2)
        with open('data3.csv','w') as file3:
            writer = csv.writer(file3)
            for row in c1:
                writer.writerow([row[0],row[1]])
            for row in c2:
                writer.writerow([row[0],row[1]])
with open('data3.csv') as file4:
    c3=csv.reader(file4)
    for row in c3:
        if int(row[1]) >=20:
            print(f'이름:{row[0]}, 나이:{row[1]}')
