#Intro to Tutorial Challenges
def introTutorial(V, arr):
    return arr.index(V)


#Insertion Sort - Part 1
def insertionSort1(n, arr):
    x = arr[-1]

    for i in range(2, n + 1):
        if arr[-i] > x:
            arr[-i + 1] = arr[-i]
            print(*arr)
        elif arr[-i] < x:
            arr[-i + 1] = x
            print(*arr)
            break

    if arr[0] > x:
        arr[0] = x
        print(*arr)


#Insertion Sort - Part 2
def insertionSort2(n, arr):

    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
        print(*arr)


#Correctness and the Loop Invariant
def insertion_sort(l):
    for i in range(len(l)):
        temp = l[i]
        for j in range(i - 1, -1, -1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
            else:
                l[j + 1] = temp
                break
    return l


#Running Time of Algorithms
def runningTime(arr):
    count = 0

    for i in range(len(arr)):
        temp = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
            else:
                arr[j+1] = temp
                break

    return count


#Quicksort 1 - Partition
def quickSort(arr):
    p = arr[0]
    left = []
    equal = []
    right = []

    for i in arr:
        if i < p:
            left.append(i)
        elif i == p:
            equal.append(i)
        elif i > p:
            right.append(i)

    return left+equal+right


#Counting Sort 1
def countingSort(arr):
    count = []

    for i in range(100):
        count.append(0)
        for j in arr:
            if j == i:
                count[i] += 1

    return count


#Counting Sort 2
def countingSort(arr):
    count = []
    lst = []

    for i in range(100):
        count.append(0)
        for j in arr:
            if j == i:
                count[i] += 1
    for i in range(len(count)):
        if count[i] > 0:
            lst.extend([i]*count[i])

    return lst


#Closest Numbers
def closestNumbers(arr):
    arr.sort(key = int)
    lst = []
    m = float('inf')
    for i in range(n-1):
            if arr[i+1] - arr[i] < m:
                m = arr[i+1] - arr[i]
    for i in range(n-1):
        if arr[i+1] - arr[i] == m:
            lst.append(arr[i])
            lst.append(arr[i+1])
    return lst


#Find the Median
def findMedian(arr):
    arr.sort(key=int)

    if len(arr) % 2 != 0:
        return arr[len(arr) // 2]

    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2