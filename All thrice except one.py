def allthrice(arr):
    ones=0
    twos=0
    for i in range(0,len(arr)):
        twos=twos^(ones&arr[i])
        ones=ones^arr[i]
        rbsm=~(ones&twos)
        ones=ones&rbsm
        twos=twos&rbsm
    return ones
arr=[3,3,3,2,1,1]
print(allthrice(arr))
