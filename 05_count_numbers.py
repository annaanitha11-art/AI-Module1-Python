numbers = []
count = 0
for i in range(5):
    num=int(input("Enter Numbers:"))
    numbers.append(num)
    if num % 2 == 0:
        count+=1
print("Number of even numbers = ",count)