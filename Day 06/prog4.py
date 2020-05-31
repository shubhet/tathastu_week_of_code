s = input("Enter the number: ")
s1= str(s)
l = len(s) - 2
Min = s[-1]
for i in range(l, -1, -1):
    a = s[i]
    if a < Min:
        s = s[:i] + Min + a + s[l:i:-1]
        break
if s1 == s:
    print("No number greater than the given number.")
else:
    print("The next greater number is",s)
