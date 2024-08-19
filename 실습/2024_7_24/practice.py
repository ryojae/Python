# #no.4
# import glob
# print(glob.glob('?bc.txt'))
# print(glob.glob('*.txt'))
# print(glob.glob('*'))

# #no.5
# import datetime

# #(1)
# s=datetime.datetime.now()
# s1=s.strftime('%Y년 %m월 %d일')
# print('오늘의 년도, 월, 일:' ,s1)

# #(2)
# s2=s.strftime('%Y년 %m월 %d일 요일: %A')
# print(s2)

# #(3)
# t=s.strftime('%H시 %M분 %S초')
# print(t)

# #no.6
# import time
# now=time.time()
# print(f'{now}초가 지났습니다.')

# #no.7
# import time_utils
# import time

# print("Current time:", time_utils.current_time()) # a
# print("Sleeping for 2 seconds...")
# start_time = time.time()
# time_utils.sleep_for(2) # b
# print("Current time:", time_utils.current_time()) # c
# print("Elapsed time after sleeping:", time_utils.time_elapsed(start_time), "seconds")

#no.8
import Triangle
t = Triangle.Triangle()
t.getCoordsInfo()
t.calcArea()