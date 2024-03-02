bulls = input('Введите количество быков и семей через пробел: ')
N, K = map(int, bulls.split())
bulls_per_family = K // N
remaining_bulls = K % N
print(remaining_bulls)
