def generate_fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[:n]

# Example usage
terms = 10
print(f"First {terms} terms of Fibonacci sequence: {generate_fibonacci(terms)}")
