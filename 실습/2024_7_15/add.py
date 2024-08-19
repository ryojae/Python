# #no.1
# # 1부터 100까지 재귀적으로 더함
# def sum1(n):
#     if n == 1:
#         return 1
#     return n + sum1(n-1)


# # 1부터 100까지 공식으로 더함
# def sum2(n):
#     return n * (n+1) // 2


# print(sum1(100))
# print(sum2(100))

# #no.2
# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     return reverse_string(s[1:]) + s[0]

# s= input('문자열을 입력해주세요:')
# print(f"Reversed: {reverse_string(s)}")

# #no.3
# def is_prime(n, i=2):
#     if n<=1:
#         return False
#     if i>=n:
#         return True
#     if n%i==0:
#         return False
#     return is_prime(n, i + 1)
# n = int(input('Input: '))
# print(f'Output: {is_prime(n)}')
# n = int(input('Input: '))
# print(f'Output: {is_prime(n)}')

# #no.4
# def sum_digits(s):
#     if len(s) == 1:
#         if s.isdigit():
#             return int(s)
#         else:
#             return 0
#     else:
#         if s[0].isdigit():
#             return sum_digits(s[1:])+int(s[0])
#         else:
#             return sum_digits(s[1:])
# s = input('Input: ')
# print(f'Output: {sum_digits(s)}')
# s = input('Input: ')
# print(f'Output: {sum_digits(s)}')
# s = input('Input: ')
# print(f'Output: {sum_digits(s)}')

# #no.5
# def isPalindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return isPalindrome(s[1:-1])
# s = input('Input: ')
# print('Output:',isPalindrome(s))

#no.6
def count_number(n, x):
    if len(n) == 1:
        if n == x:
            return 1
        else:
            return 0
    else:
        if n[0]==x:
            return count_number(n[1:],x)+1
        else:
            return count_number(n[1:],x)
n=input('Input:')
x=input('Find_Number:')
print('Output:',count_number(n,x))