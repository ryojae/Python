# #no.3
# import turtle
# screen=turtle.Screen()
# t=turtle.Turtle()
# t.shape('turtle')
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# screen.mainloop()

# #no.4
# import turtle
# screen=turtle.Screen()
# t=turtle.Turtle()
# t.shape('turtle')
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# screen.mainloop()

# #no.6
# import turtle
# screen=turtle.Screen()
# t=turtle.Turtle()
# t.shape('turtle')
# for i in range(6):
#     t.forward(100)
#     t.right(60)
# screen.mainloop()

# #no.7
# import turtle
# screen=turtle.Screen()
# screen.bgcolor('black')
# t=turtle.Turtle()
# t.shape('turtle')
# t.color('blue')
# t.begin_fill()
# t.circle(100)
# t.color('red')
# t.end_fill()
# screen.mainloop()

# #no.8
# import turtle
# screen=turtle.Screen()
# screen.bgcolor('black')
# t=turtle.Turtle()
# t.shape('turtle')
# t.color('red')
# t.forward(120)
# t.left(90)
# t.circle(120,90)
# t.left(90)
# t.forward(120)
# screen.mainloop()

# #no.8
# import turtle
# turtle.speed(0) #숫자가 클수록 빠르게 그립니다. 0는 가장 빠른 속도입니다.
# turtle.bgcolor("black") # 배경색
# colors = ["red", "yellow", "blue", "green"]
# for i in range(100):
#     turtle.color(colors[i % 4]) # colors 인덱스를 만들어 색상을 순환시킵니다.
#     turtle.forward(i * 4) # 현재 반복 횟수 i에 4를 곱한 만큼 앞으로 전진합니다.
# #이로 인해 반복할 때마다 그리는 선의 길이가 점점 길어집니다.
#     turtle.left(91)
# turtle.done()

#no.9
import turtle
def move_forward():
    t.forward(100)
def move_backward():
    t.backward(100)
def move_right():
    t.right(5)
    t.forward(10)
def move_left():
    t.left(5)
    t.forward(10)
screen=turtle.Screen()
screen.bgcolor('black')
t=turtle.Turtle()
t.shape('turtle')
t.color('blue')
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.listen()
screen.mainloop()

# #no.10
# import seaborn as sns
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# sns.scatterplot(x=x, y=y)

# # 그래프 제목과 축 레이블 추가
# plt.title('Scatter Plot of x and y')
# plt.xlabel('x')
# plt.ylabel('y')

# # 그래프 출력
# plt.show()

# # plt.scatter(x, y)

# # # 그래프 제목과 축 레이블 추가
# # plt.title('Scatter Plot of x and y')
# # plt.xlabel('x')
# # plt.ylabel('y')

# # # 그래프 출력
# # plt.show()
