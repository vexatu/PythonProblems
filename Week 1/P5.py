length = int(input("Introduce the number of sets: "))

while True:
    list_of_numbers = []
    for i in range(length):
        line = input(f"Enter pair #{i + 1} separated by space: ")
        nums = line.split()
        list_of_numbers.extend(int(n) for n in nums)
    if len(list_of_numbers) != length * 3:
        print("Length does not match")
        continue
    break



a1, a2, a3 = [], [], []
for i in range(len(list_of_numbers)):
    if i % 3 == 2:
        a1.append(list_of_numbers[i])
    elif i % 3 == 1:
        a2.append(list_of_numbers[i])
    else:
        a3.append(list_of_numbers[i])

list_of_min = []
for i,j,k in zip(a1, a2, a3):
    list_of_min.append(min(i,j,k))
print(*list_of_min)
