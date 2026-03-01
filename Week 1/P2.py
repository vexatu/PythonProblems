length = int(input("Input how many numbers: "))
numbers = input("Input numbers with space between them: ")
A = []

for num in numbers.split(): #iterates in the numbers list of strings and splits the strings inserted
    A.append(int(num)) #adds the split strings to the empty list and transform each in integer values

total = sum(A)
print(total)


