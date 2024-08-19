# #no.1
# def fsm_generator():
#       state = 'START'
#       while True:
#             input_char = yield state
#             if state == 'START':
#                 if input_char == 'a':
#                     state = 'STATE_A'
#             elif state == 'STATE_A':
#                 if input_char == 'b':
#                     state = 'STATE_B'
#                 else:
#                     state = 'START'
#             elif state == 'STATE_B':
#                 if input_char == 'a':
#                     state = 'STATE_A'
#                 elif input_char == 'b':
#                     state = 'STATE_B'
#                 else:
#                     state = 'START'
 
# # 사용 예시: 문자열을 입력하여 상태 변화를 추적
# fsm = fsm_generator()
# next(fsm) # 제네레이터 초기화
 
# input_string = "ababab"
# for char in input_string:
#       state = fsm.send(char)
#       print(f"Input: {char}, State: {state}")

# #no.2
# def process_line(line):
#     print(line.strip())
# def read_lines(filename):
#     with open(filename,'r') as file:
#         while line := file.readline():
#             yield line
# def filter_line(lines,keyword):
#     for line in lines:
#         if keyword in line:
#             yield line
# filename = 'show.txt'
# lines = read_lines(filename)
# keyword='Second'
# filtered_lines=filter_line(lines,keyword)
# for line in filtered_lines:
#     process_line(line)

# #no.5
# import asyncio
 
# async def simple_coroutine(): # aync def 는 코루틴 함수를 정의
#     # Write your code here
#     print('coroutine 시작')
#     await asyncio.sleep(1)
#     print('coroutine 종료')

# def call_coroutine():
#     # Write your code here
#     coroutine = simple_coroutine()
#     asyncio.run(coroutine)
 
# call_coroutine()

#no.6
import asyncio
 
# 각 학생의 점수 데이터
scores = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 90}
]
 
# 비동기 코루틴으로 평균 성적을 계산하는 함수
async def calculate_average(scores):
    # Write your code here
    total = 0
    for score in scores:
        total += score['score']
    average = total/len(scores)
    return average

 
async def main():
    average = await calculate_average(scores) # await는 구버전의 yield from
    print(f"전체 학생들의 평균 점수는 {average:.2f}입니다.")
 
# asyncio.run을 사용하여 메인 함수 실행
asyncio.run(main())