

def SelSort(arr):

    n = len(arr)

    for i in range(n-1):
        # min = arr[i]
        # print("i---",i)
        min = i
        for j in range(i+1,n):
            # print("j--",j)
            # print("here - ",arr[i],arr[j])
            if arr[j]<arr[min]:
                min = j
                # print("--->",j)
                # arr[j],arr[i] = arr[i],arr[j]
        arr[min],arr[i] = arr[i],arr[min]
        print(arr)
        # if i == 1:

        #     break

    return arr



arr = [31,20,31,15,6]

SelSort(arr)
# ques - interview - asks are you cheating - home banter - violent case - rw