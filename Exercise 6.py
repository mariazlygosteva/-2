parameters = input('Введите вес (в фунтах) и высоту (в дюймах): ')
weight, height = map(float, parameters.split())
weight *= 0.453592
height *= 0.0254
height **= 2
BMI = (weight / height)
BMI = round(BMI, 3)
print(BMI)
