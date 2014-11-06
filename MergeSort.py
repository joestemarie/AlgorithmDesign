def split(list):
    half = len(list)//2
    return list[:half], list[half:]

array = [5,4,1,8,7,2,6,3]
A, B = split(array)
n=len(array)

A = sorted(A)
B = sorted(B)

print(A)
print(B)

array_sorted=[]

i=0
j=0

for k in range(0,n):
    if i>=len(A):
        array_sorted.append(B[j])
        j+=1
        k+=1
        print(k)
        print(array_sorted)
    if j>=len(B):
        array_sorted.append(A[i])
        i+=1
        k+=1
        print(k)
        print(array_sorted)
    elif A[i] < B[j]:
        array_sorted.append(A[i])
        i+=1
        k+=1
        print(k)
        print(array_sorted)
    elif A[i] > B[j]:
        array_sorted.append(B[j])
        j+=1
        k+=1
        print(k)
        print(array_sorted)
    else:
        print("It's done")
        print(array_sorted)
