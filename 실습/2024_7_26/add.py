# #no.1
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.random.normal(size=100)
# y=2.5*x+np.random.normal(size=100)
# plt.scatter(x,y)
# plt.title('Numpy')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# #no.2
# import tkinter as tk
# root = tk.Tk()
# root.title('Tkinter')
# root.geometry('300x100')
# label = tk.Label(root,text='Tkinter GUI를 시작하셨습니다.')
# label.pack(pady=20)
# root.mainloop()

# #no.3
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# def calculate():
#     if feetInput.text() =='':
#         meter=float(meterInput.text())
#         feet=meter/0.3048
#         result.setText(f'피트: {feet: .4f}')
#     else:
#         feet=float(feetInput.text())
#         meter=feet*0.3048
#         result.setText(f'미터: {meter: .4f}')

# app = QApplication(sys.argv)
# win = QWidget()
# win.setWindowTitle('피트에서 미터로 변환')

# feetLabel=QLabel('피트')
# feetInput=QLineEdit()
# meterLabel=QLabel('미터')
# meterInput=QLineEdit()
# bt=QPushButton('Calculate')
# bt.clicked.connect(calculate)
# result=QLabel('결과: ')

# inputfeet=QHBoxLayout()
# inputfeet.addWidget(feetLabel)
# inputfeet.addWidget(feetInput)

# input_meter=QHBoxLayout()
# input_meter.addWidget(meterLabel)
# input_meter.addWidget(meterInput)

# buttonLayout = QHBoxLayout()
# buttonLayout.addWidget(bt)

# resultLayout = QHBoxLayout()
# resultLayout.addWidget(result)

# mainLayout = QVBoxLayout()
# mainLayout.addLayout(inputfeet)
# mainLayout.addLayout(input_meter)
# mainLayout.addLayout(buttonLayout)
# mainLayout.addLayout(resultLayout)

# win.setLayout(mainLayout)

# win.show()
# sys.exit(app.exec_())

# #no.5
# import turtle

# # 창 설정
# window = turtle.Screen()
# window.title("반대편으로 순간이동하는 거북이")
# window.bgcolor("white")
# window.setup(width=600, height=600)

# # 거북이 설정
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)

# # 창의 크기
# width = window.window_width()
# height = window.window_height()

# # 거북이가 창을 벗어나면 반대편으로 순간이동하는 함수
# def teleport_if_out_of_bounds():
#     x, y = t.pos()
#     if x > width / 2:
#         t.setx(-width / 2)
#     elif x < -width / 2:
#         t.setx(width / 2)
#     if y > height / 2:
#         t.sety(-height / 2)
#     elif y < -height / 2:
#         t.sety(height / 2)

# # 거북이를 움직이는 함수
# def move_turtle():
#     t.forward(5)  # 작은 거리로 자주 움직이도록 설정
#     teleport_if_out_of_bounds()
#     window.ontimer(move_turtle, 10)  # 짧은 주기로 호출

# # 프로그램 실행
# move_turtle()

# # 창 닫힘 방지
# window.mainloop()


# #no.7
# import pygame
# import sys

# # Pygame 초기화
# pygame.init()

# # 윈도우 크기 설정
# window_size = (800, 600)

# # 윈도우 생성
# screen = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Pygame 윈도우 생성 및 배경색 설정")

# # 배경색 설정 (RGB 값 사용)
# background_color = (0, 128, 255)  # 파란색

# # 메인 루프
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # 화면 채우기
#     screen.fill(background_color)

#     # 화면 업데이트
#     pygame.display.flip()

# # Pygame 종료
# pygame.quit()
# sys.exit()

#no.8
import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("움직이는 공")

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 공 설정
ball_radius = 15
ball_pos = [screen_width // 2, screen_height // 2]
ball_vel = [0, 0]  # 초기 속도는 0
ball_speed = 5

# 게임 루프
running = True
start_moving = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not start_moving:
                ball_vel = [random.choice([-1, 1]) * ball_speed, random.choice([-1, 1]) * ball_speed]
                start_moving = True

    if start_moving:
        # 공의 위치 업데이트
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # 벽에 부딪히면 반사
        if ball_pos[0] <= ball_radius or ball_pos[0] >= screen_width - ball_radius:
            ball_vel[0] = -ball_vel[0]
        if ball_pos[1] <= ball_radius or ball_pos[1] >= screen_height - ball_radius:
            ball_vel[1] = -ball_vel[1]

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)
    pygame.display.flip()

    # 프레임 속도 조절
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
