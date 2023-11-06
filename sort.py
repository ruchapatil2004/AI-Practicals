def getdata(array,size):
    for i in range (size):
        p = int(input("Enter the elements: "))
        array.append(p)
def selection(array,size):
    for i in range (size):
        min = i
        for j in range(i+1,size):
            if array[j]<array[min]:
                min = j
        (array[i],array[min])=(array[min],array[i])
    print("Selection sort: ",array)
def bubble(array,size):
    for i in range(size):
        for j in range(size-i-1):
            if(array[j]>array[j+1]):
                (array[j+1],array[j])=(array[j],array[j+1])
    print("Bubble Sort: ",array)
def partition(array,low,high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j]<=pivot:
            i = i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quick(array,low,high):
    if low<high:
        pi = partition(array,low,high)
        quick(array,low,pi-1)
        quick(array,pi+1,high)
    #print("Quick Sort",array)
def insertion(array,size):
    for i in range(1,size):
        key = array[i]
        j = i -1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j = j-1
        array[j+1]= key
    print("Insertion Sort", array)
def merge(array,size):
    if size>1:
        mid = size//2
        sub1 = array[:mid]
        sub2 = array[mid:]
        merge(sub1, len(sub1))
        merge(sub2, len(sub2))
        i=j=k=0
        while (i<len(sub1) and j<len(sub2)):
            if sub1[i]<sub2[j]:
                array[k] = sub1[i]
                i+=1
            else:
                array[k]=sub2[j]
                j+=1
            k+=1
        while(i<len(sub1)):
            array[k]=sub1[i]
            i+=1
            k+=1
        while(j<len(sub2)):
            array[k]=sub2[j]
            j+=1
            k+=1
    print("Merge Sort: ", array)
size = int(input("Enter the size of array: "))
array = []
ans = True
while(ans):
    print("Enter your choice:")
    print("1. Elements.")
    print("2. Selection Sort.")
    print("3. Bubble Sort.")
    print("4. Quick Sort.")
    print("5. Insertion Sort.")
    print("6. Merge Sort.")
    print("7. Exit.")
    ch = int(input("Enter your choice: "))
    if(ch==1):
        getdata(array,size)
    elif(ch==2):
        selection(array,size)
    elif(ch==3):
        bubble(array,size)
    elif(ch==4):
        quick(array,0,size-1)
        print("Quick Sort",array)
    elif(ch==5):
        insertion(array,size)
    elif(ch==6):
        merge(array,size)
    elif(ch==7):
        ans = False
    else:
        print("Please enter the correct choice...")