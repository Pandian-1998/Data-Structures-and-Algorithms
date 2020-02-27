def linearsearch(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1
k=int(input("enter the number of elements:"))
arr=[]
for i in range(k):
    f=int(input())
    arr.append(f)
    print(arr)
n=len(arr)
x=int(input("enter the element:"))
result=linearsearch(arr,n,x)
if(result ==i):
    print("Element is  present in the array",result)
else:
    print("Element is not present at the index")
    
    



def binarysearch(arr,key,low,high):
    if low > high:
        return False
    else:
        mid=(low + high)//2
        if key == arr[mid]:
            print(mid)
            return True
        elif key > arr[mid]:
            return binarysearch(arr,key,low,mid-1)
        else:
            return binarysearch(arr,key,mid+1,high)
arr=[10,12,15,18,20,25]
key=18
result=binarysearch(arr,key,0,6)
print("element is found",result)
