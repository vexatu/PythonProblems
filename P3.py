length = int(input("Introduce the number of sets: "))

while True:
    list_of_numbers = []
    for i in range(length):
        line = input(f"Enter pair #{i + 1} separated by space: ")
        nums = line.split()
        list_of_numbers.extend(int(n) for n in nums)
    if len(list_of_numbers) != length * 2:
        print("Length does not match")
        continue
    break



even = []
odd = []
for i in range(len(list_of_numbers)):
    if i % 2 == 0:
        even.append(list_of_numbers[i])
    else:
        odd.append(list_of_numbers[i])

list_of_sums = []
for i,j in zip(even, odd):
    suma = i + j
    list_of_sums.append(suma)

print(list_of_sums)
