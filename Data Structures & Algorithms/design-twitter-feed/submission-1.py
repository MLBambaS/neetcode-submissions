class Twitter:

    def __init__(self):
        self.relations = {} # map where key is a follower and val is the list of followees
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.tweets)-1, -1, -1):
            tweet = self.tweets[i]
            if tweet[1] == userId or (userId in self.relations and tweet[1] in self.relations[userId]):
                res.append(tweet[0])
                if len(res) == 10: return res
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.relations:
            if followeeId not in self.relations[followerId]:
                self.relations[followerId].append(followeeId)
        else:
            self.relations[followerId] = [followeeId]
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.relations[followerId]:
            self.relations[followerId].remove(followeeId)
        
