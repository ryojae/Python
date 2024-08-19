# #
# import sys
# try:
#     fname = 'a.txt'
#     f = open(fname)
#     lines=f.readlines()
#     f.close()
#     line = f.readlines()
# except FileNotFoundError:
#     print('Could not open '+fname)
#     sys.exit()
# except:
#     print('Other error occurred')
# print('End of the program')
# print('안끝나')

# #no.1
# def division():
#     import sys
#     try:
#         n1,n2=map(int,input('숫자 두개를 입력해주세요:').split())
#         print(n1,n2)
#         print(n1/n2)
#         return True
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')
#         sys.exit()
#     except:
#         print('잘못 입력하였습니다.')
# while 1:
#     if division():
#         break

# #no.2
# def number_to_int():
#     try:
#         n = input('숫자를 입력해주세요:')
#         n1=int(n)
#         n_1=1/n1
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')
#     except ValueError:
#         print('값이 잘못 입력 되었습니다.',n)
# number_to_int()

#no.3
# def div_100():
#     try:
#         n=int(input('정수:'))
#         print(100/n)
#     except Exception as e:
#         print(f'오류:{type(e).__name__}, 설명: {e}')

# div_100()

#no.4
try:
    f = open('b.txt','r')
    print(f.read())
except FileNotFoundError:
    print('파일이 없습니다.')
finally:
    f.close()
    print('종료합니다.')

# #no.5
# def warn():
#     try:
#         n= int(input('나이:'))
#         if n<=0:
#             raise Exception('0보다 작거나 같음')
#     except Exception as e:
#         print('에러:',e)
#     except ValueError as e:
#         print(f'에러:{type(e).__name__},설명 : {e}')
# warn()

# #no.6
# def warn():
#     try:
#         n= int(input('나이:'))
#         if n<=0:
#             raise Exception('0보다 작거나 같음')
#     except Exception as e:
#         print('에러:',e)
#     # except ValueError as e:
#     #     print(f'에러:{type(e).__name__},설명 : {e}')
# warn()

# #no.7
# def exceptino_chaining():
#     try:
#         file_name=input('파일 이름:')
#         file = open(file_name,'r')
#         print(file.read())
#     except FileNotFoundError as e:
#         raise FileNotFoundError('파일을 열 수 ') from e
# try:
#     exceptino_chaining()
# except FileNotFoundError as e:
#     print(e)
#     print('원래의 예외:',e.__cause__)


# #no.8
# def ignore_exception():
#     try:
#         num = int(input('숫자를 입력하세요:'))
#         print(f'입력된 숫자: {num}')
#     except ValueError:
#         pass
#     print('종료')
# ignore_exception()