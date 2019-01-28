import random
import math
print("Quadratic function test")
print("This program will test your ability to find x in a quadratic function")
qcounter = 1
wcounter = 1
while qcounter < 11:
    a = 1
    c = random.randrange(0,200)
    b = random.randrange(c,300)
    q1 = b*b
    q2 = 4*a*c
    q3 = q1-q2
    q4 = math.sqrt(q3)
    qb=b*-1
    q5 = qb+q4
    q6 = qb-q4
    duba = 2*a
    qfinal1 =  float(format(q5/duba, '.2f'))
    qfinal2 = float(format(q6/duba, '.2f'))
    bigger = qfinal1 if qfinal1 > qfinal2 else qfinal2
    smaller  = qfinal1 if qfinal1 < qfinal2 else qfinal2
    print("x^2+", b, "x+",c ,"= 0")
    usr1 = float(input("First answer: "))
    usr2 = float(input("Second Answer: "))
    usr1 = float(format(usr1, '.2f'))
    usr2 = float(format(usr2, '.2f'))
    usrbig = usr1 if usr1 > usr2 else usr2
    usrsmall = usr2 if usrbig == usr1 else usr1
    if usrbig == bigger and usrsmall == smaller:
        print("Correct!")
        qcounter = qcounter + 1
    else:
        print("WRONG!")
        print(bigger, smaller)
        qcounter = qcounter + 1
        wcounter = wcounter + 1
print("Amount wrong: ", wcounter)
print("Thank You")
