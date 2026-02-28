liste = int(input("Nr de perechi: "))
new_list = []
for i in range(1, liste+1):
    numbers = input().split()
    new_list.append(str(min(int(numbers[0]), int(numbers[1]))))
print(" ".join(new_list))



