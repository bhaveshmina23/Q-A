a=[1,2,9,8,7,4,6]
n=7

def secondLargest(a, n):
    largest = a[0]
    slargest = -1
    for i in range(1, n):
        if a[i] > largest:
            slargest = largest
            largest = a[i]
        elif a[i] < largest and a[i] > slargest:
            slargest = a[i]
    return slargest

def secondSmallest(a, n):
    smallest = a[0]
    ssmallest = float('inf')
    for i in range(1, n):
        if a[i] < smallest:
            ssmallest = smallest
            smallest = a[i]
        elif a[i] != smallest and a[i] < ssmallest:
            ssmallest = a[i]
    return ssmallest

def getSecondOrderElements(n, a):
    slargest = secondLargest(a, n)
    ssmallest = secondSmallest(a, n)
    return [slargest, ssmallest]

getSecondOrderElements(n=7, a=[5,7,9,5,2,8,2])



