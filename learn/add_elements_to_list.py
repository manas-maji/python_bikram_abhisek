my_list = []
while True:
    user_choice = input('Do you want to add element? (Y/N) : ')
    if user_choice == 'Y':
        my_list.append(input('Enter the value: '))
    else:
        break

print(my_list)