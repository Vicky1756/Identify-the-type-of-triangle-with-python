import math
import random
iso = 0
sca = 0
equ = 0
ri = 0
ob = 0
ac = 0
def isValidTriangle(a, b, c):
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        return False
    else:
        return True

def getPerimeter(a, b, c):
    perim = a + b + c
    return (str(perim))

def getArea(a, b, c):
    re = (a + b + c) / 2
    area = math.sqrt(re * (re - a) * (re - b) * (re - c))
    return  round((area),2)

def getTypeBySide(a, b, c):
    global equ,iso,sca
    if  a == b == c:
        equ += 1
        return ("Equilateral ")
    elif a == b or b == c or a == c:
        iso += 1
        return ("Isoceles")
    elif a != b and b != c and a != c:
        sca += 1
        return ("Scalene")

def getTypeByAngle(a, b, c):
    global ri,ob,ac
    if a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b:
        ri += 1
        return ("Right")
    elif a * a + b * b < c * c or b * b + c * c < a * a or c * c + a * a < b * b:
        ob += 1
        return ("Obtuse")
    else:
        ac += 1
        return ("Acute")

def main():
    h = 0
    print("   No    a    b   c    Type by Side    Type by Angle   Perimeter   Area" +
          "\n------------------------------------------------------------------------")

    for i in range(1000):
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        c = random.randint(1, 99)
        # print("Random: ", a, b, c)
        d = isValidTriangle(a, b, c)
        if d == False:
            print(str(i + 1).rjust(4) + " :" + str(a).rjust(5) + str(b).rjust(4) + str(c).rjust(4) +
                  str("x").rjust(12) +
                  str("x").rjust(17))
            continue
        else:
            h+= 1
            print(str(i + 1).rjust(4) + " :" + str(a).rjust(5) + str(b).rjust(4) + str(c).rjust(4) +
                  str(getTypeBySide(a, b, c).rjust(12)) +
                  str(getTypeByAngle(a, b, c)).rjust(17) +
                  str(getPerimeter(a, b, c)).rjust(12) + str(getArea(a, b, c)))
    print("Total Data : 1000")
    print("Total Triangle : ",h)
    print("Total Equilateral Triangle :",equ)
    print("Total Scalene Triangle :", sca)
    print("Total Isosceles Triangle :", iso)
    print("Total Right Triangle :", ri)
    print("Total Acute Triangle :", ac)
    print("Total Obtuse Triangle :", ob)

if __name__ == "__main__":
    main()