def replace(List):
    for i in range(size-1):
        List[i] = max(List[i+1:])
    return List
size = int(input("Enter the size of  list: "))
List = []
for i in range(size):
    List.append(int(input("Enter the element number " + str(i+1) + " in the List: ")))
print("After replacing ", replace(List))
