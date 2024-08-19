#4
print('no.4')
print("")
print("류호재", end=" ")
print(2001,2,1,sep="/")

#7
print('no.7')
print("")
print("안녕하세요. 같이 파이썬을 실습해요.\n")
print("\t앞에 공간을 띄우세요.")
print("\t\t두번을 띄워보세요.")

#11
print('no.11')
print("")
name= '류호재'
text=f'안녕하세요, {name}님!'
print(text)

#12
print('no.12')
print("")
A, B =5, 10
sum = A+B
text=f'{A}와 {B}의 합은 {sum}입니다.'
print(text)

#15
print("no.15")
print("")
print('Hello','world!','This','is','Python',sep=' ',end='.')

#16
print("no.16")
print("")
print('item'.rjust(10),'count'.rjust(10),'price'.rjust(10),end='\n')
print('pen'.rjust(10),'20'.rjust(10),'100'.rjust(10),end='\n')
print('note'.rjust(10),'4'.rjust(10),'80'.rjust(10),end='\n')
print('eraser'.rjust(10),'100'.rjust(10),'75'.rjust(10),end='\n')

#17
print('no.17')
print("")
korean, math, science = 90, 95, 100
sum= korean + math + science
averae = sum / 3
print('\t국어\t',korean)
print('\t수학\t',math)
print('\t과학\t',science)
print('\t합계\t',sum)
print('\t평균\t',averae)

#19
print('no.19')
print("")
name = input("이름을 입력하세요: ")
age = int(input('나이를 입력하세요: ')) #입력된 숫자 캐릭터를 정수로 변환
num = int(input('숫자를 입력하세요: '))
text=f'\"안녕하세요, [{name}]님! 당신은 [{age}]살입니다.\"'
print(text)
text=f'\"[{num}]년 후에는 [{age+num}]살이 됩니다.\"'
print(text)

#20
print('no.20')
print("")
total = 298
current = 50
per = 15.79
print('\t시가총액\t\t',total,'조',sep='')
print('\t현재가\t\t\t',current,',000원',sep='')
print('\tPER\t\t\t',per,sep='')
print(type(total))

#22
print('no.22')
print("")
print("************")
print("************")
print("************")
print("**  ****  **")
print("***  ***  ***")
print("****  * ****")
print("*****  *****")
print("*****  *****")
print("*****  *****")
print("************")
print("************")
