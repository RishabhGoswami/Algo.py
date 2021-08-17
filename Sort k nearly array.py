import heapq

def sort(arr,k):
    l=arr[:k+1]
    heapq.heapify(l)
    start=0
    for i in range(k+1,len(arr)):
        arr[start]=heapq.heappop(l)
        heapq.heappush(l,arr[i])
        start+=1
    while(l):
        arr[start]=heapq.heappop(l)
        start+=1
        
    for i in range(0,len(arr)):
        print(arr[i])
        

    
arr=[2,6,3,12,56,8]
k=3
(sort(arr,k))
