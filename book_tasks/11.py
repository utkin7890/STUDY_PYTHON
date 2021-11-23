print("\n Operation divided two numbers" + "\nEnter 'q' to quit\n")

while True:
    a = input("Input first number a= ")
    if a == 'q':
        break
    b = input("Input second number b= ")
    if b == 'q':
        break
    try:
        divide_res = float(a)/float(b)
    except ZeroDivisionError:
        print("\nYou cannot divide by zero!\n")
    else:
        print("\nResult a/b= " + str(divide_res))



'''
try:
    while True:
        print("\n Operation divided two numbers" + "\nEnter 'q' to quit\n")
        a = float(input("Input first number a= "))
        b = float(input("Input second number b= "))
    divide_res = a/b
    print("\nResult a/b= " + str(divide_res))
except ValueError:
    print("\nData type error, you enter not a number!")
'''
