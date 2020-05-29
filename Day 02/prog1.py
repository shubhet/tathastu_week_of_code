def prime(N):
    a = 2
    k = N // 2
    while k >= a:
        if N % a == 0:
            return False
        a += 1
        k = N // a
    return True


def palindrome(n):
    N = str(n)
    L = len(N)
    for i in range(L // 2):
        if N[i] != N[L - 1 - i]:
            return False
    return True

def even(n):
    if n % 2 == 0:
        return True
    return False

def armstrong(num):
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10
        sum += digit ** 3  
        temp //= 10  
    if num == sum:  
        return True 
    return False


def check():
    number=int(input("Enter a number : "))
    if(prime(number)):
        print(number," is prime number")
    if(even(number)):
        print(number," is even number")
    else:
        print(number," is odd number")
    if(palindrome(number)):
        print(number," is palindrome number")
    if(armstrong(number)):
        print(number," is armstrong number")
check()
