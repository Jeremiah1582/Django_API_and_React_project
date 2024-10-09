
from django.test import TestCase
from core.user.models import User
from core.post.models import Post
from core.comment.models import Comment




class Test_Comment_Model(TestCase):
    def setUp(self):
        self.user = User.objects.create(**{ 
                'first_name':'test14457591011 ',
                'last_name':'testing14457591011',
                'email':'123@1234457591011.com',
                'username':'tester12124457591011',
                'password':'test_password12311'
                })
        self.post = Post.objects.create(author=self.user, body="This is a test post")
        self.comment = Comment.objects.create(author=self.user, post=self.post, body="This is a test comment")

    def test_create_comment(self):
        self.assertIsInstance(self.comment, Comment)
        self.assertIsInstance(self.comment.author, User)
        self.assertIsInstance(self.comment.post, Post)
        self.assertEqual(self.comment.body, "This is a test comment")
        
    def tearDown(self):
        self.user.delete()
        self.post.delete()
        self.comment.delete()   
        



# # Create your tests here.
# # Comment requires User and Post Models 

# test_user= User.objects.create(**{ 
#                 'first_name':'test144575910 ',
#                 'last_name':'testing144575910',
#                 'email':'123@12344575910.com',
#                 'username':'tester121244575910',
#                 'password':'test_password123'
#                 })

# test_post= Post.objects.create(**{
#     'body':"This is a test post"
#     })



# # utility function to create comment
# def createPost(author, body):
#     return Post.objects.create(author=author, body=body)

# def createUser(user_data):
#     return User.objects.create_user(**user_data)

# def createComment():
    
#     test_Comment= {
#     'author': createUser(test_user),  # This should be a User instance, not a dictionary
#     'post': createPost(test_user, body= 'this is a post'),    # This should be a Post instance, not a dictionary
#     'body': "This is a test comment"
#     }
#     comment = Comment.objects.create(**test_Comment)
    
#     return comment




# class Test_Comment_Model(TestCase):
    
#     def test_create_comment(self):
#         self.assertIsInstance(createComment(test_user, test_post, content="This is a test comment fam"), Comment)
 
      
#         # self.assertEqual(test_Comment.body, "This is a test comment")
