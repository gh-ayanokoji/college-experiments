while True:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: ")) 

    print('''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exponential
    6. Modulus (Gives remainder after division)
    ''')

    choice = int(input("\nEnter your choice: "))

    match choice:

        case 1:
            print(num1, '+', num2, '=', num1 + num2)

        case 2:
            print(num1, '-', num2, '=', num1 - num2)

        case 3:
            print(num1, '*', num2, '=', num1 * num2)

        case 4:
            div = int(input("Which division do you want:\n1. With Decimal\n2. Without Decimal\nEnter your choice: "))
            match div:
                case 1:
                    print(num1, '/', num2, '=', num1 / num2)
                
                case 2:
                    print(num1, '/', num2, '=', num1 // num2)

        case 5:
            print(num1, '**', num2, '=', num1 ** num2)

        case 6:
            print(num1, '%', num2, '=', num1 % num2)

    quit = input("Press Enter to use Calculator again or Press Q to Quit: ")    
    match quit:
        case 'Q':
            break
        case 'q':
            break
        case _ :
            continue

        