# coding: utf-8

"""
设计推特
设计一个简化版的推特(Twitter)，
1）可以让用户实现发送推文，
2）关注/取消关注其他用户，
3）能够看见关注人（包括自己）的最近十条推文。

你的设计需要支持以下的几个功能：
postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
"""
from collections import defaultdict
import time


class UserInfo(object):
    user_id = None
    followers = [] # 谁关注了我
    follows = []  # 我关注了谁


class Twitter(object):
    """
    思路：
    建立两个存储池 一个保存用户关系，一个保存推特信息
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 保存用户推特数据
        self.user_pool = defaultdict(UserInfo)
        self.twitter_pool = defaultdict(list)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        tw_info = (tweetId, int(time.time()))  # 保存一个和时间戳
        self.twitter_pool[userId].append(tw_info)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tws = []
        # 先获取用户自己发的推特
        if self.twitter_pool[userId]:
            tws = self.twitter_pool[userId]
        # 再看关注的人发的推特
        if self.user_pool[userId].user_id:
            follows_user = self.user_pool[userId].follows
            if follows_user:
                for user_id in follows_user:
                    tws.extend(self.twitter_pool[user_id])

        # 按时间排序取前 10 条
        if tws:
            tws = sorted(tws, key=lambda x: x[1])[:10]
        return tws

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """

        # 把 followeeId append到他的 follow 属性中
        if followerId == followeeId:  # 不能自己关注自己
            return
        # 实例化一个user(followerID)
        follower = UserInfo()
        follower.user_id = followerId 
        follower.follows.append(followeeId) 
        self.user_pool[followerId] = follower

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # 在user_pool 中查询这个用户 follower
        if self.user_pool[followerId]:
            # 如果在用户的关注列表中才删除
            if followeeId in self.user_pool[followerId].follows:
                self.user_pool[followerId].follows.remove(followeeId)


        



def test():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print twitter.getNewsFeed(1)
    twitter.follow(1,2)
    twitter.postTweet(2, 6)
    print twitter.getNewsFeed(1)
    twitter.unfollow(1, 2)
    print twitter.getNewsFeed(1)


if __name__ == '__main__':
    test()


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)