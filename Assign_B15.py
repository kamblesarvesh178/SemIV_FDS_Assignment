def InsertionSort():
    c1=int(input("Student Count : "))
    print(f"Enter the {c1} students first year percentage by spacing ")
    mark=list(map(float,input().split()))
    n=len(mark)
    
    for i in range(1,n):
        key=mark[i]
        j=i-1
        while j>=0 and key< mark[j]:
            mark[j+1]=mark[j]
            j= j-1
        mark[j+1]=key

    print("Sorted Array is :")
    for i in range(n):
        print(mark[i])
    print("Top 5 Score are : ")
    print(mark[-5:n])



def ShellSort():
    c1=input("Student Count : ")
    print(f"Enter the {c1} students first year percentage by spacing ")
    mark=list(map(float,input().split()))
    n=int(len(mark))
    gap=n//2

    while gap>0:
        for i in range(gap,n):
        # add a[i] to the elements that have been gap sorted
        # save a[i] in temp and make a hole at position i
            key=mark[i]
            j=i
            while j>=gap and mark[j-gap]>key:
                mark[j]=mark[j-gap]
                j= j - gap
            mark[j]=key
        gap=gap//2

    print("Sorted Array is :")
    for i in range(n):
        print(mark[i])
    print("Top 5 Score are : ")
    print(mark[-5:n])    





#InsertionSort()
ShellSort()