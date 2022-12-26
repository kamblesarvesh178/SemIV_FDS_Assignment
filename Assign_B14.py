def BubbleSort():
    c1=int(input("Student Count:"))
    print(f"Enter the {c1} student first year percentage (separating spaces) ")
    mark=list(map(float,input().split()))
    n=len(mark)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if mark[j]>mark[j+1]:
                temp=mark[j]
                mark[j]=mark[j+1]
                mark[j+1]=temp
    print("Sorted Array is :")
    for i in range(n):
        print(mark[i])
    print("Top 5 Score are : ")
    print(mark[-5:n])
    
    
def SelectionSort():
    c1=int(input("Student Count:"))
    print(f"Enter the {c1} student first year percentage (separating spaces) ")
    mark=list(map(float,input().split()))
    n=len(mark)
    
    for i in range(n-1):
        for j in range(i+1,n):
            if mark[i]>mark[j]:
                temp=mark[i]
                mark[i]=mark[j]
                mark[j]=temp
    print("Sorted Array is :")
    for i in range(n):
        print(mark[i])
    print("Top 5 Score are : ")
    print(mark[-5:n])
    
BubbleSort()
SelectionSort()
