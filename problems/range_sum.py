number = int(input('Enter number: '))

result = 0
for i in range(1, number + 1):
    result += i

print(f'Sum of 1 to {number} = {result}')
