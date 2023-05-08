import random
from instagrapi import Client

username = input("Username: ")
password = input("Password: ")
client = Client()
client.login(username, password)

comments_state = False
follow_state = False

hashtag = input("Enter hashtag: #")  # Write hashtag from which you want to like posts.
posts_number = int(input("Number of posts to be liked: "))
option_comments = str(input("Drop comments under posts: Type 'Yes/No': "))

if option_comments == "Yes":
    comments_state = True
    comments = [input("Comments: ")]  # Write comments separated by "," in order to have different comments under post.
    comment_per_num_of_posts = int(input("Drop comment per number of posts: "))

option_follow = str(input("Follow users: Type 'Yes/No'"))

if option_follow == "Yes":
    follow_state = True
    follow_per_num_of_posts = int(input("Follow user per number of posts: "))


def insta_bot():

    for i, media in enumerate(medias):
        client.media_like(media.id)
        print(f"Liked post number {i + 1} of hashtag {hashtag}")

        if comments_state is True:
            if i % comment_per_num_of_posts == 0:
                current_comment = random.choice(comments)
                client.media_comment(media.id, current_comment)
                print(f"Commented: {current_comment}\nUnder post number {i + 1} of hashtag #{hashtag}")

        if follow_state is True:
            if i % follow_per_num_of_posts == 0:
                client.user_follow(media.user.pk)
                print(f"Followed user: {media.user.username}")


medias = client.hashtag_medias_recent(hashtag, posts_number)
insta_bot()
