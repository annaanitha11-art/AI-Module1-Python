name = input("Enter Student Name:")
marks = []
total = 0
for i in range(1,6):
    mark = int(input(f"Enter marks in subject {i}: "))
    marks.append(mark)
    total += mark
highest = marks[0]
lowest = marks[0]
for mark in marks:
    if mark > highest:
            highest = mark
    if mark < lowest:
            lowest = mark

avg = total/len(marks)
print("Student:",name)
print("Total :" ,total)
print("Average :",avg)
print("Highest :",highest)
print("Lowest :",lowest)

 