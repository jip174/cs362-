#assignment 5 Justin Phillips
from math import pi
from datetime import date

def firstrun():
    return "success"

def circleRadius(radius):
    #r = float(input ( "Enter the radius of the circle:"))
    area = pi * radius ** 2
    print ("the area is a radius: "+ str(radius) + " is: " + str(pi * radius**2))
    return area

def firstlastlist(thelist):
    size = len(thelist)
    #end = thelist[size]
    end = thelist.pop()
    begin = thelist[0]
    print("start: %s end: %s" %(begin, end))
    return begin, end

def twodates(date1, date2):
    daysbetween = abs(date2 - date1).days
    return daysbetween
"""
def main():
    list1 = [1,2,3,4,5,6,7]
    firstlastlist(list1)

if __name__ == '__main__':
    main()
    #list1 = [1,2,3,4,5,6,7]
    #firstlastlist(list1)
"""