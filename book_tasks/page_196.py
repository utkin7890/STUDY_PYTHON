print("\n Operation divided two numbers" + "\nEnter 'q' to quit\n")

while True:
    a = input("Input first number a= ")
    if a == 'q':
        break
    b = input("Input first number b= ")
    if b == 'q':
        break

    try:
        divide_res = float(a) / float(b)
    except ZeroDivisionError:
        print("\nYou cannot divide by zero!\n")
    except ValueError:
        print("\nYou cat enter only numbers!\n")
    else:
        print("\nResult a/b= " + str(divide_res))


