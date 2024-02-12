def calc_program():
    operation =input('''+ for addition, 
- for subtraction, 
* for multiplication, 
/ for division, 
% for modulo''')
    x = float(input("Enter a number: "))
    y = float(input("Enter a number: "))
    if operation == "+":
        print(x+y)
    elif operation == "-":
        print('Result =',x-y)
    elif operation == "*":
        print('Result =',x*y)
    elif operation == "/":
        print('Result =',x/y)
    elif operation == "%":
        print('Result =',x%y)
    else:
        print('You entered an invalid operation.Rerun the program')
    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calc_program()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


calc_program()