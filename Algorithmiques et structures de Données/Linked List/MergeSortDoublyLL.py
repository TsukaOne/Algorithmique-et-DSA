class Solution():
    
    #Merge appliqué en crescendo decrescendo
    def merge(self, first, second):
        #Vérification pour mettre fin à la récursion
        if first is None:
            return second
        if second is None:
            return first
        
        #IF et ELSE compare simplement les donnée entre elles pour les triés selon < ou >
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
            
    #Méthode Fast Slow pour le milieu de la linked list classique 
    def splitLL(self,head_ref):
        fast = slow = head_ref
        while(True):
            if fast.next is None or fast.next.next is None: 
                break
            fast = fast.next.next
            slow = slow.next
        tampon = slow.next
        slow.next = None
        return tampon
    
    #Même chose que pour Simply linked List 
    def sortDoubly(self,head):
        #Si la liste est vide ou qu'elle à qu'un seul élément on la retourne simplement
        if head is None: 
            return head
        if head.next is None: 
            return head
        
        start_part2 = self.splitLL(head)
        head = self.sortDoubly(head)
        start_part2 = self.sortDoubly(start_part2)
        
        return self.merge(head,start_part2)
