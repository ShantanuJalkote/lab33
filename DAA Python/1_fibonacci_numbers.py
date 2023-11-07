### Non-Recursive(Iterative) Program ###

def fibonacci_non_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b
    
print(fibonacci_non_recursive(10))
#TC = O(n), SC = O(1)

### Recursive Program ###

def fibonacci_recursive(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(10))
#TC = O(2^n) or Exponential, SC = O(n) 4e