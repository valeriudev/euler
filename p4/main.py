# https://projecteuler.net/problem=4

def is_palindrome(n):
    arr = [int(digit) for digit in str(n)]

    for i in range(0, int(len(arr)/2)):
        left = i
        right = len(arr)-1-i
        if (arr[left] != arr[right]):
            return False
    return True

palindrome = y = 0
x = 999

while (x >= 100):
    for i in range (999, 99, -1):
        num = x * i
        if (num > palindrome):
            if (is_palindrome(num)):
                palindrome = num
                y = i
    x -= 1

print(f"{x}*{y}={palindrome}")
