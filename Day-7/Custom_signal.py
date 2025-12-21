def custom_signal():
    number = int(input("Enter a number: "))

    if number < 0:
        raise ValueError("No Negatives")
    
    print("The number is not negative")

custom_signal()