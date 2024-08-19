# #no.2
# numbers = [1,2,3,4,5]
# it = numbers.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# #no.3
# numbers=[1,2,3,4,5]
# it=numbers.__iter__()
# try:
#     while 1:
#         print(it.__next__())
# except StopIteration as e:
#     print('종료')
#     print(type(e))

# #no.5
# class MyIterator:
#     def __init__(self, data):
#          self.data = data
#          self.index=0

#     def __iter__(self):
#          return self

#     def __next__(self):
#          if self.index < len(self.data):
#               result = self.data[self.index]
#               self.index+=1
#               return result
#          else:
#               raise StopIteration
# # 사용 예제
# numbers = [1, 2, 3, 4, 5]
# iterator = MyIterator(numbers)
 
# for num in iterator:
#     print(num)

# #no.6
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         # Write your code here
#         return self

#     def __next__(self):
#         # Write your code here
#          if self.index < len(self.data):
#               result = self.data[self.index]
#               self.index+=1
#               return result
#          else:
#               raise StopIteration

#     def __getitem__(self, index):
#         if index < len(self.data):
#             return self.data[index]
#         else:
#             raise IndexError

# # 사용 예제
# numbers = [1, 2, 3, 4, 5]
# iterator = MyIterator(numbers)
 
# for num in iterator:
#     print(num)

# # 인덱스로 접근하여 값 출력
# print("Index access:")
# print(iterator[0])    # 출력: 1
# print(iterator[3])    # 출력: 4

# #no.7
# def file_line_iterator(file_path):
#     # Write your code here
#     with open(file_path,'r') as file:
#         while line:=file.readline():
#             yield line.strip()
# # 예제 파일을 생성하고 테스트해 보겠습니다.
# with open('example.txt', 'w') as f:
#     f.write("First line\n")
#     f.write("Second line\n")
#     f.write("Third line\n")
 
# # 파일 경로를 입력하여 이터레이터를 생성하고 사용합니다.
# iterator = file_line_iterator('example.txt')
 
# for line in iterator:
#     print(line)

# #no.8
# class FibonacciIterator:
#     def __init__(self):
#         # Write your code here
#         self.a=0
#         self.b=1

#     def __iter__(self):
#         # Write your code here
#         return self

#     def __next__(self):
#         # Write your code here
#         result = self.a + self.b
#         self.a, self.b = self.b , result
#         if result <=100:
#             return result
#         else:
#             raise StopIteration
# # 사용 예시
# fib_iter = FibonacciIterator()
 
# for number in fib_iter:
#     print(number)

# #no.10
# def fibonacci():
#     a=0;b=1
#     while True:
#         yield a
#         a, b = b,a+b
# fib= fibonacci()
# c= next(fib)
# while c<=100:
#     print(c)
#     c=next(fib)

# #no.11
# def filter_even(nums):
#     for n in nums:
#         if n % 2 ==0:
#             yield n
# nums=[1,2,3,4,5,6,7,8,9,10]
# even_num=filter_even(nums)
# for i in even_num:
#     print(i)