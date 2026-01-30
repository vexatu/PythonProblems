n = int(input("Introduceti marimea listei:"))
element = input("Introduceti elementele listei: ")
my_list = list(map(int, element.split()))
print(my_list)
total = 0
for num in my_list:
    total += num
print(total)