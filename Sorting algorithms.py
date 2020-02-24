def bubblesort(a):
    n= len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

g=int(input("enter the no of elements:"))
a=[]
for i in range(g):
    f=int(input())
    a.append(f)
    print(bubblesort(a))

def selectionsort(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if a[min_index]>a[j]:
                min_index=j
            a[i],a[min_index]=a[min_index],a[i]
    return a
g=int(input("enter the no of elements:"))
a=[]
for i in range(g):
    f=int(input())
    a.append(f)
    print(selectionsort(a))

def insertionsort(a):
    for i in range(1,len(a)):
        key = a[i]
        j=i-1
        while j >=0 and key < a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a
g=int(input("no of elements:"))
a=[]
for i in range(g):
    f=int(input())
    a.append(f)
    print(insertionsort(a))

def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
    
def quicksort(arr,low,high):
    if low < high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr
g=int(input("no of elements:"))
a=[]
for i in range(g):
    f=int(input())
    a.append(f)
print(quicksort(a,0,len(a)-1))






def mergesort(x):
    if len(x)==0 or len(x)==1:
        return x
    else:
        middle = len(x)//2
        a=mergesort(x[:middle])
        b=mergesort(x[middle:])
    return merge(a,b)
def merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a)==0:
        c +=b
    else:
        c +=a
    return c
    
g=int(input("no of elements:"))
h=[]
for i in range(g):
    f=int(input())
    h.append(f)
print(mergesort(h))
    

        
            
            

