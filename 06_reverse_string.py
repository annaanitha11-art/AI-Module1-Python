text = input("Enter a string:")
rstr = ""
for i in range(len(str)-1,-1,-1):
    rstr += text[i]
print("reversed string = ",rstr)