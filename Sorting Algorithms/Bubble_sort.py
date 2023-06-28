def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [10, 9, 5, 4, 100, 132]
sorted_array = bubble_sort(array)
print(sorted_array)