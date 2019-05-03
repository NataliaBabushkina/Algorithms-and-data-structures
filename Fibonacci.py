# Бабушкина Н. В., 05-703, Вычисление чисел Фибоначчи
def fib(n): # рекурсивная функция вычисления чисел Фибоначчи 
    if (n<2):
        return 1
    return fib(n-1)+fib(n-2)

def fib2(n): # функция вычисления чисел Фибоначчи с помощью цикла
    f0=1
    f1=1
    if n>=2:
        for k in range(n-1):
            f0, f1=f1, f0+f1
    return f1

a=int(input('Введите количество чисел Фибоначчи: '))
print('Вычисление чисел Фибоначчи итеративным способом:\n')
for k in range(a):
    print(k, fib2(k))
print('Вычисление чисел Фибоначчи рекурсивным способом:\n')    
for k in range(a):
    print(k, fib(k))
