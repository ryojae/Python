def background(menu):  #기본 화면 출력 및 옵션 출력
    print('=======================')
    print('=     Hello Cafe      =')
    print('=======================')
    i=1
    for k, v in menu.items():
        print(i,end='.  ')
        print(k,'\t:\t',v,end='원\n')
        i += 1
    print(i,end='.  ')
    print('결제')
    print(i+1,end='.  ')
    print('삭제')
    print(i+2,end='.  ')
    print('추가')
    print(i+3,end='.  ')
    print('종료')
    return i

def delete_menu(menu):
    s= input('삭제할 메뉴를 고르시오: ')
    del menu[s] #삭제할 메뉴를 입력받고 해당 메뉴 삭제

def order(menu,s,price):
    n = int(input(f'{list(menu.keys())[s-1]}를 몇개 주문하시겠나요 :')) #딕셔너리를 리스트로 변경 후 내과 원하는 정보 추출
    price.append(n*int(list(menu.values())[s-1]))   #가격 정보 추출 후 가격 측정
    return price

def add_menu(menu):
    name = input('메뉴 이름을 넣어주세요:')
    price = input('메뉴 가격을 넣어주세요:')
    menu[name]=price #새로운 메뉴 추가

def main(menu,price):
    while 1:#무한 루프로 항상 기본 화면이 나오도록 함
        i = background(menu)
        s= int(input('메뉴를 골라주세요:'))# 옵션 선택
        if s ==i+1:
            delete_menu(menu)

        elif s==i:#가격 출력
            total=0
            for n in price:
                total += int(n)
            print(f'총 {total}원입니다.')
            input()# 딜레이를 줘서 가격 확인 가능하도록 함
            price=[] # 가격 초기화

        elif s== i+2:
            add_menu(menu)

        elif s== i+3:
            f = open("구구단.csv", 'w')
            for k, v in menu.items():
        
                f.write(f"{k},{v}원\n")
            f.close()
            break

        else:
            price = (order(menu,s,price))#이전 정보를 받지 않기 위해 계속 업데이트

menu = {'Americano':2500,
        'Cafe Latte':3500,
          'Espresoo':3000,
            'Green Tea': 3300}

price=[]

if __name__ == '__main__':
    main(menu,price)