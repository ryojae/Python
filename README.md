Python  -  프로그래밍, 파이썬, 주석문

​

프로그래밍 - 프로그램을 계획, 작업의 순서를 정하거나 실행하는 것

                     '주어진 문제를 해결하기 위해' 작업의 순서를 계획하고 수행하는 것

프로그래밍의 핵심 - 요구사항 분석, 알고리즘을 찾아야 함, 검수

프로그래밍언어의 요소 - 입력, 출력, 순차, 조건, 반복, 재사용이 있다.

​

​

Python

- 컴퓨터보다 사람이 이해하기 쉽게 만들어진 언어로 고수준 프로그래밍 언어이다.

- 위에서 아래로 순차적으로 진행하는 인터프리터 언어이며 문법이 쉽다.

- 객체 지향 언어이고 함수형 언어의 일부 기능을 지원한다.

- 다양한 분야의 라이브러리를 가지고 있다.

- 하지만 실행속도가 느린 단점도 존재한다.

​

VS code

앞으로 ubunut22.04에서 VS code를 활용하여 python 코드를 작성하도록 하겠다.

설치

시스템 업데이트

sudo apt update 

sudo apt upgrade -y

패키지 설치

sudo apt install software-properties-common apt-transport-https wget -y

저장소 가져오기

sudo apt install software-properties-common apt-transport-https wget -y

​

echo deb [arch=amd64 signed-by=/usr/share/keyrings/vscode.gpg] https://packages.microsoft.com/repos/vscode stable main | sudo tee /etc/apt/sources.list.d/vscode.list

시스템 업데이트

sudo apt update 

Visual Studio code 설치

sudo apt install code

주석문

#(한줄만 주석처리) 혹은 ctrl+/(단축키) 혹은 '''   '''(여러 줄 주석처리)을 활용해서 주석 처리가  가능하다.

​

Print

print() 를 통해 괄호 안에 원하는 문구를 터미널 창에 출력이 가능하다.

괄호 안에 문자열과 변수 모두 입력이 가능하다.

print(a,b,sep='',end='')를 사용하여  출력이 가능하다.

sep를 활용하여 ',' 부분에 기본 값인 공백 대신 원하는 값을 입력이 가능하다.

end를 활용하여 문장 마지막에 기본 값인 '\n' 대신 원하는 값을 입력이 가능하다.

 

Python  -  자료형

​

다양한 자료형으로 정수, 실수, 문자열이 존재한다.

정수, 실수의 경우 연산이 가능하고 문자열의 경우 + 혹은 *가 가능은 하지만 기존 연산의 개념보다는 문자열 추가 혹은 문자열 반복의 의미로 적용된다.

​

정수와 문자열의 경우 표현 범위의 제한이 없지만 실수의 경우 4.9*10^-324 ~ 1.8*10^308의 범위 제한이 존재한다.

​

이스케이프 시퀀스

\n - 줄바꿈문자

\t - 탭 문자

\\ - 백슬래시

\' - 작은 따옴표

\" - 큰 따옴표

​

불린 자료형

True 와 False 가 존재하며 각각 1과 0으로도 구별이 가능하다.

​

None 상수값

파이썬에만 존재하는 NoneClass 자료형을 나타내는 상수값으로 C와 Java의 null과 같은 역할을 한다.

​

type()

type('a')을 사용하면 <class'str'>이 나오는 등 원하는 값의 자료형을 확인할 수 있다.

​

리터럴

직접 명시된 숫자값이나 문자열

​

int(), float(), str()

원하는 변수의 자료형 값을 변환이 가능하고 앞에서부터 정수, 실수, 문자열의 역할을 한다.

각각의 자료형은 변환이 가능하나 문자열을 정수나 실수로 변경할 때 숫자만 포함이 되어있어야한다.

​

산술 연산

+ - 덧셈

-  - 뺄셈

* - 곱셈

/ - 실수 나눗셈

// - 정수 나눗셈

% - 정수의 나머지

** - 거듭제곱

​

연산자의 우선 순위

