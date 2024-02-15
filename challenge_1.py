from math import sqrt

side_1 = input("Enter the first side of a triangle.")
side_1 = int(side_1)
side_2 = input("Enter the second side of a triangle.")
side_2 = int(side_2)      
side_3 = input("Enter the third side of a triangle.")
side_3 = int(side_3)      
perimeter = side_1 + side_2 + side_3 # Matematical calculation for the perimeter.
s = perimeter/2
#print("The s value is " + str(s))      Check the s value
area_squared = s*(s-side_1)*(s-side_2)*(s-side_3) # If any of these brackets = 0 then the calculation comes back as 0.
#print("Area squared is " + str(area_squared))    Check the value of area_squared  
area = sqrt(area_squared)
if area == 0:
    print("It looks like those measurements do not give a complete triangle.") # if area = 0 then the lines must not connect to create a shape.
else:
    print("Area = " + str(area))
