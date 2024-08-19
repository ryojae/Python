# #no.1
# for i in range(1,11):
#     print(i)

# #no.2
# while True:
#     try:
#         n = int(input("정수를 입력하세요: "))
#         print(n)
#         break
#     except:
#         print('다시 입력해주세요')

# #no.3
# try:
#     s = input("정수를 입력하세요: ")
#     n = int(s)
#     print(n)
# except:
#     print('숫자를 입력하지 않았어요.')

# #no.4
# import sys
# try:
#     file_name=input('파일 이름:')
#     with open(file_name,'r') as file:
#         lines = file.readlines()
# except FileNotFoundError:
#     print('파일이 없습니다.')
#     try:
#         file_name=input('파일 이름:')
#         with open(file_name,'r') as file:
#             lines = file.readlines()
#     except:
#         print('파일이 없습니다.')
#         print('종료합니다.')
#         sys.exit()

# #no.5
# #1
# try:
#     A = [1, 2, 3]
#     A[3]
# except IndexError:
#      print('Index Error')
# except Exception as e:
#     print(type(e))
# #2
# try:
#       {'fb': 11, 'bb': 9, 'vb': 6}['foot']
# except KeyError:
#      print('Key Error')
# except Exception as e:
#       print(type(e))
# #3
# try:
#       pl = 'python' + 3
# except TypeError:
#      print('Type Error')
# except Exception as e:
#       print(type(e))

# #no.6
# def divicde(x, y):
#     answer = x / y
   
#     return answer
# while 1:
#     try:
#         x = int(input('숫자1:'))
#         y= int(input('숫자2:'))
#         answer=divicde(x,y)
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')
#         break
#     except:
#         print('오류가 발생했습니다.')
#         break
#     else:
#         print(f'결과: {answer}')

#no.7
# #1
# try:
#     print(int("abc"))
# except Exception as e:
#     print(f'예외 발생 이름: {type(e)}')
#     print(f'예외 발생 이유: {e}')
# else:
#     print('오류 없음')
# finally:
#     print('예외 처리가 잘되는군요!')
# #2
# try:
#     print(int("10"))
# except Exception as e:
#     print(f'예외 발생 이름: {type(e)}')
#     print(f'예외 발생 이유: {e}')
# else:
#     print('\t잘 실행됐습니다.')
# finally:
#     print('\t예외 처리가 잘되는군요!')

# #no.8
# try:
#     s=input('정수를 입력하시오')
#     n=int(s)
# except ValueError as e:
#     print(f'에러: {type(e)}')
# else:
#     print('에러가 없습니다.')
# finally:
#     print('끝입니다.')

# #no.9
# file_name=input('파일 이름:')
# try:
#     with open(file_name,'r') as f:
#         s=f.readlines()
#         print(s)
# except FileNotFoundError as e:
#     print(type(e))
# else:
#     print('에러 없음')
# finally:
#     print('끝')

# #no.10
# def calculator():
#     try:
#         num1 = float(input("첫 번째 숫자를 입력하세요: "))
#         num2 = float(input("두 번째 숫자를 입력하세요: "))
#         operator = input("연산자를 입력하세요 (+, -, *, /): ")
#         if operator == '+':
#             answer = num1+num2
#         elif operator == '-':
#             answer = num1-num2
#         elif operator == '*':
#             answer = num1*num2
#         elif operator =='/':
#             answer = num1/num2
#     except ValueError:
#         print(f'잘못 입력하였습니다. num1:{num1},num2:{num2}')
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')
#     else:
#         print('계산이 성공하였습니다.')
#         print(f'결과: {answer}')
#     finally:
#         print('종료되었습니다.')
# calculator()

#no.11
def sum_all():
    sum=0
    number=input('숫자를 입력해주세요:').split(',')
    for i in range(0, len(number)):
        try:
            n=int(number[i])
            sum += n
        except:
            print(f'{number[i]}는 숫자가 아닙니다.')
    print(f'총 합은 {sum}입니다.')
sum_all()
