 
class Solution:
    def tour(self, lis, n):
        if n==1:
            return 0
        
        #On initialise les deux pointeurs comme une circular queue
        front,rear = 0,1
        petrol = lis[front][0] - lis[front][1]
        while(rear != front or petrol < 0):
            while(petrol < 0 and front != rear):
                petrol -= (lis[front][0] - lis[front][1])
                front=(front+1)%n
                if front==0:
                    return -1
            petrol+=(lis[rear][0] - lis[rear][1])
            rear=(rear+1)%n
            
        return front