{()} -> {**} -> {*, /, //, %} ->{+, -}

​

복소수

complex(a,b) 혹은 a+bj를 사용하여 복소수 표현이 가능하다.

​

Python  -  변수의 사용자 입력

​

변수 이름을 지을때 공백이나 특수 문자가 포함이 되거나 숫자로 시작하면 안된다.

​

복합 연산자

a += b -> a = a + b

a -= b -> a = a - b

a *= b -> a = a * b

a /= b -> a = a / b

a //= b -> a = a // b

a %= b -> a = a % b

a **= b -> a = a ** b

​

형식 지정자

%s(문자열), %d(정수), %f(실수)를 문자열에 넣어 출력이 가능하다.

다음과 같이 입력한다.

print('%s %d %10.1f' % (s,d,f))

%10.1f 의 경우 전체 자릿수를 10자리로 지정하고 소수점 한자리까지 출력하도록 한다.

​

f-string

print(f'{s}')를 활용하여 변수를 바로 출력하는 것도 가능하다.

f{s:^10.1f}등을 통하여 가운데 정렬 소수점 한자리 출력등도 조절이 가능하다

​

input()

input()을 통하여 사용자에게 입력 받을 수 있는데 이때 입력 받은 값들은 문자열의 형식으로 저장된다.

input().split()을 통해 공백을 기준으로 값을 나누어 입력이 가능하고 이렇게 입력받은 값 전부를 int로 바꾸기 위해 map(int,input().split())의 혁식으로 코드를 작성해 줄 수 있다.

 

Python  -  조건문, 비교연산자, 논리 연산자

​

if를 활용하여 조건문을 생성할 수 있다.

if 조건1:

조건1에 합당하면 들여쓰기 된 명령어를 실행하게 되고

elif 조건 2:

조건1에 해당하지 않고 조건 2에 해당하면 elif 밑의 들여쓰기된 명령어를 실행하게 된다.

else:

조건1과 조건2 둘다 합당하지 않으면 else 밑의 들여쓰기 된 명령어를 실행하게 된다.

중첩 if 도 가능하다

​

비교 연산의 경우 ==이 같다 이고 !=는 같지 않다 이다. 나머지 비교연산은 기존의 비교 연산과 동일하다.

문자열도 비교가 가능하고 True or False로도 조건문 실행이 가능하다.

​

논리 연산자

and - 모두 참이어야 참

or - 하나라도 참이면 참

not - 참은 거짓으로 거짓은 참으로

​

Python  -  프로그래밍, 파이썬, 주석문

​

len()을 활용해 문자열의 길이를 확인할 수 있다.

​

인덱스를 활용하면 첫 글자부터 0에서 증가하고 마지막 글짜부터는 -1부터 감소한다.

s=s[::-1]을 활용하면 reverse 또한 가능하다.

​

s.startswith('a')를 활용하여 시작이 a인지 확인이 가능하며 s.endswith('a')를 활용하여 끝이 a인지 확인이 가능하다.

​

in을 활용하여 문자열에 원하는 값이 있는지 확인 가능하다.

​

s.index() - 문자열이 어디있는지 알려주고 없을 경우 에러 발생

s.find()- 문자열이 어디있는지 알려주며 없을 경우 -1을 반환

s.rindex(), s.rfind() - 오른쪽부터 검색

s[1:3] - s 문자열의 1번부터 2번까지 추출

s.strip() - 양 끝에서부터 있는 원하는 문자열을 제거

s.lstrip(), s.rstrip() - 각각 왼쪽, 오른쪽 부터 원하는 문자열을 제거

s.replace() - 문자열에서 해당하는 값을 원하는 문자열로 변경

s.isalnum() - 문자열이 알파벳과 숫자로만 구성되어 있는지 확인

s.isalpha() - 문자열이 알파벳만으로 구성되어 있는지 확인

s.isdigit(), s.isnumeric() - 문자열이 숫자로만 구성되어 있는지 확인

s.islower() - 문자열이 영문 소문자로만 구성되어 있는지 확인

s.isupper() - 문자열이 영문  대문자로만 구성되어있는지 확인

s.upper() - 문자열을 대문자로 변환

s.lower() - 문자열을 소문자로 변환

s.swapcase() - 대문자는 소문자로 소문자는 대문자로 변환

s.count(str) - 문자열에 str이 몇개 있는지 세줌

s.count(str,start,end) - 지정된 범위에서 몇개 있는지 세줌

​

인코딩과 디코딩

인코딩 - 문자를 이진코드로 변환     s.encode()

디코딩 - 이진 코드를 문자로 변환     s.decode()

s.encode().hex() - 헥스로 인코딩

bytes.fromhex(s).decode() - 헥스를 문자로 디코딩

Python  -  함수

​

함수 

정해진 일을 처리하기 위해 작성된 코드의 묶음

반복 작업을 하기에 용이

입력값은 전달인자라고 하고 출력의 경우 return을 사용하여 반환 가능

전달인자가 없다면 빈 괄호를 해도 가능

def를 활용하여 먼저 함수를 선언 해줘야한다.

전달인자 부분에 *args를 사용해 가변 인자로서 입력값을 받을 수 있다.

​

전역 변수

변수의 경우 유효범위가 존재하는데 모든 영역에서 사용이 가능한 것은 global 즉, 전역 변수이다.

함수 내부에서 만들어진 변수는 local 지역 변수로 함수 내부에서만 사용이 가능해 사용할 때 주의가 필요하다.

​

재귀 호출

함수에서 자기 자신인 함수를 다시 호출하는 것을 의미

재귀함수의 경우 탈출하는 경우가 존재해야함

팩토리얼, 피보나치 수열, 하노이의 탑 등과 같은 알고리즘에서 재귀함수를 사용

​

swapcase()

s.swapcase()를 사용해서 대문자는 소문자로 소문자는 대문자로 변경해줄 수 있다

​

re 모듈

re 모듈을 활용해서 문자열에서 패턴을 찾고, 매칭되는 부분을 추출하거나 대체할 수 있다


re.split()을 활용해서 다음과 같이 분할도 가능하다.


 

Python  -  반복문

while 조건:

조건에 부합한 경우 반복하는 while 반복문이다.

이를 활용해 똑같은 코드를 반복할 필요를 줄일 수 있게 된다.

​

for 변수 in 순서가있는 객체

순서가 있는 객체의 순서를 따라 변수가 설정된다

range(0,n,i)의 경우 0부터 n-1까지의 값을 i단위로 증가하게 된다

​

중첩 반복문

반복문 안에 반복문을 넣는 것이 가능하다

​

break와 continue

break의 경우 반복문을 종료

continue의 경우 뒤에 구문을 무시하고 다시 반복문을 시작

​

Python  -  리스트, 튜플

리스트

변경 가능한 자료구조

[]의 형태를 가지고 있고 크기를 동적으로 조절 가능하며 요소를 치환해서 변환이 가능

a.append를 통해 리스트 요소를 추가할 수 있다.

+를 활용해 리스트를 연결이 가능하고 *를 활용해 요소들을 반복시킬 수 있다

a[인덱스]=값 의 형태를 활용해 값 변경이 가능하다

​

인덱싱

처음 요소는 0부터 해서 +1씩 증가하고 

오른쪽에서부터 보면 -1부터 왼쪽으로 1씩 감소

​

슬라이싱

a[i:j]의 형식을 활용해 리스트 a의 i부터 j-1을 추출할 수 있다

​

리스트 요소 제거

del(a[i:j]), a[i:j]=[], a.remove(값)을 활용해 리스트 요소를 제거할 수 있다

​

insert(x,y)를 활용해서 x의 위치에 y 값을 삽입한다.

​

in을 활용해서 값이 요소로 존재하는지 확인가능하고 있으면 True 없으면 False로 반환된다

​

튜플

튜플의 경우 변경할 수 없는 자료 구조

()의 형태를 가짐

값이나 구조를 변경할 수 없는 것을 제외하고는 리스트처럼의 작업이 가능하다

 

Python  -  파일일

file을 액세스해서 열어 작업이 가능하다.

python 파일이 있는 주소를 기준으로 파일을 탐색하고 open을 통해 열 수 있다.

open(file_name,a)

a 부분에 'r'을 넣으면 읽기 모드, 'w'를 넣으면 작성 모드, 'a'를 넣으면 추가 모드이다.

파일을 열 때만 모드를 지정이 가능하고 도중에 변경은 불가능하다

파일을 오픈하게 된 경우 다시 close()를 활용하여 닫아줘야하는 불편함이 있다.

​

with open(file_name, a) as f

이 구문을 통해 파일을 열어주면 들여쓰기가 끝나는 시점에서 알아서 file을 닫아준다

​

f.read()를 통해 파일에 적힌 정보를 불러올 수 있다

f.readline()을 통해 한줄만 읽어오는 것이 가능하고 

f.readlines()를 통해 모든 줄을 리스트의 형태로 받아올 수 있다.

f.write()를 통해 파일에 작성이 가능하다

​

csv(comma seperated value)는 ,를 통해 구분되어있는 값을 의미하고

import csv와 csv.writer()를 통해 접근 및 작성이 가능하다

​

Python  -  예외 처리

​

코드를 작성하다보면 오류가 발생하고 오류가 생기게 되면 코드가 정지하게 된다.

오류는 문법 오류, 논리 오류, 실행 오류가 있다

예외처리를 통해 이를 방지할 수 있다

try, except를 통해 try 안의 코드를 실행해보고 에러가 뜨면 except의 코드를 실행하게 된다.

그리고 except Exception 이 코드의 Exception 부분에 원하는 에러를 넣게 되면 

해당 에러의 경우에 대해서만 예외 처리가 가능하다

​

raise를 통해 직접 에러를 발생시킬 수도 있고 원하는 이름으로 에러를 발생시킬 수도 있다

re-raise의 경우 



딕셔너리 (Dictionary)

딕셔너리의 특징

키(key)와 값(value)으로 구성된 한 쌍의 데이터를 담을 수 있는 자료구조입니다.

중복된 키는 허용되지 않습니다.

키는 수정 불가능한(immutable) 자료형만 사용할 수 있으며, 값은 변경 가능합니다.

중괄호 {}로 표현합니다.

요소에 대한 접근은 [] 또는 get() 함수를 사용합니다.

값 추가 또는 변경은 딕셔너리_이름[키] = 값 형태로 수행합니다.

요소 삭제는 del 함수를 사용합니다.

딕셔너리 예

d = { "name": "홍길동", "age": 20, "취미": ["영화 감상", "게임", "독서"] }
print(d["name"])  # 홍길동
print(d.get("age"))  # 20
딕셔너리 요소 개수 확인

len() 함수를 사용하여 딕셔너리의 요소 개수를 확인합니다.

d = { "name": "홍길동", "age": 20 }
print(len(d))  # 2
딕셔너리 요소 추가 및 수정

단일 요소 수정

d = { 1: 2, False: 20 }
d[1] = 3
d["new_key"] = "new_value"
print(d)  # {1: 3, False: 20, "new_key": "new_value"}
여러 요소 한꺼번에 수정

d.update({1: 4, "new_key": "updated_value"})
print(d)  # {1: 4, False: 20, "new_key": "updated_value"}
딕셔너리와 for 문

딕셔너리의 키 또는 값을 순회할 수 있습니다.

d = { 1: 2, False: 20 }
for key in d:
    print(key, d[key])
딕셔너리 삭제

특정 요소 삭제

del d[1]
print(d)  # {False: 20}
딕셔너리 전체 삭제

d.clear()
print(d)  # {}
집합 (Set)

집합의 특징

순서가 없고, 중복을 허용하지 않는 자료구조입니다.

중괄호 {}로 표현됩니다.

특정 요소에 직접 접근할 수 없습니다.

집합 연산(합집합, 교집합, 차집합 등)을 지원합니다.

집합 생성 방법

빈 집합 생성

s = set()
하드 코딩

s = {1, 2, 3}
set() 함수에 iterable 객체 전달

s = set([1, 2, 3])
s = set("hello")
집합 요소 추가 및 삭제

요소 추가

s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}
여러 요소 추가

