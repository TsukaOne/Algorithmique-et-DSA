Arr1 = [1, 23, 12, 9, 30, 2, 50]
Arr2 = [12, 5, 787, 1, 23]
Arr3 = [335, 501, 170 ,725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903 ,154 ,293 ,383 ,422 ,717 ,719 ,896 ,448 ,727 ,772, 539 ,870 ,913 ,668 ,300 ,36 ,895, 704, 812, 323, 334]
import heapq
#---------------------TEST VOIR BON CODE PLUS BAS----------------#
def kLargest1(arr, n, k):
    min_heap = []
    for val in arr:
        if len(min_heap) == k :
            #Vérification si la première valeur du tas est plus petite que la nouvelle valeur
            if min_heap[0] < val:
                #Suprression de la plus petite valeur
                heapq.heappop(min_heap) 
                #Ajout de la première valeur en première position
                heapq.heappush(min_heap,val)
        else:
            #Ajout simple à l'arbre
            heapq.heappush(min_heap,val) 
    #Retourne la min_heap en reverse
    return min_heap[::-1]

print(kLargest1(Arr2,len(Arr2),2))
print(kLargest1(Arr1,len(Arr1),3))
print(kLargest1(Arr3,len(Arr3),30))


#--------------------BON CODE------------------------#
def kLargest2(arr, n, k):
    return_array =[]
    min_heap = []
    for val in arr:
        if len(min_heap) == k :
            #Vérification si la première valeur du tas est plus petite que la nouvelle valeur
            if min_heap[0] < val:
                #Suprression de la plus petite valeur
                heapq.heappop(min_heap) 
                #Ajout de la première valeur en première position
                heapq.heappush(min_heap,val)
        else:
            #Ajout simple à l'arbre
            heapq.heappush(min_heap,val)
    while min_heap:
        val = heapq.heappop(min_heap)
        return_array.append(val)
    #Retourne l'array en reverse
    return return_array[::-1]



print(kLargest2(Arr2,len(Arr2),2))
print(kLargest2(Arr1,len(Arr1),3))
print(kLargest2(Arr3,len(Arr3),30))