

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    
    def insertionSort(self, head):
        sortLL = None
        
        current_node = head
        while current_node != None: 
            next_node = current_node.next
            sortLL = self.insertNodeinLL(sortLL,current_node)
            current_node = next_node
        return sortLL
        
    def insertNodeinLL(self,head_reference,new_node):
        current = None
        if head_reference == None or head_reference.data >= new_node.data:
            #Echange dans la linkedList : exemple 30 et 23
            #On assigne le next à 30
            new_node.next = head_reference
            #Le noeud avec la data 23 de viens la nouvel head reference
            head_reference = new_node
        else:
            #Exemplle : new_node = 28
            #current = 23
            current = head_reference
            #Parcourt la liste du départ
            while(current.next != None and current.next.data <= new_node.data):
                current = current.next
            #Echanger les deux position
            new_node.next = current.next
            current.next = new_node
            
        return head_reference
