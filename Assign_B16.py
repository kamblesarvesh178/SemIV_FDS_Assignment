def partition(per,lo,hi):               #Function for partiotioning
    if(lo<hi):                          
        pivot=lo
        i=lo
        j=hi
        while(i<j):
            while(per[i]<=per[pivot] and i<hi):
                i=i+1
            while(per[j]<=per[pivot] and i<hi):
                j=j-1
            if(i<j):
                temp=per[i]
                per[i]=per[j]
                per[j]=temp
    
    temp=per[pivot]
    per[pivot]=per[j]
    per[j]=temp

    return j


def quicksort(per,lo,hi): 
    if(lo<hi): 
        pi=partition(per,lo,hi)
        quicksort(per,lo,pi-1)
        quicksort(per,pi+1,hi)



per=[]
n=int(input("Enter the First year Students Count : "))
for i in range(n):
    m=float(input(f"Enter the Student {i+1} Percentage : "))
    per.append(m)

quicksort(per,0,n-1)

print("Sorted array is :")
for i in range(n):
    print(per[i])
    
print("Top 5 score :")
print(per[-5:n])
