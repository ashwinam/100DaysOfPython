class User:
    def __init__(self, user_id, user_name):
        print("User Created...")
        self.id = user_id
        self.user_name = user_name
        self.follower = 0  # default value
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

# user_1 = User()
# user_1.id = "001"
# user_1.user_name = "ashwin"


user_1 = User("001", "ashwin")
user_2 = User("002", "angela")

user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)

