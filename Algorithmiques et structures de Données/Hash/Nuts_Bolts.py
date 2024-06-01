class Solution:

    # Fonction pour partitionner un tableau basé sur un pivot
    def partition(self, tab, begin, end, pivot):
        i = begin
        j = begin 
        while j < end:
            # Si l'élément actuel est inférieur au pivot, l'échanger avec l'élément à l'index 'i'
            if tab[j] < pivot: 
                tab[i], tab[j] = tab[j], tab[i] 
                i += 1
            # Si l'élément actuel est égal au pivot, l'échanger avec l'élément à la fin
            elif tab[j] == pivot: 
                tab[j], tab[end] = tab[end], tab[j] 
                j -= 1  # Décrémenter 'j' pour re-vérifier cet élément
            j += 1
        # Placer le pivot à sa position correcte
        tab[i], tab[end] = tab[end], tab[i]
        return i  # Retourner la position du pivot

    # Fonction pour faire correspondre les paires d'écrous et de boulons
    def matchPairs(self, nuts, bolts, n):
        # Fonction interne pour trier et partitionner récursivement les écrous et les boulons
        def matchPairs2(nuts, bolts, begin, end):
            if begin < end:
                # Partitionner les écrous en utilisant le dernier boulon comme pivot
                piv = self.partition(nuts, begin, end, bolts[end])
                # Partitionner les boulons en utilisant l'écrou trouvé comme pivot
                self.partition(bolts, begin, end, nuts[piv])
                # Trier récursivement les sous-tableaux gauche et droit
                matchPairs2(nuts, bolts, begin, piv - 1) 
                matchPairs2(nuts, bolts, piv + 1, end)

        # Appel initial pour trier les écrous et les boulons
        matchPairs2(nuts, bolts, 0, n - 1)
