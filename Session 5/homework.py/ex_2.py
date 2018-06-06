numbers = [1, 6, 9, 2, 3, 3, 4, 5, 9, 7, 1, 6]
print(numbers)
num = int(input('enter a number: '))
count = 0

for i in numbers:
    if i == num:
        count += 1
print(num, 'appears:', count, 'times in my list')