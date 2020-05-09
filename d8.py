def factorial(n):
    if n==0 or n==1:
        result = 1
    else:
        result = n*factorial(n-1)
    return result
print(factorial(int(input())))
