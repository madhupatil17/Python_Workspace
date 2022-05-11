class NewClasss:
    def __init__(self):
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = NewClasss()
user2 = NewClasss()

user1.follow(user2)
print(user1.following, user1.followers)
print(user2.following, user2.followers)

