def find_average(numbers):
    total = 0
    for num in numbers:
        total += num
    avg = total/len(numbers)
    return avg

numbers = [10, 20, 30, 40, 50]

print(find_average(numbers))