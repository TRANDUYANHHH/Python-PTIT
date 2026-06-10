import math
class Decimal:
    def __init__(self, xx):
        self.x = float(xx)

class Point:
     def __init__(self, da: Decimal, db: Decimal):
         self.x = da.x
         self.y = db.x
     def distance(self, other) -> str:
        ans = math.sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y))
        return f"{ans:.4f}"
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
# ezpz
