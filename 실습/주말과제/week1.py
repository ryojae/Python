# #no.1
# num = input('0~9까지의 숫자 중 하나를 입력하시오:')
# for i in range(0,10):
#     for j in range(0,10):
#         print(num,end='')
#     print('\n')

#no.2
num = input('0~9까지의 숫자 중 하나를 입력하시오:')
print('정방행렬')
for i in range(0,10):
    for j in range(0,10):
        print(num,end='')
    print('\n')
print('정삼각형')
for i in range(0,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for j in range(-1,i*2):
        print(num,end='')
    print('\n')

# #no.3
# s=input('문자열을 입력해주세요:')
# index_num=int(input('참조하고 싶은 문자의 위치 입력(0~16)>>'))
# if 0<=index_num<=16:
#     print('문자열:',s,'길이:',len(s))
#     print(f'{index_num+1}번째 문자: {s[index_num]}')
# else:
#     print('잘못 입력했습니다.')

# #no.4
# hour, minute = map(int, input('알람 시간과 분을 입력해주세요:').split())
# if minute >= 45:
#     minute -= 45
#     print(f'바뀐 알람의 시간은 {hour}시 {minute}분입니다.')
# else:
#     if hour ==1:
#         hour = 12
#     else:
#         hour -= 1
#     minute = (60+minute)-45
#     print(f'바뀐 알람의 시간은 {hour}시 {minute}분입니다.')  

# #no.5
# s1 = input('첫번째 문자열을 입력해주세요:')
# s2 = input('두번째 문자열을 입력해주세요:')
# if sorted(s1) == sorted(s2):
#     print(f'{s1}과 {s2}는 순열관계입니다.')
# else:
#     print(f'{s1}과 {s2}는 순열관계가 아닙니다.')