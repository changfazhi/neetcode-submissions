class Twitter:

    def __init__(self):
        self.tweets = {} # dict of list, list[0] is oldest, list[-1] is newest
        self.following = {} # dict to keep track who is following who
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        if tweetId not in self.tweets[userId]:
            self.tweets[userId].append((self.timestamp, tweetId)) # it should be storing the timestamp then tweetId

        # so the larger the timestamp, the newer it is
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # wanting the most recent, means that i need the top 10 largest time stamp
        # this means i need to get min-heap
        max_heap = []
        # first of all i need to filter if userId follows the followeeId
        lists = []
        res = []
        heapq.heapify(res)
        if userId in self.tweets:
            lists.append(self.tweets[userId])
        if userId in self.following:
            for user in self.following[userId]:
                if user != userId:
                    lists.append(self.tweets[user])
        # second, i need to merge their list and sort it
        for lst_idx, lst in enumerate(lists):
            if lst:
                el_idx = len(lst) - 1
                heapq.heappush(max_heap, (-lst[el_idx][0], lst[el_idx][1], lst_idx, el_idx)) # (timestamp, tweetid, lst_idx, el_idx)
        
        while max_heap and len(res) < 10:
            val, tId, lst_idx, el_idx = heapq.heappop(max_heap)
            res.append(tId)

            next_el_idx = el_idx - 1
            if next_el_idx >= 0:
                next_val = lists[lst_idx][next_el_idx][0]
                next_tId = lists[lst_idx][next_el_idx][1]
                heapq.heappush(max_heap, (-next_val, next_tId, lst_idx, next_el_idx))
        # now res has all the tweet that the user follow
        # third make sure min_heap size is 10
    
        # return the min_heap in reverse as peeking give me smallest which is the oldest
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        if followeeId not in self.following[followerId]:
            self.following[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
        
