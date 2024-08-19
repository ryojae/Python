pi =3.1415
def circumference(r):
    return  2 * pi * r
class Circle:
    def __init__(self,r):
        self.r=r
    def getCircumference(self):
        return self.r