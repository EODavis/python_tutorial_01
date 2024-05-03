def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

print('the fibonacci series up to 20:')
for x in range(20):
    print(fib_recursive(x), end=", ")
