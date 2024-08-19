# # # f= open('t.txt')
# # with open('t.txt') as f:
# #     # lines=f.readlines()
# #     for line in f:
# #         print(line,end='')
# #     # line=f.readline()
# # # f.close()

# import locale
# print(locale.getpreferredencoding())

# #no.1
# name1 = input('이름:')
# name2 = input('이름:')
# name3 = input('이름:')
# with open(name1) as f1:
#     s1 = f1.read()
# with open(name2) as f2:
#     s2=f2.read()
# with open(name3,'w') as f3:
#     f3.write(s1)
#     f3.write(s2)


# #no.2
# lineNum = 1
# found =False
# filename = input('파일 이름을 입력하세요:')
# findStr = input('검색할 문자열을 입력하세요:')
# with open(filename) as f:
#     for line in f:
#         if findStr in line:
#             if findStr in line:
#                 found =True
#                 print(f'{lineNum}:{line.strip()}')
#             lineNum+=1

# if found == False:
#     print('검색 단어가 파일에 없습니다.')

# #no.3
# with open('output.txt','a') as f:
#     s= input('텍스트:')
#     while s !='stop':
#         f.write(s)
#         s= input('텍스트:')
#     print('완료')


# #no.4
# def Countfile():
#     with open('output.txt') as f:
#         s=f.read()
#         c=input('단어:')
#         print(s.count(c))
# Countfile()

# #no.6
# import csv
# def save_csv():
#     with open('contacts.csv','w' )as c:
#         writer = csv.writer(c)
#         writer.writerow(['이름','나이','이메일'])
#         while True:
#             name = input('이름을 입력하세요:')
#             if name == 'stop':
#                 break
#             age = int(input('나이를 입력하세요:'))
#             email=input('이메일을 입력하세요:')
#             writer.writerow([name,age,email])
#     print('연락처가 csv 파일에 저장되었습니다.')
# save_csv()

# #no.7
# def read_csv():
#     import csv
#     with open('contacts.csv') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for i in reader:
#             print(f'이름: {i[0]}, 나이: {i[1]}, 이메일: {i[2]}')

# read_csv()

# #no.9
# def write_binary_data():
#     data = bytes([255,0,127,64,32,16])
#     print(data)
#     with open('binary_data.bin','wb') as file:
#         file.write(data)
#     print('바이너리 데이터가 저장')
# write_binary_data()

# #no.10
# def read_binary():
#     with open('binary_data.bin','rb') as file:
#         b = 