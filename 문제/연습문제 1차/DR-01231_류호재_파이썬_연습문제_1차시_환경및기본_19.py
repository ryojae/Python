name = input("이름을 입력하세요: ")
age = int(input('나이를 입력하세요: ')) #입력된 숫자 캐릭터를 정수로 변환
num = int(input('숫자를 입력하세요: '))
text=f'\"안녕하세요, [{name}]님! 당신은 [{age}]살입니다.\"'
print(text)
text=f'\"[{num}]년 후에는 [{age+num}]살이 됩니다.\"'
print(text)
