#!/usr/bin/env python3

# Formula for fibonacci is f(n) = f(n-1) + f(n-2)
def print_fibonacci(length):
    num1 =0
    num2=1
    fib=[num1,num2]
    for i in range(length):
        sum = num1 + num2
        num1 = num2
        num2 = sum
        fib.append(num2)
    print(fib[:length])

print_fibonacci(9)