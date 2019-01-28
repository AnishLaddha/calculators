
import math
print("Welcome to my area and quadratics calculator!")
def areaquadcalc():
    print("choose your shape:")
    print("1.Circle")
    print("2. Triangle")
    print("3. Rectangle/Square")
    print("4.Pentagon")
    print("5.Hexagon")
    print("6. Quadratic formula")
    usrchoice = int(input("choose your shape: "))
    if usrchoice == 3:
        rbase= float(input("enter base: "))
        rheight = float(input("enter height: "))
        rarea = rbase * rheight
        print(rarea)
    elif usrchoice == 2:
        tbase = float(input("enter base: "))
        theight = float(input("enter height: "))
        tarea = tbase*theight*0.5
        print(tarea)
    elif usrchoice == 4:
        pside = float(input("enter the side of the pentagon: "))
##pp1 is gonna be the square root 5
        pp1 = math.sqrt(5)
##pp2 is multiplying it by 2 and adding 5
        pp2 = 5+2*pp1
##pp3 is multiplying the whole thing by 5
        pp3 = pp2 * 5
##pp4 is taking the squareroot of the main middle part
        pp4 = math.sqrt(pp3)
##ps2 is squareing the side
        ps2 = pside*pside
##pp5 is putting it all together
        pp5 = 0.25*pp4*ps2
        print(pp5)
    elif usrchoice == 1:
        cradius = float(input("Enter radius of circle: "))
        carea = math.pi*cradius*cradius
        print(carea)
    elif usrchoice == 6:
        print("fyi, Will be referencing equation ax^2+bx+c = 0")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
## bsquare is q1
        q1 = b*b
##q2 is -4ac
        q2 = 4*a*c
##q3 is the part inside root
        q3 = q1-q2
        if q3 >= 0:
##square root part is q4
            q4 = math.sqrt(q3)
##qb is negative b
            qb=b*-1
##q5 is the plus part
            q5 = qb+q4
##q6 is the minus part
            q6 = qb-q4
##duba is 2a
            duba = 2*a
##qfinal1 is 1 of the answers
            qfinal1 = q5/duba
##qfinal 2 is second answer
            qfinal2 = q6/duba
            print(qfinal1, "and", qfinal2)
        else:
            print("No solutions")
    elif usrchoice == 5:
        hside = float(input("Enter the side: "))
        h1 = math.sqrt(3)*3
        h2 = h1/2
        hsq = hside**2
        harea= h2*hsq
        print(harea)
    else:
        print("Enter a integer from 1-6 , fool")
    areaquadcalc()
areaquadcalc()
