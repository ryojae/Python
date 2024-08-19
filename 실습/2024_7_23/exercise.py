# #no.1
# import math
# class Rectangle:
#     def __init__(self,x1,y1,x2,y2):
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2
#     def calcArea(self):
#         print(abs((self.x2-self.x1)*(self.y2-self.y1)))
# class Circle:
#     def __init__(self,x,y,r):
#         self.x=x
#         self.y=y
#         self.r=r
#     def calcArea(self):
#         print(math.pi*self.r**2)
# shapeList = []
# for i in range(3):
#     s = input("도형 모양을 입력하세요: ")
#     if s == "사각형":
#         x1 = int(input("왼쪽 상단의 x좌표를 입력: "))
#         y1 = int(input("왼쪽 상단의 y좌표를 입력: "))
#         x2 = int(input("오른쪽 하단의 x좌표를 입력: "))
#         y2 = int(input("오른쪽 하단의 y좌표를 입력: "))
#         shapeList.append(Rectangle(x1, y1, x2, y2))
#     elif s == "원":
#         x = int(input("원의 중심 x 좌표를 입력: "))
#         y = int(input("원의 중심 y 좌표를 입력: "))
#         r = int(input("원의 반지름을 입력: "))
#         shapeList.append(Circle(x, y, r))
# for s in shapeList:
#     print(f"면적: {s.calcArea()}")

# #no.2
# import math
# class Shape:
#     def __init__(self, shapeStr):
#         self.shapeStr = shapeStr
#     def getShapeStr(self):
#         return self.shapeStr
# class Circle(Shape):
#     def __init__(self, shapeStr, x, y, r):
#         super().__init__(shapeStr)
#         self.x = x
#         self.y = y
#         self.r = r
#     def calcArea(self):
#         return math.pi * self.r * self.r
# class Rectangle(Shape):
#     def __init__(self, shapeStr, x1, y1, x2, y2):
#         super().__init__(shapeStr)
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#     def calcArea(self):
#         return (self.x2 - self.x1) * (self.y1 - self.y2)
# shapeList = []
# for i in range(3):
#     s = input("도형 모양을 입력하세요: ")
#     if s == "사각형":
#         x1 = int(input("왼쪽 상단의 x좌표 입력: "))
#         y1 = int(input("왼쪽 상단의 y좌표 입력: "))
#         x2 = int(input("오른쪽 하단의 x좌표 입력: "))
#         y2 = int(input("오른쪽 하단의 y좌표 입력: "))
#         shapeList.append(Rectangle("사각형",x1,y1,x2, y2))
#     elif s == "원":
#         x = int(input("원의 중심 x 좌표 입력: "))
#         y = int(input("원의 중심 y 좌표 입력: "))
#         r = int(input("원의 반지름 입력: "))
#         shapeList.append(Circle("원", x, y, r))
# for s in shapeList:
#     print(f"도형 모양: {s.getShapeStr()}")
#     print(f"면적: {s.calcArea()}")

# #no.3
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
# def create_and_print_car():
#     my_car = Car("Toyota", "Corolla", 2021)
#     print(f"차량 정보: {my_car.year} {my_car.make} {my_car.model}")
# # 함수 호출
# create_and_print_car()

# #no.4
# class Dog:
#     def bark(self):
#         print("Woof!")
# def make_dog_bark():
#     my_dog = Dog()
#     my_dog.bark()
# # 함수 호출
# make_dog_bark()

# #no.5
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
# class Truck(Vehicle):
#     def __init__(self, make, model, load_capacity):
#         super().__init__(make, model)
#         self.load_capacity = load_capacity
# def create_and_print_truck():
#     my_truck = Truck("Ford", "F-150", 1000)
#     print(f"트럭 정보: {my_truck.make} {my_truck.model}, 적재 용량:
#     {my_truck.load_capacity}kg")
# # 함수 호출
# create_and_print_truck()

# #no.6
# class MathOperations:
#     def add(self, a, b):
#         return a + b
#     @classmethod
#     def multiply(cls, a, b):
#         return a * b
#     @staticmethod
#     def subtract(a, b):
#         return a - b
# def perform_operations():
#     math_op = MathOperations()
#     print("Add:", math_op.add(2, 3))
#     print("Multiply:", MathOperations.multiply(4, 5))
#     print("Subtract:", MathOperations.subtract(10, 3))
# # 함수 호출
# perform_operations()

# #no.7
# class Account:
#     def __init__(self, balance):
#         self.__balance = balance
#     def __update_balance(self, amount):
#         self.__balance += amount
#     def deposit(self, amount):
#         if amount > 0:
#             self.__update_balance(amount)
#             print(f"Deposited: ${amount}")
#             print(f"New Balance: ${self.__balance}")
#         else:
#             print("Invalid amount")
# # 함수 호출
# my_account = Account(100)
# my_account.deposit(50)

# #no.8
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: ${amount}. New balance: ${self.balance}")
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             print(f"Withdrew: ${amount}. New balance: ${self.balance}")
# # 함수 호출
# account = BankAccount(100)
# account.deposit(50)
# account.withdraw(200)

# #no.9
# class Animal:
#     def speak(self):
#         print("Some generic sound")
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
# class Cat(Animal):
#     def speak(self):
#         print("Meow")
# # 함수 호출
# my_dog = Dog()
# my_cat = Cat()
# my_dog.speak()
# my_cat.speak()

#no.10
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
print(product.price) # Output: 5
product.price = -10 # Should raise an error message
product.price = 15
print(product.price) # Output: 15