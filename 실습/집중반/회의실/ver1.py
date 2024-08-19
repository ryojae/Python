import os
import meeting

def main():
    cate = ['검색','예약','취소','수정','종료']
    meet = ['회의실 1','회의실 2','회의실 3']
    folder = os.getcwd()
    room1=meeting.Meetingroom('room1.csv',folder)
    room2=meeting.Meetingroom('room2.csv',folder)
    room3=meeting.Meetingroom('room3.csv',folder)
    while 1:
        print('#'*30)
        print('#'*5+'회의실 예약 시스템'+'#'*5)
        print('#'*30)
        for i, menu in enumerate(cate):
            print(f'{i+1}.  {menu}')
        number = int(input('카테고리를 골라주세요:'))
        
        if number == 1:
            print(f'회의실 종류: {meet}')
            room = input('회의실을 골라주세요:')
            if room == '회의실 1':
                room1.search()
            elif room =='회의실 2':
                room2.search()
            elif room == '회의실 3':
                room3.search()
            else:
                print('없는 회의실입니다.')
        elif number == 2:
            print(f'회의실 종류: {meet}')
            room = input('회의실을 골라주세요:')
            if room == '회의실 1':
                room1.reservation()
            elif room =='회의실 2':
                room2.reservation()
            elif room == '회의실 3':
                room3.reservation()
            else:
                print('없는 회의실입니다.')
        elif number == 3:
            print(f'회의실 종류: {meet}')
            room = input('회의실을 골라주세요:')
            if room == '회의실 1':
                room1.edit()
            elif room =='회의실 2':
                room2.edit()
            elif room == '회의실 3':
                room3.edit()
            else:
                print('없는 회의실입니다.')
        elif number == 4:
            print(f'회의실 종류: {meet}')
            room = input('회의실을 골라주세요:')
            if room == '회의실 1':
                room1.cancel()
            elif room =='회의실 2':
                room2.cancel()
            elif room == '회의실 3':
                room3.cancel()
            else:
                print('없는 회의실입니다.')
        elif number == 5:
            room1.end('room1.csv')
            room2.end('room2.csv')
            room3.end('room3.csv')
            break

if __name__=='__main__':
    main()