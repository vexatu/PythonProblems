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

even = list_of_numbers[0::2]
odd  = list_of_numbers[1::2]

list_of_max = [min(i, j) for i, j in zip(even, odd)]

print(*list_of_max)
