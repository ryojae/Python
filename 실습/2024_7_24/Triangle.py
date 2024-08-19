class Triangle:
    def __init__(self):
        pass

    def calcArea(self):
        w=((self.x3-self.x2)**2+(self.y3-self.y2)**2)**(1/2)
        h=((self.x3-self.x1)**2+(self.y1-self.y1)**2)**(1/2)
        print(f'삼각형의 넓이는 {w*h/2:.2f}입니다.')
        
    def getCoordsInfo(self):
        self.x1 = int(input("x1 좌표값을 정수로 입력하세요: "))
        self.y1 = int(input("y1 좌표값을 정수로 입력하세요: "))
        self.x2 = int(input("x2 좌표값을 정수로 입력하세요: "))
        self.y2 = int(input("y2 좌표값을 정수로 입력하세요: "))
        self.x3 = int(input("x3 좌표값을 정수로 입력하세요: "))
        self.y3 = int(input("y3 좌표값을 정수로 입력하세요: "))

if __name__ == '__main__':
    t=Triangle()
    t.getCoordsInfo()
    t.calcArea()