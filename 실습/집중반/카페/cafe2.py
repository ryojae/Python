import csv
import os.path
def background(menu,cate):  #기본 화면 출력 및 옵션 출력
    print('=======================')
    print('=     Hello Cafe      =')
    print('=======================')
    i=1
    for name in cate:
        print(i,end='.  ')
        print(name)
        i+=1
    i=i-4
    return i

def delete_menu(menu_coffee,menu_tea,menu_cake):
    c= input('삭제할 카테고리를 고르시오: ')
    s= input('삭제할 메뉴를 고르세요')
    if c == '커피':
        if s in menu_coffee.keys():
            del menu_coffee[s] #삭제할 메뉴를 입력받고 해당 메뉴 삭제
        else:
            print('메뉴가 없습니다.')
    elif c== '차':
        if s in menu_tea.keys():
            del menu_tea[s]
        else:
            print('메뉴가 없습니다.')
    elif c=='케이크':
        if s in menu_tea.keys():
            del menu_tea[s]
        else:
            print('메뉴가 없습니다.')
    else:
        print('카테고리를 잘못 선택하셨습니다.')

def order(menu,s,price):
    n = int(input(f'{list(menu.keys())[s-1]}를 몇개 주문하시겠나요 :')) #딕셔너리를 리스트로 변경 후 내과 원하는 정보 추출
    won =str(list(menu.values())[s-1])
    price.append(n*int(won.strip('\n')))   #가격 정보 추출 후 가격 측정
    return price

def add_menu(menu):
    name = input('메뉴 이름을 넣어주세요:')
    price = input('메뉴 가격을 넣어주세요:')
    cate=input('카테고리를 입력해주세요:')
    if cate == '커피':
        menu_coffee[name]=price #새로운 메뉴 추가
    elif cate == '케이크':
        menu_cake[name]=price
    elif cate =='차':
        menu_tea[name]=price
    else:
        print('잘못 입력하셨습니다.')


def show_menu(s,price):
    if s == 1:
        i=1
        for k,v in menu_coffee.items():
            print(i,end='.   ')
            print(k,v,'원')
            i+=1
        s= int(input('메뉴를 골라주세요:'))# 옵션 선택
        return(order(menu_coffee,s,price))#이전 정보를 받지 않기 위해 계속 업데이트
    elif s==2:
        i=1
        for k,v in menu_tea.items():
            print(i,end='.   ')
            print(k,v,'원')
            i+=1
        s= int(input('메뉴를 골라주세요:'))# 옵션 선택
        return(order(menu_tea,s,price))#이전 정보를 받지 않기 위해 계속 업데이트
    elif s==3:
        i=1
        for k,v in menu_cake.items():
            print(i,end='.   ')
            print(k,v,'원')
            i+=1
        s= int(input('메뉴를 골라주세요:'))# 옵션 선택
        return(order(menu_cake,s,price))#이전 정보를 받지 않기 위해 계속 업데이트
    else:
        print('잘못 입력하였습니다.')
        return price

def main(menu,price,cate):
    while 1:#무한 루프로 항상 기본 화면이 나오도록 함
        i = background(menu,cate)
        s= int(input('메뉴를 골라주세요:'))# 옵션 선택
        if s ==i+1:
            delete_menu(menu_coffee,menu_tea,menu_cake)

        elif s==i:#가격 출력
            total=0
            if len(price)>0:
                for n in price:
                    total += int(n)
                print(f'총 {total}원입니다.')
                input()# 딜레이를 줘서 가격 확인 가능하도록 함
                price=[] # 가격 초기화
            else:
                print('0원입니다.')

        elif s== i+2:
            add_menu(menu)
            

        elif s== i+3:
            f = open("커피메뉴.csv", 'w')
            for k, v in menu_coffee.items():
        
                f.write(f"{k},{v}\n")
            f.close()
            f = open("차메뉴.csv", 'w')
            for k, v in menu_tea.items():
        
                f.write(f"{k},{v}\n")
            f.close()
            f = open("케이크메뉴.csv", 'w')
            for k, v in menu_cake.items():
        
                    f.write(f"{k},{v}\n")
            f.close()
            break

        else:
            price = show_menu(s,price)



menu_coffee={}
menu_tea={}
menu_cake={}
folder = os.getcwd()
if '커피메뉴.csv' in os.listdir(folder):
    with open('커피메뉴.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            menu_coffee[row[0]]=row[1]
else:
    menu_coffee={'Americano':1000,'Caffe latte':2000,'Espresso':3000}
if '차메뉴.csv' in os.listdir(folder):
    with open('차메뉴.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            menu_tea[row[0]]=row[1]
else:
    menu_tea={'Green tea':3300}
if '차메뉴.csv' in os.listdir(folder):
    with open('케이크메뉴.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            menu_cake[row[0]]=row[1]        
else:
    menu_cake={'Cake':5000}
# print(menu_coffee)
# print(menu_tea)
# print(menu_cake)
# menu_coffee={'Americano':1000,'Caffe latte':2000,'Espresso':3000}
# menu_tea={'Green tea':3300}
# menu_cake={'Cake':5000}
menu = [menu_coffee,menu_tea,menu_cake]
cate =['커피','차','케이크','결제','삭제','추가','종료']
price=[]

if __name__ == '__main__':
    main(menu,price,cate)