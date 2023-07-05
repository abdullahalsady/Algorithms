array = [10, 1, 7, 199, 13]
length = len(array)

for i in range(length):
    min_index = i
    for j in range(i+1, length):
        if array[j] < array[min_index]:
            array[j], array[min_index] = array[min_index], array[j]

print(array)