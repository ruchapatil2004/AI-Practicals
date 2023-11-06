def getdata(array,size):
    for i in range(size):
        p = int(input("Enter the elements:"))
        array.append(p)
def selection(array,size):
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if array[j]<array[min]:
                min = j
        (array[i], array[min]) = (array[min], array[i])
    print("Selection Sort: ", array)

size = int(input("Enter the size of array:"))
array = []
getdata(array,size)
selection(array,size)