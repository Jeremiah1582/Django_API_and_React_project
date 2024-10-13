from django.test import TestCase
from core.post.models import Post
from core.user.models import User
import time	


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
        
    def test_update_post_successful(self):
        # Update the post body
        new_body = "This is an updated test post"
        self.post.body = new_body
        self.post.save()

        # Retrieve the post from the database to verify the update
        updated_post = Post.objects.get(id=self.post.id)

        # Assert that the post body has been updated
        self.assertEqual(updated_post.body, new_body)
       
        self.assertNotEqual(updated_post.body, "This is a test post")

        # Check that other attributes remain unchanged
        self.assertEqual(updated_post.author, self.user)
        self.assertEqual(updated_post.id, self.post.id)

    def test_post_updated_at_field(self):
        # Get the initial updated_at value
        initial_updated_at = self.post.updated

        # Wait for a short duration to ensure the updated_at field changes
        time.sleep(2)

        # Update the post body
        self.post.body = "This is another test post"
        self.post.save()
        
        # get new updated time: 
        updated_post = self.post.updated
        
        self.assertNotEqual(initial_updated_at, updated_post)
    
    def test_post_delete(self):
        self.post.delete()
        self.assertEqual(Post.objects.count(), 0)
    
    def tearDown(self):
        # Clean up created objects
        User.objects.all().delete()
        Post.objects.all().delete()

# Create your tests here.
