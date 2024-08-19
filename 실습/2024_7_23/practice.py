# #no.7
# class Rectnagle:
#     def __init__(self,x,y,width,height):
#         self.x=x
#         self.y=y
#         self.width=width
#         self.height=height
#     def print(self):
#         print(f'x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}')
# rec=Rectnagle(1,2,3,4)
# rec.print()

#no.8
class parent:
    def __init__(self):
        self.name='parent'

    def foo(self):
        print(f'{self.name}')

class child(parent):
    def __init__(self):
        self.name='child'
        print('생성 성공')

test=child()
test.foo()