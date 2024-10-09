from django.test import TestCase
from core.post.models import Post
from core.user.models import User


user_test_data={ 
                'first_name':'jjjjjtest',
                'last_name':'bbbtest',
                'email':'123@123brw.com',
                'username':'jjjbbbtest',
                'password':'test_password123'
                }

def createPost(author, body):
    return Post.objects.create(author=author, body=body)

def createUser(user_data):
    return User.objects.create_user(**user_data)


class Test_Post_model(TestCase):
    def setUp(self):
        self.user = createUser(user_test_data)
        self.post = createPost(author=self.user, body="This is a test post")

    def test_create_post(self):
        self.assertIsInstance(self.post, Post)
        self.assertIsInstance(self.post.author, User)
        self.assertEqual(self.post.body, "This is a test post")

    def tearDown(self):
        # Clean up created objects
        User.objects.all().delete()
        Post.objects.all().delete()

# Create your tests here.
