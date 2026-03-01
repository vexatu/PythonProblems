numbers = input()

nums = numbers.split()

line = []
for num in nums:
    line.append(int(num))

print(max(line), min(line))
