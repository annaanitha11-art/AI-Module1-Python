numbers = []
total = 0
for i in range(1,6):
    num = int(input(f"Enter number {i} :"))
    numbers.append(num)
    total += num
count = 0
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num % 2 == 0:
        count += 1
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
avg = total/len(numbers)
print("Total =",total)
print("Average =",avg)
print("Largest Number =",largest)
print("Smallest Number =",smallest)
print("Total number of Even numbers =",count)
