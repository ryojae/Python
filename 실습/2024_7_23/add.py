# #no.1
# class Rectnagle:
#     def __init__(self,x,y,width,height):
#         self.x=x
#         self.y=y
#         self.width=width
#         self.height=height
#     def print(self):
#         print(f'x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}')
# rec=Rectnagle(1,2,3,4)
# rec.print()

# #no.2
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         print(f"Vehicle initialized: {self.brand} {self.model}")
 
# class Car(Vehicle):
#     def __init__(self, brand, model, horsepower):
#         super().__init__(brand, model)  # 부모 클래스의 생성자 호출
#         self.horsepower = horsepower
#         print(f"Car initialized: {self.brand} {self.model} with {self.horsepower} HP")
 
# # 객체 생성
# my_car = Car("AAA", "BBB", 350)

# #no.3
# import math
 
# class Rectangle:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1=x1
#         self.y1=y1
#         self.x2=x2
#         self.y2=y2
 
#     def calcArea(self):
#         return(abs((self.x2-self.x1)*(self.y2-self.y1)))
 
# class Circle:
#     def __init__(self, x, y, r):
#         self.x=x
#         self.y=y
#         self.r=r
 
#     def calcArea(self):
#         return (math.pi*self.r**2)
 
           
# shapeList = []
 
# for i in range(3):
#     s = input("도형 모양을 입력하세요 (1:사각형 0:원): ")
#     if s == "1":
#         x1 = int(input("왼쪽 상단의 x좌표를 입력: "))
#         y1 = int(input("왼쪽 상단의 y좌표를 입력: "))
#         x2 = int(input("오른쪽 하단의 x좌표를 입력: "))
#         y2 = int(input("오른쪽 하단의 y좌표를 입력: "))
#         shapeList.append(Rectangle(x1, y1, x2, y2))
#     elif s == "0":
#         x = int(input("원의 중심 x 좌표를 입력: "))
#         y = int(input("원의 중심 y 좌표를 입력: "))
#         r = int(input("원의 반지름을 입력: "))
#         shapeList.append(Circle(x, y, r))
# for s in shapeList:
#     print(f"면적: {s.calcArea():.2f}")

# #no.4
# import math
# class Rectangle:
#     def __init__(self):
#         None
#     def calcArea(self):
#         return(abs((self.x2-self.x1)*(self.y2-self.y1)))
#     def getCoordsInfo(self):
#         self.x1 = int(input("왼쪽 상단의 x 좌표값을 정수로 입력하세요: "))
#         self.y1 = int(input("왼쪽 상단의 y 좌표값을 정수로 입력하세요: "))
#         self.x2 = int(input("오른쪽 하단의 x 좌표값을 정수로 입력하세요: "))
#         self.y2 = int(input("오른쪽 하단의 y 좌표값을 정수로 입력하세요: "))
 
# class Circle:
#     def __init__(self):
#         None
#     def calcArea(self):
#         return (math.pi*self.r**2)
#     def getCoordsInfo(self):
#         self.x = int(input("원의 중심 x 좌표값을 정수로 입력하세요: "))
#         self.y = int(input("원의 중심 y 좌표값을 정수로 입력하세요: "))
#         self.r = int(input("원의 반지름을 입력하세요: "))

# shapeList = []

# for i in range(3):
#     s = input("도형 모양을 입력하세요 (1:사각형 0:원): ")
#     if s == "1":
#         rect = Rectangle()
#         rect.getCoordsInfo()
#         shapeList.append(rect)
#     else:
#         circle = Circle()
#         circle.getCoordsInfo()
#         shapeList.append(circle)
# for s in shapeList:
#     print(f"면적: {s.calcArea():.2f}")

# #no.5
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def setX(self,x):
#         self.x=x
#     def setY(self,y):
#         self.y=y
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
# pt=Point(1,3)
# print(f'X: {pt.getX()}, Y: {pt.getY()}')
# pt.setX(2)
# pt.setY(6)
# print(f'변경 후 \nX: {pt.getX()}, Y: {pt.getY()}')

# #no.6
# class Problem:
#       def __init__(self, studentsNumDictionary):
#             self.studentsNumDictionary = studentsNumDictionary
#       def subproblem1(self):
#             max = 0
#             year = 0

#             value=list(self.studentsNumDictionary.values())
            
#             decrease=[]
#             for i in range(0,len(value)-1):
#                   decrease.append(value[i]-value[i+1])
#             for i in range(0,len(decrease)):
#                   if max<decrease[i]:
#                         max=decrease[i]
#                         year=list(self.studentsNumDictionary.keys())[i+1]
#             print(f"(1) {year}에 {max:.1f}명 감소한 것이 최근 가장 급격하게 줄어든 경우입니다.")
#       def subproblem2(self):
#             value=list(self.studentsNumDictionary.values())
#             i=0
#             for j in range(0,len(value)):
#                   if value[j]<30:
#                         i=list(self.studentsNumDictionary.keys())[j]
#                         break
            
#             print(f"(2) 학생 수가 30명 미만으로 떨어진 첫 해는 {i}년입니다.")
 
#       def subproblem3(self):
#             # 3 2010년부터 2021년까지 평균적으로 감소한 학생 수
#             Sum = 0
#             value=list(self.studentsNumDictionary.values())
            
#             decrease=[]
#             for i in range(0,len(value)-1):
#                   decrease.append(value[i]-value[i+1])
#             Sum=sum(decrease)
#             print(f"(3) 2010년부터 2021년까지 평균적으로 감소한 학생 수는 {Sum / 11:.2f}명이다")
# d = {2010:33.7, 2011:33.1, 2012:32.5, 2013:31.9, 2014:30.9,
#       2015:30.0, 2016:29.3, 2017:28.2, 2018:26.2, 2019:24.5, 2020:23.4, 2021:23}
# p = Problem(d)
# p.subproblem1()
# p.subproblem2()
# p.subproblem3()

# #no.7
# class Car:
#       def __init__(self, company, year, color):
#             self.company=company
#             self.year=year
#             self.color=color 
#       def __str__(self):
#             return f'자동차 회사: {self.company}, 년식: {self.year}, 색상: {self.color}'
#       def __eq__(self, other):
#             if isinstance(other, Car):
#                 return self.company == other.company and self.year == other.year and self.color == self.color
#             return False

 
# # 예시 코드
# mycar = Car('ABC', 2020, '검정')
# yourcar = Car('DEF', 2021, '백색')
# print(mycar)
# print(yourcar)
# print(mycar == yourcar)

print('asdf')
