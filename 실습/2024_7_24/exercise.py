# #no.1
# import Circle1
# r=Circle1.Circle(1)
# print(Circle1.circumference(r.getCircumference()))

# #no.2
# import glob, sys
# lst=[]
# print(sys.argv)
# if len(sys.argv) == 1:
#     lst = glob.glob('*')
# else:
#     lst = glob.glob(sys.argv[1])
# if len(lst) == 0: # 빈 리스트
#     print("매칭되는 파일이 없습니다")
# else:
#     for name in lst:
#         print(name)

# #no.3
# import hell
# hell.main()

# #no.4
# from pr3 import sum_all
# from pr3 import multi

# if __name__=='__main__':
#     print(sum_all(1,2))
#     print(multi(3))

# #no.5
# import pr5
# print(pr5.a,pr5.b,pr5.c)
# pr5.a=3
# print(pr5.a,pr5.b,pr5.c)

# #no.6
# from personmodule import Person
# person = Person("Bob", 30)
# print(person.greet()) # Hello, my name is Bob and I am 30 years old. 

# #no.7
# from errormodule import MyError
# try:
#     raise MyError("Something went wrong")
# except MyError as e:
#     print(e)

# #no.8
# from my_package.utilities import multiply_numbers
# n=multiply_numbers(2,3)
# print(n)

# #no.9
# from my_package.math_tools import add
# from my_package.string_tools import capitalize_string
# print(add(1,3))
# print(capitalize_string('hello'))