s.update([4, 5])
print(s)  # {1, 2, 3, 4, 5}
요소 삭제

s.remove(1)
print(s)  # {2, 3, 4, 5}
집합 연산

교집합

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # {2, 3}
합집합

print(s1 | s2)  # {1, 2, 3, 4}
차집합

print(s1 - s2)  # {1}
대칭 차집합

print(s1 ^ s2)  # {1, 4}
실습문제 풀이

실습문제 1

다음 문자열에서 각 알파벳 문자들의 빈도수를 구하는 프로그램 작성

def count_characters():
    sentences = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, 
    purus lectus malesuada libero, sit amet commodo magna eros quis urna. 
    Nunc viverra imperdiet enim."""
    d = {}
    for char in sentences.lower():
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    for k, v in d.items():
        if k == ' ':
            k = "SPACE"
        elif k == '\t':
            k = "TAB"
        elif k == '\n':
            k = "NEWLINE"
        print(f"{k}:{v}")

count_characters()
실습문제 2

사용자로부터 이름과 나이를 입력받아 딕셔너리에 저장하고, 저장된 딕셔너리를 출력하는 프로그램 작성

def store_in_dictionary():
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    person = {"name": name, "age": age}
    print(person)
    print(type(person))

store_in_dictionary()
실습문제 3

사용자로부터 키 값을 입력받고, 해당 키에 대한 값을 딕셔너리에서 찾아 출력하세요.

def access_dictionary():
    data = {'name': 'Alice', 'age': 30}
    key = input("찾고 싶은 키를 입력하세요: ")
    try:
        print(f"{key}의 값: {data[key]}")
    except KeyError:
        print(f"오류: {key}는 존재하지 않는 키입니다.")

access_dictionary()
실습문제 4

사용자로부터 여러 개의 숫자를 입력받아 집합을 생성하고 출력하는 프로그램 작성

def create_and_print_set():
    numbers = input("숫자들을 공백으로 구분하여 입력하세요: ").split()
    number_set = set(numbers)
    print("생성된 집합:", number_set)

create_and_print_set()
실습문제 5

사용자로부터 딕셔너리에 추가할 키와 값을 입력받고, 기존 딕셔너리에 추가한 후 최종 딕셔너리를 출력하세요.

def update_dictionary():
    data = {'name': 'Alice', 'age': 30}
    key = input("추가할 키를 입력하세요: ")
    value = input("추가할 값을 입력하세요: ")
    data[key] = value
    print("업데이트된 딕셔너리:", data)

update_dictionary()
실습문제 6

사용자로부터 삭제할 키를 입력받고, 해당 키를 딕셔너리에서 삭제한 후 결과를 출력하세요.

def delete_from_dictionary():
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    key = input("삭제할 키를 입력하세요: ")
    if key in data:
        del data[key]
        print("삭제 후 딕셔너리:", data)
    else:
        print(f"오류: {key}는 존재하지 않는 키입니다.")

delete_from_dictionary()
실습문제 7

주어진 딕셔너리에서 모든 키를 리스트로 만들어 출력하세요.

def list_dictionary_keys():
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    keys = list(data.keys())
    print("딕셔너리의 키들:", keys)

list_dictionary_keys()
실습문제 8

딕셔너리의 모든 아이템을 순회하면서 키와 값을 출력하는 프로그램을 작성하세요.

def iterate_dictionary_items():
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    for key, value in data.items():
        print(f"{key}: {value}")

iterate_dictionary_items()
실습문제 9

두 개의 딕셔너리를 병합하고 결과를 출력하는 프로그램을 작성하세요.

def merge_dictionaries():
    dict1 = {'name': 'Alice', 'age': 30}
    dict2 = {'city': 'New York', 'country': 'USA'}
    dict1.update(dict2)
    print("병합된 딕셔너리:", dict1)

merge_dictionaries()
실습문제 10

사용자로부터 키를 입력받고, 해당 키로 딕셔너리에서 값을 조회합니다. 키가 없는 경우 'Not Found'를 기본값으로 출력하세요.

def get_with_default():
    data = {'name': 'Alice', 'age': 30}
    key = input("값을 조회할 키를 입력하세요: ")
    value = data.get(key, 'Not Found')
    print(f"{key}: {value}")

get_with_default()
실습문제 11

주어진 딕셔너리에서 값이 20보다 큰 아이템만 포함하는 새 딕셔너리를 생성하여 출력하세요.

def filter_dictionary():
    data = {'Alice': 25, 'Bob': 19, 'Cathy': 34, 'Dan': 20}
    filtered_data = {k: v for k, v in data.items() if v > 20}
    print("값이 20보다 큰 아이템:", filtered_data)

filter_dictionary()
실습문제 12

사용자로부터 숫자 요소를 입력받아, 집합에 추가한 후, 집합을 출력하는 프로그램을 작성하세요.

def add_to_set():
    my_set = {1, 2, 3}
    new_element = int(input("추가할 요소를 입력하세요: "))
    my_set.add(new_element)
    print("업데이트된 집합:", my_set)

add_to_set()
실습문제 13

사용자로부터 요소를 입력받아 집합에서 해당 요소를 제거한 후, 집합을 출력하는 프로그램을 작성하세요. 요소가 집합에 없는 경우 적절한 메시지를 출력하세요.

def remove_from_set():
    my_set = set([1, 2, 3, 4, 5])
    element = int(input("제거할 요소를 입력하세요: "))
    try:
        my_set.remove(element)
    except KeyError:
        print("해당 요소가 집합에 없습니다.")
    print("업데이트된 집합:", my_set)

remove_from_set()
실습문제 14

두 집합을 생성하고, 두 집합의 교집합을 계산하여 출력하는 프로그램을 작성하세요.

def intersection_of_sets():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    intersection = set1 & set2
    print("두 집합의 교집합:", intersection)

intersection_of_sets()
실습문제 15

두 집합의 합집합을 계산하여 출력하는 프로그램을 작성하세요.

def union_of_sets():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union = set1 | set2
    print("두 집합의 합집합:", union)

union_of_sets()
실습문제 16

한 집합에서 다른 집합을 빼고 결과를 출력하는 프로그램을 작성하세요.

def difference_of_sets():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}
    difference = set1 - set2
    print("집합1에서 집합2를 뺀 차집합:", difference)

difference_of_sets()
실습문제 17

두 집합의 대칭 차집합(양쪽 집합 중 어느 한쪽에만 속하는 요소들의 집합)을 계산하여 출력하는 프로그램을 작성하세요.

def symmetric_difference_of_sets():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    symmetric_difference = set1 ^ set2
    print("두 집합의 대칭 차집합:", symmetric_difference)

symmetric_difference_of_sets()
실습문제 18

사용자로부터 여러 개의 아이템을 입력받아, 각 아이템이 몇 번 등장하는지 딕셔너리로 만들어 출력하세요.

def count_items():
    items = input("아이템을 공백으로 구분하여 입력하세요: ").split()
    count_dict = {}
    for item in items:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    print("아이템 카운트:", count_dict)

count_items()
실습문제 19

사용자로부터 여러 개의 숫자를 입력받고, 중복을 제거한 후, 각 숫자가 몇 번 입력되었는지 출력하세요.

def remove_duplicates_and_count():
    numbers = map(int, input("숫자들을 공백으로 구분하여 입력하세요: ").split())
    number_dict = {}
    for number in numbers:
        if number in number_dict:
            number_dict[number] += 1
        else:
            number_dict[number] = 1
    unique_numbers = set(number_dict.keys())
    print("고유 숫자:", unique_numbers)
    print("각 숫자의 카운트:", number_dict)

remove_duplicates_and_count()
실습문제 20

두 문자열을 입력받고, 두 문자열에 공통으로 포함된 문자들을 출력하세요.

def common_characters():
    string1 = input("첫 번째 문자열을 입력하세요: ")
    string2 = input("두 번째 문자열을 입력하세요: ")
    set1 = set(string1)
    set2 = set(string2)
    common_chars = set1 & set2
    common_chars = sorted(common_chars)
    print("두 문자열에 공통으로 포함된 문자:", common_chars)

common_characters()
딕셔너리와 집합의 기본 개념, 생성, 요소 추가/삭제, 순회, 연산 등의 다양한 조작 방법을 설명하고 있습니다. 실습 문제를 통해 딕셔너리와 집합의 사용법을 익히도록 돕습니다.

​

객체지향 프로그래밍 (Object-Oriented Programming, OOP)

프로그래밍 패러다임

프로그램을 작성하는 방향과 구조를 정하는 방법.

파이썬은 절차적 프로그래밍(procedural programming)과 객체지향 프로그래밍(object-oriented programming)을 지원합니다.

절차적 프로그래밍의 문제점

데이터와 동작(기능)이 분리됨.

재사용성이 떨어짐.

예: 전화 거는 과정을 절차적 프로그래밍으로 작성할 때 데이터와 함수가 분리되어 유지 보수가 어려움.

객체지향 프로그래밍의 장점

데이터와 코드를 객체로 함께 구성하여 한 개 자료형으로 취급.

클래스(class)를 사용하여 데이터와 코드를 묶음.

높은 재사용성, 캡슐화, 상속, 다형성 등을 제공.

객체와 클래스

객체: 프로그램이 실행될 때 클래스로부터 생성되는 실체.

클래스: 객체의 속성과 기능을 정의하는 설계도.

클래스의 구성 요소

속성(변수)과 기능(함수)을 포함.

클래스는 객체를 생성하기 위한 설계도.

객체는 클래스로부터 생성되고, 인터페이스로 제공되는 함수들을 호출하여 사용.

파이썬의 모든 자료형은 클래스

파이썬의 모든 자료형은 클래스 자료형.

type() 명령을 이용하여 확인 가능.

객체지향 프로그래밍의 특성

추상화: 실존하는 사물 또는 개념을 컴퓨터에서 처리할 수 있도록 축약.

캡슐화: 필요한 정보와 인터페이스만 공개하고 나머지 구현 내용을 감춤.

재사용성: 클래스는 절차적 프로그래밍의 함수보다 재사용성이 높음.

상속: 기존 클래스 코드를 수정하지 않고 클래스의 기능을 확장하거나 다르게 만듦.

다형성: 동일한 함수가 다르게 작동. 상속 관계의 여러 클래스에서 동일한 명칭으로 구현된 함수들이 각각 다르게 동작.

클래스 선언 및 사용

클래스 선언

class 클래스_이름:
    def __init__(self, 매개_변수_리스트):
        멤버_변수_생성

    def 메소드_이름(self, 매개_변수_리스트):
        코드_블록
객체 생성

객체_변수_이름 = 클래스_이름(인자)
클래스의 인스턴스 메소드

첫 번째 매개 변수로 self를 지정해야 함.

클래스 내부에서 메소드 호출 시 self.함수_이름으로 호출.

클래스 외부에서 메소드 호출 시 객체_이름.함수_이름으로 호출.

실습문제 풀이

실습문제 1

사각형 또는 원의 면적 계산에 필요한 데이터를 3회 입력받고, 면적을 계산하는 프로그램

import math

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcArea(self):
        return (self.x2 - self.x1) * (self.y1 - self.y2)

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def calcArea(self):
        return math.pi * self.r * self.r

shapeList = []
for i in range(3):
    s = input("도형 모양을 입력하세요 (사각형/원): ")
    if s == "사각형":
        x1 = int(input("왼쪽 상단의 x좌표를 입력: "))
        y1 = int(input("왼쪽 상단의 y좌표를 입력: "))
        x2 = int(input("오른쪽 하단의 x좌표를 입력: "))
        y2 = int(input("오른쪽 하단의 y좌표를 입력: "))
        shapeList.append(Rectangle(x1, y1, x2, y2))
    elif s == "원":
        x = int(input("원의 중심 x 좌표를 입력: "))
        y = int(input("원의 중심 y 좌표를 입력: "))
        r = int(input("원의 반지름을 입력: "))
        shapeList.append(Circle(x, y, r))

for shape in shapeList:
    print(f"면적: {shape.calcArea()}")
실습문제 2

Rectangle과 Circle을 클래스에서 상속받도록 다시 구현

import math

class Shape:
    def __init__(self, shapeStr):
        self.shapeStr = shapeStr

    def getShapeStr(self):
        return self.shapeStr

class Circle(Shape):
    def __init__(self, shapeStr, x, y, r):
        super().__init__(shapeStr)
        self.x = x
        self.y = y
        self.r = r

    def calcArea(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, shapeStr, x1, y1, x2, y2):
        super().__init__(shapeStr)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcArea(self):
        return (self.x2 - self.x1) * (self.y1 - self.y2)

shapeList = []
for i in range(3):
    s = input("도형 모양을 입력하세요 (사각형/원): ")
    if s == "사각형":
        x1 = int(input("왼쪽 상단의 x좌표를 입력: "))
        y1 = int(input("왼쪽 상단의 y좌표를 입력: "))
        x2 = int(input("오른쪽 하단의 x좌표를 입력: "))
        y2 = int(input("오른쪽 하단의 y좌표를 입력: "))
        shapeList.append(Rectangle("사각형", x1, y1, x2, y2))
    elif s == "원":
        x = int(input("원의 중심 x 좌표를 입력: "))
        y = int(input("원의 중심 y 좌표를 입력: "))
        r = int(input("원의 반지름을 입력: "))
        shapeList.append(Circle("원", x, y, r))

for shape in shapeList:
    print(f"도형 모양: {shape.getShapeStr()}")
    print(f"면적: {shape.calcArea()}")
실습문제 3

간단한 Car 클래스를 정의하고, 객체를 생성한 후 속성을 출력하는 프로그램

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

def create_and_print_car():
    my_car = Car("Toyota", "Corolla", 2021)
    print(f"차량 정보: {my_car.year} {my_car.make} {my_car.model}")

# 함수 호출
create_and_print_car()
실습문제 4

Dog 클래스를 정의하고, bark 메소드를 추가하여 객체를 생성하고 메소드를 호출하는 프로그램

class Dog:
    def bark(self):
        print("Woof!")

def make_dog_bark():
    my_dog = Dog()
    my_dog.bark()

# 함수 호출
make_dog_bark()
실습문제 5

Vehicle 클래스를 만들고, 이를 상속받는 Truck 클래스를 정의하는 프로그램

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Truck(Vehicle):
    def __init__(self, make, model, load_capacity):
        super().__init__(make, model)
        self.load_capacity = load_capacity

def create_and_print_truck():
    my_truck = Truck("Ford", "F-150", 1000)
    print(f"트럭 정보: {my_truck.make} {my_truck.model}, 적재 용량: {my_truck.load_capacity}kg")

# 함수 호출
create_and_print_truck()
실습문제 6

MathOperations 클래스를 정의하고, 인스턴스 메소드로 add, 클래스 메소드로 multiply, 스태틱 메소드로 subtract를 구현하는 프로그램

class MathOperations:
    def add(self, a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @staticmethod
    def subtract(a, b):
        return a - b

def perform_operations():
    math_op = MathOperations()
    print("Add:", math_op.add(2, 3))
    print("Multiply:", MathOperations.multiply(4, 5))
    print("Subtract:", MathOperations.subtract(10, 3))

# 함수 호출
perform_operations()
실습문제 7

Account 클래스를 정의하고, balance를 프라이빗 속성으로 갖는 프로그램

class Account:
    def __init__(self, balance):
        self.__balance = balance

    def __update_balance(self, amount):
        self.__balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            print(f"Deposited: ${amount}")
            print(f"New Balance: ${self.__balance}")
        else:
            print("Invalid amount")

# 함수 호출
my_account = Account(100)
my_account.deposit(50)
실습문제 8

BankAccount 클래스를 정의하고, 초기 잔액(balance)을 매개변수로 받아 입금(deposit) 메소드와 출금(withdraw) 메소드를 포함하는 프로그램

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")

# 함수 호출
account = BankAccount(100)
account.deposit(50)
account.withdraw(200)
실습문제 9

Animal 클래스를 정의하고, Dog와 Cat 클래스가 Animal 클래스를 상속받아 speak 메소드를 오버라이드하는 프로그램

class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

# 함수 호출
my_dog = Dog()
my_cat = Cat()
my_dog.speak()
my_cat.speak()
실습문제 10

Product 클래스를 정의하고, 이름(name), 가격(price) 속성을 포함하는 프로그램

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

# 함수 호출
product = Product("Coffee", 5)
print(product.price)  # Output: 5
product.price = -10  # Should raise an error message
product.price = 15
print(product.price)  # Output: 15
객체지향 프로그래밍의 개념과 장점, 클래스와 객체의 정의 및 사용 방법, 상속과 다형성에 대해 설명하며, 다양한 실습 문제를 통해 객체지향 프로그래밍의 주요 개념을 익히도록 돕습니다.

​

모듈(Module)

모듈의 필요성

코드 관리의 용이성: 코드가 길어지면 한 개 파일에 모든 코드를 넣고 관리하는 것이 어려움.

실행의 효율성: 긴 코드를 메모리에 올려서 실행시키는 것은 비효율적.

재사용성: 관련된 함수나 클래스들을 한 개 파일에 묶으면 재사용이 용이해짐.

모듈 만들기

파이썬 함수나 클래스를 작성하고 파일에 저장.

예: Rectangle.py와 Circle.py에 클래스 저장.

모듈 사용법

다른 모듈 파일을 사용하려면 import해야 함.

import 모듈_이름, from 모듈_이름 import 함수_이름 형태로 사용.

모듈에 변수 넣고 수정하기

모듈에 변수를 정의하고 수정할 수 있음.

예: dice2.py에서 변수 minNum, maxNum 수정 가능.

from…import로 모듈 이름 줄이기

from 모듈_이름 import 변수_함수_클래스_이름 형식을 사용해 모듈 이름을 생략하고 함수나 클래스를 사용할 수 있음.

name 변수 활용

파이썬은 코드가 직접 실행될 때 __name__ 변수를 "__main__"으로 지정.

모듈이 import되면 __name__ 변수값이 "__main__"이 아님.

if __name__ == "__main__": 구문을 사용해 직접 실행 시에만 특정 코드가 실행되도록 할 수 있음.

패키지, 라이브러리, 패키지 관리 프로그램

패키지(package)

관련된 모듈들을 묶어놓은 것.

라이브러리

관련된 패키지들을 모아서 한 개의 묶음으로 만든 것.

패키지 관리 프로그램

pip를 사용하여 다른 사람들이 만들어둔 패키지를 쉽게 설치하고 사용 가능.

pip install 패키지_이름, pip uninstall 패키지_이름 명령을 사용.

날짜와 시간 다루기

date 클래스

today(), weekday(), strftime() 함수를 사용하여 날짜 정보를 처리.

예: date.today(), date.strftime("%Y/%m/%d").

time 클래스

특정 시각 정보를 나타냄.

time 모듈은 시간을 다루기 위한 다양한 함수 제공.

경로와 파일 관리 및 파일 목록 뽑기

os 모듈을 사용하여 디렉토리 및 파일을 관리.

os.getcwd(), os.chdir(path), os.mkdir(path), os.listdir(path) 등의 함수를 사용.

실습문제 풀이

실습문제 1

와일드 카드의 파일 이름을 명령행 인자로 요청하면, 현재 작업 디렉토리에서 매칭되는 파일의 목록을 화면에 출력

import glob, sys

def list_files():
    lst = []
    if len(sys.argv) == 1:
        lst = glob.glob("*")
    else:
        lst = glob.glob(sys.argv[1])
    if len(lst) == 0:
        print("매칭되는 파일이 없습니다")
    else:
        for name in lst:
            print(name)

list_files()
실습문제 2

모듈 생성 및 사용: 파이썬 파일을 하나 생성하고, 이 파일에 간단한 함수를 정의하세요. 그리고 다른 파이썬 파일에서 이 함수를 가져와서 사용하세요.

# mymodule.py
def greet(name):
    print(f"Hello, {name}!")

# main.py
import mymodule

mymodule.greet("Alice")
실습문제 3

모듈에서 여러 함수 사용: 모듈을 생성하고 그 안에 두 개의 함수를 정의하세요.

# mathmodule.py
def square(x):
    return x * x

def add(a, b):
    return a + b

# use_mathmodule.py
import mathmodule

print(mathmodule.square(4)) # 16
print(mathmodule.add(5, 3)) # 8
실습문제 4

모듈의 변수 사용: 모듈에 몇 가지 변수를 정의하고, 이를 다른 파일에서 가져와 출력하세요.

# config.py
username = "admin"
password = "secret"

# use_config.py
import config

print(config.username) # admin
print(config.password) # secret
실습문제 5

모듈의 클래스 사용: 모듈에 클래스를 정의하고, 이 클래스의 인스턴스를 생성하여 다른 파일에서 사용하세요.

# personmodule.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# use_personmodule.py
from personmodule import Person

person = Person("Bob", 30)
print(person.greet()) # Hello, my name is Bob and I am 30 years old.
실습문제 6

모듈의 예외 처리: 모듈에 사용자 정의 예외를 정의하고, 이 예외를 다른 파일에서 처리하세요.

# errormodule.py
class MyError(Exception):
    pass

# handle_error.py
from errormodule import MyError

try:
    raise MyError("Something went wrong")
except MyError as e:
    print(e)
실습문제 7

패키지 생성 및 모듈 호출: my_package라는 패키지를 생성하고, 이 안에 utilities.py라는 모듈을 만드세요.

# my_package/utilities.py
def multiply_numbers(a, b):
    return a * b

# main.py
from my_package.utilities import multiply_numbers

result = multiply_numbers(4, 5)
print(f"Result: {result}") # Result: 20
실습문제 8

패키지 내 여러 모듈 사용: my_package 패키지 안에 math_tools.py와 string_tools.py 두 개의 모듈을 만드세요.

# my_package/math_tools.py
def add(x, y):
    return x + y

# my_package/string_tools.py
def capitalize_string(s):
    return s.capitalize()

# main.py
from my_package.math_tools import add
from my_package.string_tools import capitalize_string

print(add(10, 20)) # 30
print(capitalize_string("hello world")) # "Hello world"
모듈의 필요성과 사용 방법, 모듈 내 변수 및 함수의 활용, 패키지와 라이브러리의 개념, __name__ 변수의 활용, 날짜와 시간 다루기, 파일 및 경로 관리 등에 대해 설명하며, 실습 문제를 통해 모듈과 패키지를 사용하는 방법을 익히도록 돕습니다.

​

시퀀스(Sequence)

시퀀스의 정의

시퀀스는 순서가 있는 데이터의 집합입니다.

파이썬에서의 시퀀스는 문자열, 리스트, 튜플 등이 있습니다.

시퀀스 객체의 특징

시퀀스 객체는 인덱싱, 슬라이싱, 길이, 포함 연산 등을 지원합니다.

시퀀스 객체의 요소 개수 구하기

len() 함수를 사용하여 시퀀스 객체의 요소 개수를 구할 수 있습니다.

s = "Hello, World!"
print(len(s))  # 13
인덱스 사용

시퀀스 객체의 특정 위치에 있는 요소에 접근할 때 인덱스를 사용합니다.

인덱스는 0부터 시작하며 음수 인덱스를 사용하면 뒤에서부터 요소에 접근할 수 있습니다.

s = "Hello"
print(s[1])  # 'e'
print(s[-1])  # 'o'
슬라이스 사용

시퀀스 객체의 일부분을 추출할 때 슬라이스를 사용합니다.

[start:end] 형태로 사용하며, start는 포함되고 end는 포함되지 않습니다.

s = "Hello, World!"
print(s[0:5])  # 'Hello'
print(s[7:])  # 'World!'
실습문제 풀이

실습문제 1

파일에서 단어 읽기 및 분석: 텍스트 파일을 읽고, 파일에서 가장 많이 등장하는 단어와 그 빈도를 출력하는 프로그램을 작성하세요.

코드:

def most_frequent_word(filename):
    try:
        with open(filename, encoding="utf-8") as file:
            text = file.read()
        words = text.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_frequent = max(word_count, key=word_count.get)
        return most_frequent, word_count[most_frequent]
    except FileNotFoundError:
        return "File not found."

# 함수 호출
filename = "info.txt"
result = most_frequent_word(filename)
print(f"The most frequent word is '{result[0]}' with {result[1]} occurrences.")
실습문제 2

문자열 시퀀스에서 특정 문자 제거: 주어진 문자열에서 모든 구두점을 제거하고 결과를 반환하세요.

코드:

import string

def remove_punctuation1(input_string):
    sans_punctuation_documents = []
    for i in input_string:
        sans_punctuation_documents.append(i.translate(str.maketrans('', '', string.punctuation)))
    return ''.join(sans_punctuation_documents)

def remove_punctuation2(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

# 함수 호출
sample_text = "Hello, world! How are you doing? It's a great day."
clean_text1 = remove_punctuation1(sample_text)
print("Clean text1:", clean_text1)
실습문제 3

여러 가지 제품의 가격이 리스트로 주어집니다. 모든 제품 가격에 20% 할인을 적용한 후의 가격을 계산하여 출력하세요.

코드:

def apply_discount(prices):
    discount_rate = 0.20
    discounted_prices = [price * (1 - discount_rate) for price in prices]
    return discounted_prices

# 함수 호출 및 출력
original_prices = [100, 200, 300, 400]
discounted_prices = apply_discount(original_prices)
print("할인된 가격들:", discounted_prices)
실습문제 4

OMR을 통한 선거 투표 데이터를 입력 받았습니다. 투표 결과를 문자열 리스트로 입력받고, 각 후보의 표 수를 계산하여 가장 많은 표를 받은 후보의 이름과 표 수를 출력하세요.

코드:

def tally_votes(votes):
    vote_count = {}
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    winner = max(vote_count, key=vote_count.get)
    return winner, vote_count[winner]

# 함수 호출 및 출력
votes = ["Alice", "Bob", "Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Alice", "Bob", "Alice", "Charlie"]
winner, count = tally_votes(votes)
print(f"승자는 {winner}이며, {count}표를 얻었습니다.")
실습문제 5

7/15-7/21 사이 일주일간의 온도 리스트에서 평일(월-금)과 주말(토, 일)의 평균 온도를 각각 계산하여 출력하세요.

코드:

def calculate_average_temperatures(temperatures):
    weekday_temps = temperatures[:5]  # 월요일부터 금요일
    weekend_temps = temperatures[5:]  # 토요일과 일요일
    weekday_average = sum(weekday_temps) / len(weekday_temps)
    weekend_average = sum(weekend_temps) / len(weekend_temps)
    return weekday_average, weekend_average

# 함수 호출 및 출력
week_temperatures = [31, 30, 30, 27, 31, 30, 31]
weekday_avg, weekend_avg = calculate_average_temperatures(week_temperatures)
print(f"지난주 전국 평일 평균 온도: {weekday_avg}도, 주말 평균 온도: {weekend_avg}도")
시퀀스 자료형의 기본 개념, 인덱싱 및 슬라이싱, 시퀀스 객체의 요소 개수 구하기 등의 다양한 활용 방법을 설명하고 있습니다. 또한 실습 문제를 통해 시퀀스 자료형을 다루는 방법을 익힐 수 있습니다.

​

터틀 그래픽스 활용

터틀 그래픽스

파이썬에서 그래픽을 쉽게 그릴 수 있는 모듈.

주로 교육용으로 사용되며 간단한 그림이나 패턴을 그릴 수 있음.

turtle 모듈을 사용하여 그래픽을 그릴 수 있음.

터틀 그래픽스는 터틀(거북이)을 이동시켜 그림을 그리는 방식으로 동작.

설치 방법

일반적으로 turtle 모듈은 파이썬에 내장되어 있어 별도의 설치가 필요 없음.

ubunt : sudo apt install python3-tk를 통해 설치할 수 있음.

기본 사용법

turtle.Turtle(): 터틀 객체를 생성.

turtle.forward(distance): 터틀을 앞으로 이동.

turtle.right(angle): 터틀을 오른쪽으로 회전.

turtle.left(angle): 터틀을 왼쪽으로 회전.

turtle.penup(): 터틀이 이동할 때 선을 그리지 않음.

turtle.pendown(): 터틀이 이동할 때 선을 그림.

실습문제 풀이

실습문제 1

터틀 그래픽스를 사용하여 각 꼭지점에서 색상이 변경되는 5각 별을 그리는 프로그램을 작성하세요.

코드:

import turtle

def draw_star():
    screen = turtle.Screen()
    screen.bgcolor("black")

    star = turtle.Turtle()
    star.speed(1)

    colors = ['red', 'yellow', 'blue', 'green', 'purple']

    for i in range(5):
        star.color(colors[i])
        star.forward(100)
        star.right(144)

    star.hideturtle()
    screen.mainloop()

# 함수 호출
draw_star()
실습문제 2

터틀 그래픽스를 사용하여 무지개 색상의 원을 겹쳐 그리는 프로그램을 작성하세요.

코드:

import turtle

def draw_rainbow_circles():
    screen = turtle.Screen()
    screen.bgcolor("black")

    rainbow = turtle.Turtle()
    rainbow.speed(0)

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    radius = 50

    for color in colors:
        rainbow.color(color)
        rainbow.circle(radius)
        radius += 10  # 원의 반지름을 점점 늘려서 그리기

    rainbow.hideturtle()
    screen.mainloop()

# 함수 호출
draw_rainbow_circles()
PyQt 활용

PyQt

Python 프로그래밍 언어를 위한 크로스 플랫폼 GUI 툴킷.

Qt 라이브러리의 기능을 Python 언어로 사용할 수 있도록 하는 래퍼(wrapper).

다양한 운영 시스템에서 동일하게 작동하는 응용 프로그램을 개발할 수 있음.

PyQt를 사용하면 표준 위젯, 테이블 뷰, 트리 뷰 등 복잡한 사용자 인터페이스를 쉽게 구성할 수 있음.

설치 방법

pip install PyQt5

pip install pyqt5-tools

기본 사용법

QApplication: 애플리케이션을 초기화하고 실행.

QWidget: 모든 위젯의 기본 클래스.

QLabel: 텍스트나 이미지를 표시.

QPushButton: 버튼 위젯.

QVBoxLayout, QHBoxLayout: 수직/수평 레이아웃 관리.

기본 예제

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    
    l1 = QLabel("Hello World")
    l2 = QLabel("PyQt5 Tutorial")
    l3 = QLabel("Welcome to PyQt5 GUI Programming")

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addWidget(l2)
    vbox.addWidget(l3)
    
    win.setLayout(vbox)
    win.setWindowTitle("PyQt5 Window")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
PyQt 실습문제 풀이

실습문제 3

PyQt를 사용하여 두 개의 버튼을 포함한 윈도우를 만들고, 버튼을 클릭했을 때 각각 다른 메시지를 출력하는 프로그램을 작성하세요.

코드:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def button1_clicked():
    print("Button 1 clicked")

def button2_clicked():
    print("Button 2 clicked")

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    b1 = QPushButton("Button 1")
    b2 = QPushButton("Button 2")
    b1.clicked.connect(button1_clicked)
    b2.clicked.connect(button2_clicked)

    vbox = QVBoxLayout()
    vbox.addWidget(b1)
    vbox.addWidget(b2)

    win.setLayout(vbox)
    win.setWindowTitle("PyQt5 Button Click Example")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
실습문제 4

PyQt를 사용하여 입력 필드를 포함한 폼을 만들고, 사용자가 입력한 데이터를 출력하는 프로그램을 작성하세요.

코드:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QFormLayout

def show_data():
    print("Name:", name_input.text())
    print("Address:", address_input.text())

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    global name_input, address_input
    name_label = QLabel("Name")
    address_label = QLabel("Address")
    name_input = QLineEdit()
    address_input = QLineEdit()
    submit_button = QPushButton("Submit")
    submit_button.clicked.connect(show_data)

    form_layout = QFormLayout()
    form_layout.addRow(name_label, name_input)
    form_layout.addRow(address_label, address_input)
    form_layout.addRow(submit_button)

    win.setLayout(form_layout)
    win.setWindowTitle("PyQt5 Form Example")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
터틀 그래픽스와 PyQt를 활용하여 그래픽 프로그램을 작성하는 방법을 설명합니다. 터틀 그래픽스를 사용한 다양한 도형 그리기 예제와 PyQt를 사용하여 GUI 애플리케이션을 만드는 방법을 다룹니다. 각 섹션마다 실습문제를 포함하여 학습자가 실제로 코드를 작성하고 실행해볼 수 있도록 돕습니다.


람다 함수

람다 함수의 정의

람다 함수는 파이썬에서 간단한 함수를 한 줄의 코드로 작성할 수 있도록 해주는 익명 함수입니다.

lambda 키워드를 사용하여 정의합니다.

람다 함수의 문법

lambda arguments: expression
arguments: 함수의 입력 인자, 콤마로 구분하여 여러 개를 넣을 수 있습니다.

expression: 인자를 사용하는 표현식으로, 이 표현식의 결과가 함수의 반환 값이 됩니다.

람다 함수의 특징

이름을 지정하지 않고, 필요한 곳에 바로 작성하여 사용할 수 있습니다.

작은 익명 함수입니다.

식이 하나만 사용됩니다.

함수 객체가 필요한 곳이면 어디서나 사용할 수 있습니다.

고차 함수의 인수로 자주 활용됩니다.

filter(), map(), reduce()와 같은 함수와 함께 사용됩니다.

람다 함수의 활용 예시

기본 사용법

f = lambda x, y: x + y
print(f(3, 5))  # 8
함수식 안에서 람다 활용

def mult_table(n):
    return lambda x: x * n

n = 5
y = mult_table(n)
for i in range(1, 11):
    print(f"{n} x {i} = {y(i)}")
단순 계산식에 람다 활용

print((lambda x: x * 3.14)(12))  # 37.68
print((lambda x: x / 3.14)(12))  # 3.821
고차 함수와 람다 함수

map() 함수

map(func, *iterables)는 iterable의 각 요소에 대해 function 함수를 적용한 결과를 새로운 iterator로 반환합니다.

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
filter() 함수

filter(func, iterable)는 iterable의 각 요소를 함수에 전달하여 논리적으로 참인 요소만 반환합니다.

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
reduce() 함수

reduce(func, iterable[, initial])는 시퀀스의 요소들을 누적적으로 특정 함수에 적용하여 하나의 값으로 줄입니다.

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # 15
실습문제 풀이

문제 1: 람다 리스트 정렬

주어진 사람들의 리스트를 각 사람의 나이에 따라 정렬하세요.

people = [
    {"name": "John", "age": 45},
    {"name": "Diana", "age": 32},
    {"name": "Tom", "age": 20}
]

sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)
문제 2: 최대값 찾기

주어진 숫자 리스트에서 최대값을 찾으세요.

from functools import reduce

numbers = [5, 8, 6, 10, 9, 2]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)
문제 3: 조건에 맞는 요소 필터링

주어진 숫자 리스트에서 5보다 큰 숫자만 포함하는 새 리스트를 만드세요.

numbers = [3, 5, 7, 10, 2, 6]
filtered_numbers = list(filter(lambda x: x > 5, numbers))
print(filtered_numbers)
문제 4: 요소 변환

주어진 문자열 리스트에서 각 문자열의 첫 글자만 대문자로 변환하세요.

words = ["hello", "world", "python", "programming"]
capitalized_words = list(map(lambda word: word.capitalize(), words))
print(capitalized_words)
문제 5: 복잡한 조건의 필터링

주어진 제품 리스트에서 가격이 100보다 크고, 재고가 10개 이상인 제품만 추출하세요.

products = [
    {"name": "Product A", "price": 150, "stock": 5},
    {"name": "Product B", "price": 120, "stock": 12},
    {"name": "Product C", "price": 50, "stock": 20},
    {"name": "Product D", "price": 200, "stock": 9}
]

filtered_products = list(filter(lambda p: p['price'] > 100 and p['stock'] >= 10, products))
print(filtered_products)
문제 6: 평균 점수 계산

학생들의 점수 리스트에서 평균 점수를 계산하세요.

from functools import reduce

scores = [88, 92, 78, 90, 84, 100, 95]
average_score = reduce(lambda x, y: x + y, scores) / len(scores)
print(f"The average score is: {average_score:.2f}")
문제 7: 특정 조건에 따른 문자열 필터링

주어진 문자열 리스트에서 길이가 5 이상인 문자열만 추출하세요.

words = ["apple", "pear", "banana", "cherry", "kiwi"]
long_words = list(filter(lambda x: len(x) >= 5, words))
print(long_words)
문제 8: 각 요소의 제곱값 계산

주어진 숫자 리스트의 각 요소에 대해 제곱값을 계산하세요.

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
문제 9: 복수 필드에 따른 복합 필터링

상품 리스트에서 가격이 100 이상이면서 재고가 50 이상인 상품만 추출하세요.

products = [
    {"name": "Keyboard", "price": 150, "stock": 25},
    {"name": "Mouse", "price": 70, "stock": 90},
    {"name": "Monitor", "price": 200, "stock": 50},
    {"name": "USB cable", "price": 10, "stock": 150}
]

filtered_products = list(filter(lambda p: p['price'] >= 100 and p['stock'] >= 50, products))
print(filtered_products)
문제 10: 문자열 길이 변환

주어진 문자열 리스트에서 각 문자열의 길이를 계산하여 새로운 리스트로 만드세요.

words = ["hello", "world", "python", "code"]
lengths = list(map(lambda x: len(x), words))
print(lengths)
문제 11: 평균 점수와 평균 이상 점수 추출

학생들의 점수 리스트에서 평균 점수를 계산하고, 평균 이상인 점수들만 추출하세요.

from functools import reduce

scores = [88, 92, 78, 90, 84, 100, 95]
average = reduce(lambda x, y: x + y, scores) / len(scores)
above_average = list(filter(lambda x: x >= average, scores))
print(f"Average score: {average:.2f}")
print("Scores above average:", above_average)
람다 함수의 개념과 사용 방법, 고차 함수와의 조합을 통한 다양한 데이터 처리 방법을 설명하며, 실습 문제를 통해 람다 함수의 실제 활용 방법을 익힐 수 있도록 돕습니다.

​

이터레이터(Iterator)

이터레이터의 정의

이터레이터는 값의 집합을 순회할 수 있는 객체입니다.

__iter__()와 __next__() 메소드를 구현하여 이터레이터를 만들 수 있습니다.

이터레이터 사용법

iter() 함수를 사용하여 이터러블 객체를 이터레이터로 변환할 수 있습니다.

next() 함수를 사용하여 이터레이터의 다음 값을 가져옵니다.

더 이상 값이 없을 때 StopIteration 예외가 발생합니다.

이터레이터 예제

it = iter(range(3))
print(next(it))  # 0
print(next(it))  # 1
print(next(it))  # 2
# print(next(it))  # StopIteration 발생
제너레이터(Generator)

제너레이터의 정의

제너레이터는 이터레이터를 생성하는 함수입니다.

함수 내부에서 yield 키워드를 사용하여 값을 반환합니다.

yield를 사용하면 함수가 중단되었다가 다시 호출될 때 이전 상태를 유지하고 재개됩니다.

제너레이터 사용법

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
실습문제 풀이

문제 1: 커스텀 이터레이터 구현

숫자의 범위를 지정해서, 그 범위 내의 모든 숫자를 반환하는 이터레이터 클래스 RangeIterator를 만드세요.

코드:

class RangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration

# 함수 호출
for num in RangeIterator(1, 10):
    print(num)
문제 2: 제너레이터 구현

주어진 최대값까지의 모든 짝수를 반환하는 제너레이터 함수 even_numbers를 작성하세요.

코드:

def even_numbers(max_num):
    n = 0
    while n <= max_num:
        if n % 2 == 0:
            yield n
        n += 1

# 함수 호출
for num in even_numbers(10):
    print(num)
문제 3: 피보나치 수열 제너레이터

피보나치 수열을 무한히 반환하는 제너레이터 함수 fibonacci()를 작성하세요.

코드:

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 함수 호출 및 출력
fib = fibonacci()
for _ in range(10):  # 처음 10개의 피보나치 수 출력
    print(next(fib))
문제 4: 이터레이터로 순열 생성

주어진 리스트의 모든 가능한 순열(permutations)을 생성하는 이터레이터 클래스 PermutationIterator를 구현하세요.

코드:

from itertools import permutations

class PermutationIterator:
    def __init__(self, items):
        self.permutations = permutations(items)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.permutations)

# 함수 호출
for perm in PermutationIterator([1, 2, 3]):
    print(perm)
문제 5: 소수 제너레이터

주어진 범위까지의 모든 소수를 반환하는 제너레이터 함수 primes를 작성하세요.

코드:

def primes(max_num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, max_num + 1):
        if is_prime(num):
            yield num

# 함수 호출 및 출력
for prime in primes(30):
    print(prime)
문제 6: 반복 이터레이터

주어진 리스트를 무한히 반복하여 반환하는 이터레이터 클래스 InfiniteRepeater를 구현하세요.

코드:

class InfiniteRepeater:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        while True:
            for item in self.data:
                yield item

# 함수 호출
repeater = InfiniteRepeater([1, 2, 3])
for num, value in enumerate(repeater):
    if num > 9:
        break
    print(value)
문제 7: 제너레이터를 이용한 파일 읽기

한 번에 한 줄씩 읽어오면서 파일의 내용을 처리하는 제너레이터 read_lines를 작성하세요.

코드:

def read_lines(filename):
    with open(filename, 'r') as file:
        while line := file.readline():  # 파이썬 3.8 이상에서 사용 가능
            yield line.strip()

# 파일 생성 및 테스트
filename = 'test.txt'
with open(filename, 'w') as f:
    f.write("First line\nSecond line\nThird line")

# 함수 호출 및 출력
for line in read_lines(filename):
    print(line)
문제 8: 제너레이터를 이용한 파이프라인 구성

문자열 리스트에서 각 문자열의 공백을 제거하고, 대문자로 변환하는 파이프라인을 구성하세요.

코드:

def strip_strings(strings):
    for s in strings:
        yield s.strip()

def uppercase_strings(strings):
    for s in strings:
        yield s.upper()

# 함수 호출 및 출력
strings = [" Hello ", " World ", " Python "]
stripped = strip_strings(strings)
uppercased = uppercase_strings(stripped)
for string in uppercased:
    print(string)
문제 9: 누적 합계 제너레이터

숫자 리스트의 누적 합계를 반환하는 제너레이터 cumulative_sum을 작성하세요.

코드:

def cumulative_sum(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total

# 함수 호출 및 출력
numbers = [1, 2, 3, 4, 5]
for total in cumulative_sum(numbers):
    print(total)
코루틴(Coroutine)

코루틴의 정의

코루틴은 제너레이터의 특별한 형태로, 중간에 값을 받아들이면서 코드 실행을 멈추고 다시 시작할 수 있는 함수입니다.

제너레이터와 마찬가지로 yield 키워드를 사용하지만, send() 메소드를 통해 외부로부터 값을 받을 수 있습니다.

코루틴 사용법

코루틴 함수를 정의합니다.

코루틴 객체를 생성하고, next() 함수를 사용해 코루틴을 시작합니다.

send() 메소드를 사용해 코루틴으로 값을 보냅니다.

코루틴 예제

def coroutine_example():
    print("Coroutine started")
    while True:
        value = (yield)
        print(f"Received value: {value}")

# 코루틴 사용
co = coroutine_example()
next(co)  # 코루틴 시작
co.send(10)
co.send(20)
코루틴의 종료

close() 메소드를 사용하여 코루틴을 종료할 수 있습니다.

GeneratorExit 예외가 발생합니다.

co.close()
코루틴 활용 예제

데이터 처리 파이프라인, 이벤트 핸들링 등에 유용하게 사용됩니다.

이터레이터와 제너레이터의 개념과 활용 방법을 설명하며, 다양한 예제와 실습 문제를 통해 이터레이터와 제너레이터의 실제 사용 방법을 익힐 수 있도록 돕습니다. 또한, 코루틴의 개념과 활용 방법을 설명하고 간단한 예제를 통해 코루틴의 사용법을 이해할 수 있도록 합니다.

​

정규 표현식(Regular Expression)

정규 표현식의 정의

정규 표현식은 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어입니다.

파이썬에서는 re 모듈을 사용하여 정규 표현식을 처리합니다.

정규 표현식의 기본 사용법

re.match(): 문자열의 시작에서 패턴이 일치하는지 검사합니다.

re.search(): 문자열 전체에서 패턴이 일치하는지 검사합니다.

re.findall(): 패턴에 일치하는 모든 부분 문자열을 리스트로 반환합니다.

re.sub(): 패턴에 일치하는 부분 문자열을 대체합니다.

정규 표현식의 예제

import re

pattern = r'\d+'
string = "There are 123 apples and 456 oranges."

# find all matches
matches = re.findall(pattern, string)
print(matches)  # ['123', '456']

# replace matches
replaced_string = re.sub(pattern, 'many', string)
print(replaced_string)  # 'There are many apples and many oranges.'
실습문제 풀이

문제 1: 이메일 주소 검증

주어진 문자열이 유효한 이메일 주소인지 확인하는 정규식을 작성하세요.

코드:

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid email"
    else:
        return "Invalid email"

# 함수 호출 및 출력
print(validate_email("example@email.com"))  # Valid email
print(validate_email("example.email.com"))  # Invalid email
문제 2: 전화번호 형식 확인

주어진 문자열이 "(xxx) xxx-xxxx" 형식의 전화번호인지 확인하는 정규식을 작성하세요.

코드:

import re

def validate_phone_number(number):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    if re.match(pattern, number):
        return "Valid phone number"
    else:
        return "Invalid phone number"

# 함수 호출 및 출력
print(validate_phone_number("(123) 456-7890"))  # Valid phone number
print(validate_phone_number("123-456-7890"))  # Invalid phone number
문제 3: HTML 태그 제거

주어진 HTML 문자열에서 모든 HTML 태그를 제거하고 텍스트 내용만 반환하는 정규식을 사용하세요.

코드:

import re

def remove_html_tags(html):
    pattern = r'<[^>]+>'
    text = re.sub(pattern, '', html)
    return text

# 함수 호출 및 출력
html_content = "<html><head><title>Test</title></head><body>Hello, world!</body></html>"
print(remove_html_tags(html_content))  # Hello, world!
문제 4: 비밀번호 복잡성 검사

주어진 비밀번호가 다음 조건을 모두 만족하는지 확인하세요: 최소 8자, 하나 이상의 대문자, 하나 이상의 소문자, 하나 이상의 숫자.

코드:

import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    if re.match(pattern, password):
        return "Strong password"
    else:
        return "Weak password"

# 함수 호출 및 출력
print(validate_password("Password123"))  # Strong password
print(validate_password("password"))  # Weak password
문제 5: URL 파싱

주어진 URL에서 프로토콜, 호스트, 옵션적으로 포트 번호를 추출하는 정규식을 작성하세요.

코드:

import re

def parse_url(url):
    pattern = r'^(https?):\/\/([^:/\s]+)(?::(\d+))?'
    match = re.match(pattern, url)
    if match:
        return {"protocol": match.group(1), "host": match.group(2), "port": match.group(3)}
    else:
        return "Invalid URL"

# 함수 호출 및 출력
print(parse_url("http://example.com:8080"))  # {'protocol': 'http', 'host': 'example.com', 'port': '8080'}
print(parse_url("https://example.com"))  # {'protocol': 'https', 'host': 'example.com', 'port': None}
정규 표현식의 기본 개념과 활용법을 설명하며, 다양한 실습 문제를 통해 이를 실제로 적용해 볼 수 있도록 돕는다.
