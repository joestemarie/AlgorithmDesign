def split(list):
    half = len(list)//2
    return list[:half], list[half:]

def mergesort(array):
    A, B = split(array)
    n=len(array)

    A = sorted(A)
    B = sorted(B)

    array_sorted=[]

    i=0
    j=0

    for k in range(0,n):
        if i>=len(A) and j>=len(B):
            k=n
        if i>=len(A):
            array_sorted.append(B[j])
            j+=1
        elif j>=len(B):
            array_sorted.append(A[i])
            i+=1
        elif A[i] < B[j]:
            array_sorted.append(A[i])
            i+=1
        elif A[i] > B[j]:
            array_sorted.append(B[j])
            j+=1

    return array_sorted

list = [88,99,77,150,143,200]
print(mergesort(list))
