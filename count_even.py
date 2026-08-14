def count_even(numbers):
    count = 0 
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

numbers = [10, 15, 22, 7, 40]

print(count_even(numbers))