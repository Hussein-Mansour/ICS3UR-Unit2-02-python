#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sun,Apr26/2020
# This program does basic math


def main():
    # input:
    length_of_rectangle = int(input("enter the length of the rectangle (mm) :")) 
    width_of_rectangle = int(input("enter the width of the rectangle (mm) :"))
    
    # process:
    calculation_of_area = length_of_rectangle * width_of_rectangle
    calculation_of_perimeter = 2 * (length_of_rectangle + width_of_rectangle)
    
    # output:
    print("")
    print("Area is {} mm²".format(calculation_of_area))
    print("perimeter is {} mm²".format(calculation_of_perimeter))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
