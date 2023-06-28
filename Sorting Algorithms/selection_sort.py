def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if array[j] < array[min_index]:
                array[j], array[min_index] = array[min_index], array[j]
    return array

array = [10, 1, 7, 199, 13]
sorted_array = selection_sort(array)
print(sorted_array)