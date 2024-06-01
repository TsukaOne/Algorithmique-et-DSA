class Twitter:
    def __init__(self):
        #Dictionnaire (hash map) pour stocker les amis d'un user
        self.friends_of_User = {}
        # Compteur pour assigner un ordre unique à chaque tweet
        self.curr = 0
        # Dictionnaire pour stocker les tweets par utilisateur
        self.tweets_by_user = {}
        # Liste pour stocker tous les tweets dans l'ordre de leur publication
        self.all_tweets = []

    def postTweet(self, userId: int, tweetId: int):
        # Si l'utilisateur n'a pas encore posté de tweets, initialiser sa liste de tweets
        if userId not in self.tweets_by_user:
            self.tweets_by_user[userId] = []
        # Ajouter le nouveau tweet à la liste de tweets de l'utilisateur
        self.tweets_by_user[userId].append((self.curr, tweetId))
        # Ajouter le tweet à la liste globale des tweets
        self.all_tweets.append((self.curr, tweetId, userId))
        # Incrémenter le compteur pour le prochain tweet
        self.curr += 1

    # Fonction pour les 10 tweets les plus récents
    def getNewsFeed(self, userId: int):
        actuality_file = []  # Liste pour stocker les tweets à afficher dans le fil d'actualité
        count = 0  # Compteur pour limiter à 10 tweets

        # Parcourir les tweets dans l'ordre inverse (du plus récent au plus ancien)
        for i in range(len(self.all_tweets) - 1, -1, -1):
            # Si le nombre de tweet ajouter est de 10 on arrête
            if count == 10:
                break  
            tweet_time, tweet_id, tweet_user = self.all_tweets[i]
            # Vérifier si le tweet a été posté par l'utilisateur ou un de ses amis
            if tweet_user == userId or (userId in self.friends_of_User and tweet_user in self.friends_of_User[userId]):
                actuality_file.append(tweet_id)  # Ajouter le tweet au fil d'actualité
                count += 1

        return actuality_file

    def follow(self, followerId: int, followeeId: int):
        # Si le followerId n'a pas encore de liste d'amis, initialiser cette liste
        if followerId not in self.friends_of_User:
            self.friends_of_User[followerId] = set()
        # Ajouter le followeeId à la liste d'amis du followerId
        self.friends_of_User[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        # Vérifier que le followerId suit déjà le followeeId
        if followerId in self.friends_of_User and followeeId in self.friends_of_User[followerId]:
            # Retirer le followeeId de la liste d'amis du followerId
            self.friends_of_User[followerId].remove(followeeId)
