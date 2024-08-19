import csv
import os.path
from datetime import datetime

class edit_menu:
    def __init__(self,file,folder):
        self.dict={}
        self.file=file
        if file in os.listdir(folder):
            with open(file) as file1:
                reader = csv.reader(file1)
                for row in reader:
                # print(row)
                    self.dict[row[0]]=row[1]
        else:
            if file == '커피메뉴.csv':
                self.dict={'Americano':1000,'Caffe latte':2000,'Espresso':3000}
            elif file == '차메뉴.csv':
                self.dict={'Green tea':3300}
            elif file =='케이크메뉴.csv':
                self.dict={'Cake':5000}
            elif file =='여름특선메뉴.csv':
                self.dict={'Brunch':10000,'수박 주스':5000}
        self.price = 0

    def add_menu(self):
        name = input('메뉴 이름을 넣어주세요:')
        price = input('메뉴 가격을 넣어주세요:')
        self.dict[name]=price

    def remove_menu(self):
        name = input('메뉴 이름을 넣어주세요:')
        if name in self.dict.keys():
            del self.dict[name]
        else:
            print('없는 메뉴입니다.')

    def show_menu(self):
        self.price = 0
        i=1
        for k,v in self.dict.items():
            print(i,end='.   ')
            print(k,v,'원')
            i+=1
        self.order_menu()
        return self.price
    
    def order_menu(self):
        s= int(input('메뉴를 골라주세요:'))# 옵션 선택
        if s<= len(self.dict.keys()):
            n = int(input(f'{list(self.dict.keys())[s-1]}를 몇개 주문하시겠나요 :')) #딕셔너리를 리스트로 변경 후 내과 원하는 정보 추출
            won =str(list(self.dict.values())[s-1])
            self.price += (n*int(won.strip('\n')))   #가격 정보 추출 후 가격 측정
        else:
            print('없는 메뉴입니다.')
        
    
    def save_menu(self):
        f = open(self.file, 'w')

        for k, v in self.dict.items():
        
            f.write(f"{k},{v}\n")
        f.close()
    
    def delete_menu(self):
        s= input('삭제할 메뉴를 고르세요')
        if s in self.dict.keys():
            del self.dict[s]
        else:
            print('메뉴가 없습니다.')


def background(cate):  #기본 화면 출력 및 옵션 출력
    print('=======================')
    print('=     Hello Cafe      =')
    print('=======================')
    print(datetime.now())
    i=1
    for name in cate:
        print(i,end='.  ')
        print(name)
        i+=1
    i=i-4
    return i


folder = os.getcwd()
menu_coffee=edit_menu('커피메뉴.csv',folder)
menu_tea=edit_menu('차메뉴.csv',folder)
menu_cake=edit_menu('케이크메뉴.csv',folder)
menu_summer=edit_menu('여름특선메뉴.csv',folder)
price = 0

cate =['커피','차','케이크','여름 특선 메뉴','결제','삭제','추가','종료']

def main(price,cate):
    while 1:
        i = background(cate)
        s= int(input('메뉴를 골라주세요:'))# 옵션 선택
        if s ==i+1:
            c= input('카테고리를 골라주세요:')
            if c=='커피':
                menu_coffee.delete_menu()
            elif c=='차':
                menu_tea.delete_menu()
            elif c=='케이크':
                menu_cake.delete_menu()
            elif c=='여름특선':
                menu_summer.delete_menu()
            else:
                print('카테고리가 없습니다.')
        elif s == i:
            print(f'총 가격은 {price}입니다.')
            price=0
        elif s== i+2:
            c= input('카테고리를 골라주세요:')
            if c=='커피':
                menu_coffee.add_menu()
            elif c=='차':
                menu_tea.add_menu()
            elif c=='케이크':
                menu_cake.add_menu()
            elif c=='여름특선':
                menu_summer.add_menu()
            else:
                print('카테고리가 없습니다.')
        elif s == i+3:
            print('종료합니다.')
            menu_summer.save_menu()
            menu_cake.save_menu()
            menu_coffee.save_menu()
            menu_tea.save_menu()
            break
        elif s == i-4:
            price += menu_coffee.show_menu()
        elif s== i-3:
            price += menu_tea.show_menu()
        elif s== i-2:
            price += menu_cake.show_menu()
        elif s== i-1:
            price += menu_summer.show_menu()
            
if __name__=='__main__':
    main(price,cate)