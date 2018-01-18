class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._number_of_recent_tweets = 10
        self._followings = collections.defaultdict(set)
        self._messages = collections.defaultdict(list)
        self._time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self._time += 1
        self._messages[userId].append((self._time, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        max_heap = []
        if self._messages[userId]:
            heapq.heappush(max_heap, (-self._messages[userId][-1][0], userId, 0))
        for uid in self._followings[userId]:
            if self._messages[uid]:
                heapq.heappush(max_heap, (-self._messages[uid][-1][0], uid, 0))

        res = []
        while max_heap and len(res) < self._number_of_recent_tweets:
            t, uid, curr = heapq.heappop(max_heap)
            nxt = curr + 1
            if nxt != len(self._messages[uid]):
                heapq.heappush(max_heap, (-self._messages[uid][-(nxt + 1)][0], uid, nxt))
            res.append(self._messages[uid][-(curr + 1)][1])
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self._followings[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self._followings[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
