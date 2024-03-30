class Area:
    def __init__(self) -> None:
        pass

    def rectangle(self):
        self.l = float(input("enter length: "))
        self.w = float(input("enter width: "))
        print(self.l * self.w)

    def square(self):
        self.s = float(input("enter length: "))
        print(self.s * self.s)

    def circle(self, val) -> None:
        self.c = val
        print(3.14 * (self.c*2))

    def triangle(self, height, breadth):
        self.h = height
        self.b = breadth
        print((self.h * self.b) / 2)


obj = Area()
obj.circle(23)
obj.rectangle()
obj.triangle(2, 3)
obj.square()