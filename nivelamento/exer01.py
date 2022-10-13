array = [1,7,2,9]
tamanhoDoArray=4

for i in range(0, 100):
    array.append(array[i] + array[(i + 1)])
    if array[i+tamanhoDoArray]>100:
        break

print(array)
