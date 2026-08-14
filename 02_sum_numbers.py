total= 0
nums = []
for i in range(5):
    num = int(input("Enter Number"))
    nums.append(num)
for i in range(5):
    total += nums[i]
print(total)