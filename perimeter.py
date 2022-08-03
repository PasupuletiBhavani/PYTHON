class calculate:
    def __init__(self, l, b, r, h, a, d, c):
         self.l = l
         self.b = b
         self.r = r
         self.h = h
         self.a = a
         self.d = d
         self.c = c
    def area(self):
        a=self.l*self.b
        print("the area is", a)
    def areacircle(self):
        c=3.14*self.r
        print("the area of circle is",c)
    def areatriangle(self):
        t=self.l*self.b*self.h
        print("the area of triangle",t)
    def perimeter(self):
        A=2*(self.l+self.b)
        print("the perimeter of rectangle is",A)
    def perimetercircle(self):
        C=2*3.14*r
        print("the perimeter of circle is", C)
    def perimeterTriangle(self):
        T=self.a+self.d+self.c
        print("the perimeter of triangle is",T)
l=int(input("enetr the length"))
b=int(input("enter the breadth"))
r=int(input("enter the radius"))
h=int(input("enter height"))
a=int(input("enter side"))
d=int(input("enter side"))
c=int(input("enter side"))
obj=calculate(l, b, r, h, a, d, c)
obj.area()
obj.areacircle()
obj.areatriangle()
obj.perimeter()
obj.perimetercircle()
obj.perimeterTriangle()
