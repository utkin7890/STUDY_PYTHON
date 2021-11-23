'''
Exercise 4. The area of the garden plot
Create a program that asks the user for the length and width of the
garden plot in feet. Display the area of the plot in acres.
'''

garden_length = float(input("Input length of the garden plot in feet:"))
garden_width = float(input("Input width of the garden plot in feet:"))
garden_square_feet = garden_length * garden_width
proportion_feet_in_acre = 43560
garden_square_acres = garden_square_feet/proportion_feet_in_acre

print("\nSqure of the garden plot in acres: "+str(garden_square_acres)+ " acres")