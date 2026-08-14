numbers = []
for i in range(5):
    num = int(input("Enter Number:"))
    numbers.append(num)
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print("Largest = ",maximum)