def replace(number):
    return int(str(number).replace('0','5'))
number = int(input("Enter the number : "))
print("After replacing ", replace(number))

