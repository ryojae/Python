# #no.1
# import random
# s1=set()
# while len(s1) <10:
#     n=random.randint(1,20)
#     s1.add(n)
# print(f'{s1}, 개수: {len(s1)}')

# #no.2
# student_courses = {
#   	"학생1": {"수학", "과학", "영어"},
#   	"학생2": {"수학", "음악", "미술"},
#       "학생3": {"수학", "과학", "음악"}}
# print(f'모든 학생이 듣는 과목은 {student_courses["학생1"]&student_courses["학생2"]&student_courses["학생3"]}입니다.')
# print(f'한명이라도 듣는 과목은 {student_courses["학생1"]|student_courses["학생2"]|student_courses["학생3"]}입니다.')
# data ={}
# lst=list(student_courses["학생1"])+list(student_courses["학생2"])+list(student_courses["학생3"])
# for i in lst:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# s=set()
# for k,v in data.items():
#     if v == 1:
#         s.add(k)
# print(f'한명씩만 듣는 과목은 {s}입니다.')

# #no.3
# sentence = '''The first they had heard of the strangers from outer
# space was when the new ultra short-wave frequencies were used
# Professor Kennicot of Palmira University was the first to find how to generate and control them
# He tried to transform the wavelengths upward to a range either 
# auditory or visual but for some reason power was lost in the process
# Apparently he gave them a sufficient jolt with extra voltage however 
# because they were picked up by the strangers in outer space
# as a signal The heaviside layer did not stop these wavelengths
# Professor Kennicot was startled one day when he heard or thought he heard a soundless voice in his mind
# '''
# lst = sentence.split()
# data ={}
# for i in lst:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# print('모든 단어\n',data)
# max1=0
# max1_word=0
# max2=0
# max2_word=0
# for k,v in data.items():
#     if max2<v:
#         if max1<v:
#             max2=max1
#             max2_word=max1_word
#             max1=v
#             max1_word=k
#         else:
#             max2=v
#             max2_word=k
# print(f'가장 많이 나온 단어는 {max1_word}: {max1}회입니다.')
# print(f'두번째로 많이 나온 단어는 {max2_word}: {max2}회입니다.')

# #no.4
# sentence = '''The first they had heard of the strangers from outer
# space was when the new ultra short-wave frequencies were used
# Professor Kennicot of Palmira University was the first to find how to generate and control them
# He tried to transform the wavelengths upward to a range either 
# auditory or visual but for some reason power was lost in the process
# Apparently he gave them a sufficient jolt with extra voltage however 
# because they were picked up by the strangers in outer space
# as a signal The heaviside layer did not stop these wavelengths
# Professor Kennicot was startled one day when he heard or thought he heard a soundless voice in his mind
# '''
# data ={}
# for i in sentence:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# del(data[' ']); del(data['-']); del(data['\n'])
# max_key=0; max_value=0
# for k,v in data.items():
#     if max_value<v:
#         max_value=v
#         max_key=k
# print(f'가장 많이 나온 알파벳은 {max_key}로 {max_value}회 입니다.')

# #no.5
# sentence = '''The first they had heard of the strangers from outer
# space was when the new ultra short-wave frequencies were used
# Professor Kennicot of Palmira University was the first to find how to generate and control them
# He tried to transform the wavelengths upward to a range either 
# auditory or visual but for some reason power was lost in the process
# Apparently he gave them a sufficient jolt with extra voltage however 
# because they were picked up by the strangers in outer space
# as a signal The heaviside layer did not stop these wavelengths
# Professor Kennicot was startled one day when he heard or thought he heard a soundless voice in his mind
# '''
# data ={}
# for i in sentence:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# max_key=0; max_value=0; max2_key=0; max2_value=0
# for k,v in data.items():
#     if max2_value<v:
#         if max_value<v:
#             max2_key=max_key
#             max2_value=max_value
#             max_value=v
#             if k==' ':
#                 k='SPACE'
#             max_key=k
#         else:
#             max2_value=v
#             if k==' ':
#                 k='SPACE'
#             max2_key=k
# print(f'가장 많이 나온 알파벳은 {max_key}로 {max_value}회 입니다.')
# print(f'두번째로 많이 나온 알파벳은 {max2_key}로 {max2_value}회 입니다.')

