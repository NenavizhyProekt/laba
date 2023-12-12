def f(x,n):
    def factorial(n):
        if n == 0:
            return 1
        return factorial(n-1) * n

    return (x ** n) / factorial(n)

try:
    x = float(input('Введите число x: '))
    n = int(input('Введите число n: '))
    if n <= 0:
        raise ValueError

    print(f(x, n))

except:
    print('Введены неверные значения')
