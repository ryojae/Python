import datetime
import csv
import os

def transtime(time):
    return datetime.datetime.strptime(time, '%H:%M')

class Meetingroom():
    def __init__(self,file,folder):
        self.meet=['회의실 1','회의실 2','회의실 3']
        self.lst=[] 
        # 파일에서 회의실 정보 호출
        if file in os.listdir(folder):
            with open(file,'r') as f:
                reader = csv.reader(f)
                # print(reader)
                i=0
                for row in reader:
                    self.lst.append({row[0]:row[1]})
                    self.lst[i][row[2]]=row[3]
                    self.lst[i][row[4]]=row[5]
                    self.lst[i][row[6]]=row[7]
                    self.lst[i][row[8]]=row[9]
                    i+=1

    def reservation(self):
        day = input('예약 날짜를 입력해주세요 (YYYY-MM-DD):')
        start1 = input('이용 시작 시간을 입력해주세요 (HH:MM):')
        end1 = input('이용 종료 시간을 입력해주세요 (HH:MM):')
        start = transtime(start1)
        end = transtime(end1)
        
        if start >= end:
            print("이용 시작 시간은 이용 종료 시간보다 이전이어야 합니다.")
            return

        reserve_state = True
        for reservation in self.lst:
            if day == reservation['날짜']:
                reserved_start = transtime(reservation['이용 시작 시간'])
                reserved_end = transtime(reservation['이용 종료 시간'])
                if not (end <= reserved_start or start >= reserved_end):
                    reserve_state = False
                    break

        if reserve_state:
            self.lst.append({
                '날짜': day,
                '이용 시작 시간': start1,
                '이용 종료 시간': end1,
                '성함': input('예약자 이름을 알려주세요:'),
                '이용인원': input('이용 인원을 입력해주세요:')
            })
            print("예약이 완료되었습니다.")
        else:
            print('이미 예약이 되어있습니다.')
    
    def search(self):
        n=1
        name = input('예약자 성함을 입력해주세요:')
        for i in self.lst:
            if i['성함'] == name:
                print(f'{n}.   {i}')
                n+=1
            else:
                print('예약 내역이 없습니다.')
        
    def edit(self):
        name = input('예약자의 성함을 입력해주세요:')
        cnt1=0
        cnt2=0
        data = []
        for i in self.lst:
            if name == i['성함']:
                cnt1 += 1
                data.append(i)
            else:
                cnt2 += 1
        if cnt2 == len(self.lst):
            print('예약 내역이 없습니다.')
        elif cnt1 == 1:
            print(data[0])
            n=0
        elif cnt1 >=2:
            for i in range(1,len(data)+1):
                print(f'{i}.  {data[i-1]}')
            n = int(input('몇번 정보를 수정하겠습니까?'))-1
            print(data[n])
        data[n]['이용인원']=input('이용인원을 입력해주세요:')
        print(self.lst)
        
    def cancel(self):
        name = input('예약자의 성함을 입력해주세요:')
        cnt1=0
        cnt2=0
        data = []
        for i in self.lst:
            if name == i['성함']:
                cnt1 += 1
                data.append(i)
            else:
                cnt2 += 1
        if cnt2 == len(self.lst):
            print('예약 내역이 없습니다.')
        elif cnt1 == 1:
            print(data[0])
            n=0
        elif cnt1 >=2:
            for i in range(1,len(data)+1):
                print(f'{i}.  {data[i-1]}')
            n = int(input('몇번 정보를 취소하겠습니까?'))-1
            print(f'선택한 정보:\n {data[n]}')
        for i in self.lst:
            if i ==data[n]:
                self.lst.remove(i)
    
    def end(self,file):
        with open(file,'w') as file:
            for i in range(len(self.lst)):
                for j in self.lst[i]:
                    file.write(f'{j},{self.lst[i][j]},')
                file.write('\n')        
