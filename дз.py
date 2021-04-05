def fibonacci(n):
    current = 1
    if n > 2:
        current = fibonacci(n-1) + fibonacci(n-2)
    return current
if __name__ == "__main__":
    n = int(input('Введите искомый элемент последовательности ряда Фибоначчи : '))
print (fibonacci(n))
