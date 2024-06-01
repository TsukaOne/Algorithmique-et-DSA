from typing import List
from queue import Queue

class Solution:
    def rearrangeQueue(self, N: int, q: List[int]) -> List[int]:
        # Initialiser la queue
        queue = Queue()
        # Remplir la queue avec les éléments de la liste q
        for item in q:
            queue.put(item)
        
        # Créer deux listes pour stocker les moitiés
        first_half = []
        second_half = []
        # Extraire la première moitié de la queue
        for _ in range(N // 2):
            first_half.append(queue.get())
        # Extraire la deuxième moitié de la queue
        for _ in range(N // 2):
            second_half.append(queue.get())
        
        # Intercaler les éléments des deux moitiés
        result = []
        for i in range(N // 2):
            result.append(first_half[i])
            result.append(second_half[i])
        
        return result