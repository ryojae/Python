# #no.1
# class RangeIterator:
#     def __init__(self,start,end):
#         self.current = start
#         self.stop = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current<self.stop:
#             number = self.current
#             self.current += 1
#             return number
#         else:
#             raise StopIteration
# for num in RangeIterator(1,10):
#     print(num)

# #no.2
# def even_numbers(n):
#     start=0
#     while start<=n:
#         if start %2==0:
#             yield start
#         start+=1
# for num in even_numbers(10):
#     print(num)

# #no.3
# def fibonacci():
#     a=0; b=1
#     while True:
#         yield a
#         a, b = b, a+b
# fib = fibonacci()
# print(fib)
# for _ in range(10):
#     print(next(fib))

# #no.4
# from itertools import permutations
# class PermutationIterator:
#     def __init__(self,lst):
#         self.permutation = permutations(lst)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return next(self.permutation)
# for perm in PermutationIterator([1,2,3]):
#     print(perm)
#     print(permutations([1,2,3,4,5]))

#no.5
# def primes(n):
#     start = 2
#     def is_prime(x):
#         for i in range(2,int(x**0.5)+1):
#             if x%i ==0:
#                 return False
#         return True     
#     while start <=n:
#         if is_prime(start):
#             yield start
#         start+=1
# for num in primes(20):
#     print(num)

# #no.6
# class InfiniteRepeater:
#     def __init__(self, data):
#         self.data = data
#     def __iter__(self):
#         while True:
#             for item in self.data:
#                 yield item
# # 함수 호출
# repeater = InfiniteRepeater([1, 2, 3])
# for num, value in enumerate(repeater):
#     if num > 9:
#         break
#     print(num,value)

# #no.7
# def read_lines(filename):
#     with open(filename, 'r') as file:
#         line=file.readline()
#         while line:
#             yield line.strip()
#             line=file.readline()
# filename = 'show.txt'
# with open(filename,'w') as f:
#     f.write('First line\nSecond line\nThird line')
# for line in read_lines(filename):
#     print(line)

# #no.8
# def strip_strings(strings):
#     for s in strings:
#         yield s.strip()
# def uppercase_strings(strings):
#     for s in strings:
#         yield s.upper()
# strings = ['Hello', 'world','Python']
# stripped = strip_strings(strings)
# uppercased=uppercase_strings(stripped)
# for string in uppercased:
#     print(string)

# #no.9
# def cumulative_sum(lst):
#     total = 0
#     for n in lst:
#         total+=n
#         yield total
# numbers=[1,2,3,4,5]
# for total in cumulative_sum(numbers):
#     print(total)