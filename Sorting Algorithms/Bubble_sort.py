array = [10, 9, 5, 4, 100, 132]
length = len(array)

for i in range(length):
    for j in range(length-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]


print(array)
