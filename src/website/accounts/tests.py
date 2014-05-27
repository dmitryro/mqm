import autofixture
from django_webtest import WebTest


class SignupTests(WebTest):
    def test_signup_steps(self):
        reserved_email = autofixture.create_one('accounts.ReservedEmail')
        url = reserved_email.get_signup_url()

        response = self.app.get(url)
        response = response.follow()
        self.assertEqual(response.status_code, 200)

        # First step.
