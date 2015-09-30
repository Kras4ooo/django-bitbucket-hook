import os
import json
from django.test import TestCase
from django_bitbucket_hook.models import Hook


class DjangoBitbucketHookTestCase(TestCase):
    def setUp(self):
        Hook.objects.create(
            name='test-name',
            user='user',
            repo='repo',
            path='date',  # Put absolute path to executable file. Example: /home/test/test.sh..
            branch='master'
        )

        self.bitbucket_payload = """
            {
              "ref": "refs/heads/master",
                  "repository": {
                    "id": "000000000",
                    "name": "repo",
                    "full_name": "user/repo",
                    "owner": {
                      "name": "user",
                      "email": "user@email"
                    }
                  }
            }
        """

    def tearDown(self):
        if os.path.isfile("test.txt"):
            os.remove('test.txt')

    def test_broke__main_url(self):
        response = self.client.post('/')
        content = json.loads(response.content.decode('utf-8'))
        self.assertFalse(content['success'])
        self.assertEqual(content['message'], 'No JSON data or URL argument : cannot identify hook')
        self.assertEqual(response.status_code, 200)

    def test_broke_repo_url(self):
        response = self.client.post('/test')
        content = json.loads(response.content.decode('utf-8'))
        self.assertFalse(content['success'])
        self.assertEqual(content['message'], 'Not exist Hook')
        self.assertEqual(response.status_code, 200)

    def test_broke_repo_branch_url(self):
        response = self.client.post('/test/test')
        content = json.loads(response.content.decode('utf-8'))
        self.assertFalse(content['success'])
        self.assertEqual(content['message'], 'Not exist branch')
        self.assertEqual(response.status_code, 200)

    def test_main_url(self):
        data = {"payload": self.bitbucket_payload}
        response = self.client.post('/', data)
        content = json.loads(response.content.decode('utf-8'))
        self.assertIsInstance(content, dict)
        self.assertEqual(response.status_code, 200)

    def test_repo_url(self):
        data = {"payload": self.bitbucket_payload}
        response = self.client.post('/test-name', data)
        content = json.loads(response.content.decode('utf-8'))
        self.assertIsInstance(content, dict)
        self.assertTrue(content['success'])
        self.assertEqual(response.status_code, 200)

    def test_repo_broke_branch_url(self):
        data = {"payload": self.bitbucket_payload}
        response = self.client.post('/test-name/not-right', data)
        content = json.loads(response.content.decode('utf-8'))
        self.assertIsInstance(content, dict)
        self.assertFalse(content['success'])
        self.assertEqual(content['message'], 'This is not the right branch')
        self.assertEqual(response.status_code, 200)

    def test_repo_branch_url(self):
        data = {"payload": self.bitbucket_payload}
        response = self.client.post('/test-name/master', data)
        content = json.loads(response.content.decode('utf-8'))
        self.assertIsInstance(content, dict)
        self.assertTrue(content['success'])
        self.assertEqual(response.status_code, 200)
