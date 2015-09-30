from django.test import TestCase
from django_bitbucket_hook.models import Hook


class DjangoBitbucketHookTestCase(TestCase):
    def setUp(self):
        Hook.objects.create(
            name='test',
            user='test',
            repo='test',
            path='tests/test.sh',
            branch='test'
        )

    def test_plain_post(self):
        """
        POST without payload or name is invalid
        """
        response = self.client.post('/')
        self.assertEqual(response.status_code, 200)
