size = int(input("Enter the number of string: "))
List = []
for i in range(size):
    List.append(input("Enter the string number " + str(i + 1) + ": ").strip())
prefix = List[0]
for i in range(1,size):
    while True:
        if List[i].startswith(prefix):
            break
        prefix = prefix[:-1]
print("The largest prefix is \"" + prefix +"\"")
