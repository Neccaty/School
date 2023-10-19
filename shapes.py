#!usr/bin/env python3
import math as math

def main():
    print("Vítejte v kalkulačce obvodů, obsahů, povrchů a objemů vybraných geometrických tvarů! Zadejte parametry nutné pro výpoček a zbytek udělá kalkulačka za Vás!")
    dimension = int(input("Jedná se o 2D(1) nebo 3D(2) objekt? [1/2] "))
    if (dimension == 1):
        shape = int(input("Jedná se o čtverec(1), obdélník(2) nebo kruh(3)? [1/2/3] "))
        operation = int(input("Počítáme obvod(1) nebo obsah(2) [1/2]? "))
        if (shape == 1):
            a = float(input("Zadejte velikost strany a v cm: "))
            print("Výsledek je {0:.2f} cm{1}".format(squareShapes(a, a, 1, operation, dimension), "" if operation == 1 else operation))
        elif (shape == 2):
            a = float(input("Zadejte velikost strany a v cm: "))
            b = float(input("Zadejte velikost strany b v cm: "))
            print("Výsledek je {0:.2f} cm{1}".format(squareShapes(a, b, 1, operation, dimension), "" if operation == 1 else operation))
        else: #shape == 3
            r = float(input("Zadejte poloměr v cm: "))
            print("Výsledek je {0:.2f} cm{1}".format(cylinderShapes(r, 1, operation, dimension), "" if operation == 1 else operation))
    else: #dimension == 2
        shape = int(input("Jedná se o krychli(1), kvádr(2), kouli(3) nebo válec(4)? [1/2/3/4] "))
        operation = int(input("Počítáme povrch(1) nebo objem(2) [1/2]? "))
        if (shape == 1):
            a = float(input("Zadejte velikost strany a v cm: "))
            print("Výsledek je {0:.2f} cm{1}".format(squareShapes(a, a, a, operation, dimension), operation+1))
        elif (shape == 2):
            a = float(input("Zadejte velikost strany a v cm: "))
            b = float(input("Zadejte velikost strany b v cm: "))
            c = float(input("Zadejte velikost strany c v cm: "))
            print("Výsledek je {0:.2f} cm{1}".format(squareShapes(a, b, c, operation, dimension), operation+1))
        elif (shape == 3):
            a = float(input("Zadejte poloměr v cm: "))
            print("Výsledek je {0:.2f} cm{1}".format(sphere(a, operation), operation+1))
        else: #shape == 4
            r = float(input("Zadejte poloměr v cm: "))
            h = float(input("Zadejte výšku v cm: "))
            print("Výsledek je {0:.2f} cm{1}".format(cylinderShapes(r, h, operation, dimension), operation+1))

def squareShapes(a, b, c, operation, dimension):
    if (operation == 2):
        return a*b*c
    elif (operation == 1 and dimension == 1):
        return 2*(a+b)
    else: #operation == 1 and dimension == 2
        return 2*a*b + 2*b*c + 2*c*a

def cylinderShapes(r, h, operation, dimension):
    if (operation == 2):
        return math.pi * r**2 * h
    elif (operation == 1 and dimension == 1):
        return 2 * math.pi * r
    else: #operation == 1 and dimension == 2
        return 2 * math.pi * r * (r+h)

def sphere(r, operation):
    if (operation == 2):
        return (4/3) * math.pi * r**3
    else: #operation == 1
        return 4 * math.pi * r**2
    
if (__name__ == "__main__"):
    main()