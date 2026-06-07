class Twitter:

    def __init__(self):
        self.relations = {} # map where key is a follower and val is the list of followees
        self.tweets = {}
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if userId not in self.tweets:
            self.tweets[userId] = set()
        self.tweets[userId].add((self.count, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        if userId in self.tweets:
            for (c,t) in self.tweets[userId]:
                heapq.heappush(heap,(-c,t))
        if userId in self.relations:
            for x in self.relations[userId]:
                if x in self.tweets:
                    for (c,t) in self.tweets[x]:
                        heapq.heappush(heap, (-c,t))
        while heap:
            (c,t) = heapq.heappop(heap)
            res.append(t)
            if len(res) == 10: return res
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.relations:
            self.relations[followerId] = set()
        self.relations[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.relations and followeeId in self.relations[followerId]:
            self.relations[followerId].remove(followeeId)
        
