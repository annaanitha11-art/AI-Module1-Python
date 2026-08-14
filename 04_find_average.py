numbers = []
total = 0
for i in range(5):
    num=int(input("Enter Numbers:"))
    numbers.append(num)
    total += numbers[i]
    
print("Average = ",total/len(numbers))