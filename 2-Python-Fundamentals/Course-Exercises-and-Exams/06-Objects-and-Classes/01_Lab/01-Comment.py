# 1.	Comment
# Create a class with name "Comment". The __init__ method should accept 3 parameters
# •	username
# •	content
# •	likes (optional, 0 by default)
# Use the exact names for your variables
# Note: there is no input/output for this problem. Test the class yourself and submit only the class

# class Comment:
#     def __init__(self, username, content, likes=0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#
#
# comment = Comment("user1", "I like this book")
#
# print(comment.username)
# print(comment.content)
# print(comment.likes)

class SlidoComment:
    def __init__(self, author_name, content, date="now", likes=0, dislikes=0, author_picture="https://www.partyfest.de/wp-content/uploads/2017/06/minions-carl-lifesize-cardboard-cutout-139cms-product-image.jpg"):
        self.author_name = author_name
        self.content = content
        self.date = date
        self.likes = likes
        self.dislikes = dislikes
        self.author_picture = author_picture

    def present_comment(self):
        return f"{self.author_name}\n Likes: {self.likes} Dislikes: {self.dislikes}\n{self.author_picture}"


comment = SlidoComment("No name", content="Ne sym siguren")

print(comment.present_comment())

for _ in range(100):
    comment.likes += 1

print(comment.present_comment())