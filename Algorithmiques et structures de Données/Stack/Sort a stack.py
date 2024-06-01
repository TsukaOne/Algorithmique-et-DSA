class Solution:
    #Utilisation d'un array classique
    #Haut du stack = n-1 ; Bas du stack = 0
    
    #Fonction pour récupérer la première valeur(Haut du stack)
    def top_stack(self,stack):
        #stack[n-1]
        return stack[len(stack) -1]
    
    def Sorted(self,s):
        #Initialisation d'un stack temporaire
        stack = []
        #Tant que le stack n'est pas vide = Tant que le pointeur n'est pas à la position -1
        while(len(s)!=0):
            #Récupère la première valeur en haut du stack
            temp = self.top_stack(s)
            #Principe LIFO 
            s.pop()
            while(len(stack)!=0 and (self.top_stack(stack)) > temp):
                s.append(self.top_stack(stack))
                stack.pop()
            #On ajoute la valeur temp à la fin du stack
            stack.append(temp)
        #Pour les besoins de l'exercice nous devons faire que stack = s
        s.extend(stack)

