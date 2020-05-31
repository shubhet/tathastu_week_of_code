size = int(input("Enter the number: "))
List = []
for i in range(size):
    List.append(int(input("Enter the element " + str(i + 1) + " in the List: ")))
a, b, c = sorted(List)[-3:]
print("Highest product possibled by multiplying 3 ", a * b * c)
