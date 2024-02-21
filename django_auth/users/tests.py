from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.
class CreateUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a user
        user = User.objects.create_user(email='hamba@gmail.com', first_name='Baldwin', last_name='Hamba', password='testpass')
        user.save()

    def test_email_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.email}'
        self.assertEquals(expected_object_name, 'hamba@gmail.com')

    def test_first_name_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.first_name}'
        self.assertEquals(expected_object_name, 'Baldwin')

    def test_last_name_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.last_name}'
        self.assertEquals(expected_object_name, 'Hamba')