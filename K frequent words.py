import heapq
arr=[[3,3],[5,-1],[-2,4]]
k=2
# Min heap
heap=[]

for i in range(0,len(arr)):
    distance=((arr[i][0])**2+(arr[i][1])**2)**(0.5)
    if(len(heap)==k):
        if(abs(heap[0][0])>distance):
            heapq.heappop(heap)
            heapq.heappush(heap,(-1*distance,i))
    else:
        heapq.heappush(heap,(-1*distance,i))
        
for i in range(0,len(heap)):
    print(arr[heap[i][1]])