# #no.6
# sentence = '''The first they had heard of the strangers from outer
# space was when the new ultra short-wave frequencies were used
# Professor Kennicot of Palmira University was the first to find how to generate and control them
# He tried to transform the wavelengths upward to a range either 
# auditory or visual but for some reason power was lost in the process
# Apparently he gave them a sufficient jolt with extra voltage however 
# because they were picked up by the strangers in outer space
# as a signal The heaviside layer did not stop these wavelengths
# Professor Kennicot was startled one day when he heard or thought he heard a soundless voice in his mind
# '''
# sentence=sentence.lower()
# s='abcdefghijklmnopqrstuvwxyz'
# set_sentence=set()
# set_alphabet=set()
# for i in s:
#     set_alphabet.add(i)
# for i in sentence:
#     set_sentence.add(i)
# print(sorted(set_alphabet))
# print(sorted(set_sentence))
# diffenrce=set_alphabet-set_sentence
# if len(diffenrce) == 0:
#     print('나타나지 않은 알파벳은 없습니다.')
# else:
#     print(f'나타나지 않은 알파벳은 {diffenrce}입니다.')

# #no.7
# sentence = '''The first they had heard of the strangers from outer
# space was when the new ultra short-wave frequencies were used
# Professor Kennicot of Palmira University was the first to find how to generate and control them
# He tried to transform the wavelengths upward to a range either 
# auditory or visual but for some reason power was lost in the process
# Apparently he gave them a sufficient jolt with extra voltage however 
# because they were picked up by the strangers in outer space
# as a signal The heaviside layer did not stop these wavelengths
# Professor Kennicot was startled one day when he heard or thought he heard a soundless voice in his mind
# '''
# word = sentence.split()
# s1=set()
# s2=set()
# j=0
# for i in word:
#     if i[0]=='T' or i[0] == 't':
#         if not i.lower() in s2:
#             s1.add(word[j])
#             s2.add(i.lower())
#     j+=1
# print('t:',end=' ')
# for i in sorted(s1):
#     print(i, end =', ')

# #no.8
# guPopulation={'가':3,'나':1,'다':10,'라':24,'마':4,'바':25,'사':12,'아':15,'자':162,'차':345}
# n=int(input('정수:'))
# data={}
# for k,v in guPopulation.items():
#     if v<n:
#         data[k]=v
# if len(data) ==0:
#     print('인구가 num보다 작은 구가 없습니다.')
# else:
#     print(data)

# #no.9
# def check_password_strength(password):
#     special_characters = "~!@#$%^&:',./?><|"

#     length = len(password)
#     has_special = any(char in special_characters for char in password)
#     special_count = sum(char in special_characters for char in password)
#     has_digit = any(char.isdigit() for char in password)
#     has_upper = any(char.isupper() for char in password)
#     if length > 10 and special_count >= 2 and has_digit and has_upper:
#         return "안전함"
#     elif 8 <= length <= 10 and has_digit and has_upper:
#         return "보통"
#     elif 8 <= length <= 10 and (has_special or has_digit or has_upper):
#         return "보통 이하"
#     else:
#         return "안전하지 않음"

# # 사용자로부터 비밀번호 입력 받기
# password = input("비밀번호를 입력하세요: ")
# # 비밀번호 안전도 출력
# print("비밀번호 안전도:", check_password_strength(password))

# #no.10
# data={'21년':23.0,'20년':23.4,'19년':24.5,'18년':26.2,'17년':28.2,
#       '16년':29.3,'15년':30.0,'14년':31.9,'13년':31.9,'12년':32.5,'11년':33.1,'10년':33.7}
# decrease={}
# k_ex=0;v_ex=0
# max=0
# for k,v in data.items():
#     if v<30:
#         key_under30=k
#     if k_ex == 0 and v_ex ==0:
#         k_ex=k;v_ex=v
#     else:
#         decrease[k]=round(v-v_ex,2)
#         k_ex=k;v_ex=v
# for k,v in decrease.items():
#     if max<v:
#         max=v
#         index=k
# print(f'30명 미만으로 떨어진 해는 {key_under30}입니다.')
# print(f'전해에 비해 가장 급격하게 학생 수가 줄어든 해는 {index}입니다.')
# print(f'2010년부터 2021년 사이에 평균적으로 학급당 학생 {sum(decrease.values())/11:.2f}')

#no.11
from collections import Counter
with open('input.txt','r') as file:
    s1=file.read()
tabel = s1.maketrans({'!':'','.':'',',':''})
s1=s1.translate(tabel)
s1=s1.lower()
s=s1.split()
data=Counter(s)
data=dict(data)
print(data)
print(sorted(data.items()))