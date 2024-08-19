# #no.1
# import os
# print(os.listdir())

# #no.2
# import divisors
# n=divisors.getDivisorsList(10)
# print(n)

# #no.3
# import os
# n=os.listdir()
# lst=[]
# for i in n:
#     if i[-4:] == '.txt':
#         lst.append(i)
# print(lst)

# #no.4
# import os
 
# def calcFileSize(subdirectory):
#     lst = os.listdir(subdirectory)
#     size = 0
#     for i in lst:
#         s=subdirectory+'/'+i
#         size += os.path.getsize(s)
#     return size
# def listDir(directory):
#     fileLst = os.listdir(directory)
#     print(f'{directory}: {fileLst}')
#     for i in fileLst:
#         s=directory+'/'+i
#         size = calcFileSize(s)
#         print(f'{i}의 용량은 {size}입니다.')

# listDir('fol')

# #no.5
# import shutil
# shutil.copyfile('abc.txt','abc2.txt')

#no.6
from datetime import date, timedelta

today = date.today()
xmasday=date(2024,12,25)
time_100=timedelta(100)
print(f'오늘 날짜부f터 크리스마스까지 남은 날짜: {(xmasday-today).days}일')
print(f'오늘로부터 100일 이후의 날짜:{today+time_100}')