#assignment 5 Justin Phillips
from math import pi


def circleRadius(radius):
    #r = float(input ( "Enter the radius of the circle:"))
    print ("the area is a radius: "+ str(radius) + " is: " + str(pi * radius**2))


def firstlastlist(thelist):
    size = len(thelist)
    end = thelist.pop()
    begin = thelist[0]
    print("start: %s end: %s" %(begin, end))

def twodates(date1, date2):
    daysbetween = date1- date2
    return daysbetween

def main():
    list1 = [1,2,3,4,5,6,7]
    firstlastlist(list1)

if __name__ == '__main__':
    main()
    #list1 = [1,2,3,4,5,6,7]
    #firstlastlist(list1)