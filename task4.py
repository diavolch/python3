'''Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.

    *Пример:*
    - для k = 8 список будет выглядеть так: 
    [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''

num = int(input('Введите число: '))
fbn = []
nfbn = []
fbn.insert(0,0)
fbn.insert(1,1)
nfbn.insert(1,1)

for i in range(2, num + 1):
    fbn.insert(i,fbn[i-1] + fbn[i-2])
    if i % 2 == 0:
        nfbn.append(fbn[i] * (-1))
    else:
        nfbn.append(fbn[i])
    
print(nfbn[::-1] + fbn)