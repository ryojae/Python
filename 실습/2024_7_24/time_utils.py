import time

def current_time():
    lt= time.strftime('%Y년 %m월 %d일 %H:%M:%S')
    return lt
    

def sleep_for(seconds):
    time.sleep(seconds)

def time_elapsed(start_time):
    now=time.time()
    t=now-start_time
    return t

if __name__ == '__main__':
    s, t=current_time()
    print(s)
    sleep_for(1)
    print('1')
    print(time_elapsed(t))