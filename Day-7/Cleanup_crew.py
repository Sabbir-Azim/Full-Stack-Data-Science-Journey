try:
    n1 = int(input("Print your first number: "))
    n2 = int(input("Print your second number: "))
    
    result = n1/n2

    print("The division is ", result)

except ZeroDivisionError as e:
    print("Can't divide by zero")

finally:
    print("Execution Complete")