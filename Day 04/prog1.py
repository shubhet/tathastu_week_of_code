size = int(input("Enter the size : "))
print("Enter the elements ")
arr = []
for i in range(size):
    arr.append(input())
arr = tuple(arr)
element = input("Enter the element occurrence")
print("Tuple contains  element", arr.count(element), "times")
