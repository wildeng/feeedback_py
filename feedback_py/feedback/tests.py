# myapp/tests.py
from django.contrib.auth.models import User
from django.test import TestCase


class FeedbackTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )

    def test_feedback_creation(self):
        feedback_text = "This is a test feedback"
        response = self.client.post(
            "/feedback/", {"feedback_text": feedback_text}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Feedback.objects.filter(
                user=self.user, feedback_text=feedback_text
            ).exists()
        )

# Create your tests here.
