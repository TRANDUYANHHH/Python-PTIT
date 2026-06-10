class Rectangle:
    def __init__(self, hh, ww, cc):
        self.h = hh
        self.w = ww
        self.c = cc
    def perimeter(self):
        return (self.h + self.w) * 2
    def area(self):
        return self.h * self.w
    def color(self):
        return self.c[0].upper() + self.c[1:].lower()
    def check(self):
        return self.h > 0 and self.w > 0

arr = input().split()
try:
    rr = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    if not rr.check():
        print("INVALID")
    else:
        print(f"{rr.perimeter()} {rr.area()} {rr.color()}")
except:
    print("INVALID")
