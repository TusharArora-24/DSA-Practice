


def fun(arr,n):

    if n==0:
        return
    print(arr.pop(0),end = " ")
    fun(arr,n-1)

fun(arr=[1,2,3,4,5],n=5)
