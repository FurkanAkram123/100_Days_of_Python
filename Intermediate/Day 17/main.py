class Instagram_User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers_count = 0

    def display_info(self):
        print ('Creating new user...')
        print(f"User ID: {self.user_id}, Username: {self.username}, Followers: {self.followers_count}")

    def follow(self):
        self.followers_count += 1
        print(f"{self.username} has gained a follower! Total followers: {self.followers_count}")    

    def unfollow(self):
        if self.followers_count > 0:
            self.followers_count -= 1
            print(f"{self.username} has lost a follower! Total followers: {self.followers_count}")
        else:
            print(f"{self.username} has no followers to lose.")

    def get_followers_count(self):
        return self.followers_count


#example usage:

Instagram_user1 = Instagram_User(1, "furkan_the_kaptaan")
Instagram_user1.display_info()
Instagram_user1.follow()
Instagram_user1.display_info()

