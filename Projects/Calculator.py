import math

# Ask the  user to calculate 1 or 2 numbers
input_type = int(input("Enter number (type 1 or 2) : "))

if input_type == 1:
    # For one input calculation
    num = float(input("Enter any number : "))
    
    print("1. Square")
    print("2. Qube")
    print("3. Square Root")
    
    # Choose option you want to calculate
    cl = int(input("Choose 1/2/3 : "))
    
    if cl == 1:
        # Square calculate
        print("Square : ", num**2)
    elif cl == 2:
        # Cube calculate
        print("Qube : ", num**3)
    elif cl == 3:
        # Square root calculate
        print("Square Root : ", math.sqrt(num))
    else:
        # Invalid option
        print("Invalid Number! Please enter 1 or 2 or 3 ")

elif input_type == 2:
    # For two input calculation
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multyply")
    print("4. Division")
    print("5. Modulus")
    
    # Choose option you want to calculate
    cl = int(input("Choose 1/2/3/4/5 : "))
     
    if cl == 1:
        #Add
        print("Addition : ", num1 + num2)
    elif cl == 2:
        # Subtraction
        print("Subtraction : ", num1 - num2)
    elif cl == 3:
        # Multiply
        print("Multiply : ", num1 * num2)
    elif cl == 4:
        # Devide,and zero check
        if num2 != 0:
            print("Division : ", num1 / num2)
        else:
            print("Math Error! Division by zero")
    elif cl == 5:
        # modulus
        print("Modulus : ", num1 % num2)
    else:
        # Invalid option
        print("Invalid Number! Please input 1 or 2 or 3 or 4 or 5 ")

else:
    # Invalid number input (1 or 2)
    print("Invalid Number! Please input 1 or 2 ")