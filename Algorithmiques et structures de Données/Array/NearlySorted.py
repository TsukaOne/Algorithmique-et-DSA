

a = [3,1,4,2,5]

#-------------Code valide mais mauvaise compléxité temporelle------#
def nearly_sorted_val(a,n,k):
    for i in range(0,n):
        indx = i
        for j in range(indx,min(indx+k+1,n)):
            if(a[indx]>a[j]):
                indx = j
        a[i], a[indx] = a[indx], a[i]
    return a

print(nearly_sorted_val(a,len(a),2))

#-----------------Meilleur comlpléxité temporelle------#
import heapq

def sortNearlySortedArray(a, n, k):
    min_heap = []
    arr = []
    for val in a :
        if len(min_heap) < 2*k: 
            heapq.heappush(min_heap,val)
        else: 
            arr.append(heapq.heappop(min_heap))
            heapq.heappush(min_heap,val)
    while(len(min_heap)):
            arr.append(heapq.heappop(min_heap))
    return arr    
    
print(sortNearlySortedArray(a,len(a),2))