print("""What do you want to perform ?
1. Addition
2. Subtraction
3. Multiplication
4. Division""")

user_choice = input('Enter 1, 2, 3 or 4: ')
num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))


if user_choice == '1':
    print('Result', num1 + num2)
elif user_choice == '2':
    print('Result', num1 - num2)
elif user_choice == '3':
    print('Result', num1 * num2)
elif user_choice == '4':
    print('Result', num1 / num2) if num2 != 0 else print('Division by zero not possible!')
else:
    print('Invalid user choice!')
