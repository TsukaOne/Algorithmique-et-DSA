
#CREATION DES CLASS POUR LA LINKED LIST

# create Node using class Node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    #Initialisation la linkedList vide
    def __init__(self):
        self.head = None
    
    #Ajouter de nouvelle valeur à la linkedList
    def append(self, new_value):
        
        #On crée une nouvelle paire valeur et next --> Null car pas de valeur suivante
        new_node = Node(new_value)
        
        #Vérification si le premier noeud Head n'existe pas 
        if self.head is None:
            #Si oui alors on crée le head
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
#---------------------------------------------------#     

#FONCTION POUR POUVOIR PRINT LA LINKED LIST
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print(' ')
#---------------------------------------------------# 
#Algorithme pour "Merge Sorted for linked List"
class Solution:
    #Fonction pour trier les parties séparés
    def sortedMerge(self, gauche, droite):
        result = None
        #Si il n'y a pas de partie gauche alors on renvoie la partie droite
        if gauche == None:
            return droite
        #Si il n'y a pas de partie droite alors on renvoie la partie gauche
        if droite == None:
            return gauche
         
        if gauche.data <= droite.data:
            result = gauche
            result.next = self.sortedMerge(gauche.next, droite)
        else:
            result = droite
            result.next = self.sortedMerge(gauche, droite.next)
        return result
    
    def mergeSort(self, head):
        #Si la linked list est vide ou ne comporte qu'un élément
        if head == None or head.next == None:
            return head

        milieu = self.getMiddle(head)
        suivant_milieu = milieu.next

        milieu.next = None

        gauche = self.mergeSort(head)
        droite = self.mergeSort(suivant_milieu)

        sortedlist = self.sortedMerge(gauche, droite)
        return sortedlist
    
    def getMiddle(self, head):
        if (head == None):
            return head
        
        slow = head
        fast = head

        while (fast.next != None and 
            fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
        
if __name__ == '__main__':
    #Initialisation d'une linkedList
    li = LinkedList()
    sol = Solution()
    
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)
   
    #On fait le merge sort 
    li.head = sol.mergeSort(li.head)
    printList(li.head)
