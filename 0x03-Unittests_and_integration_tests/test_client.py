#!/usr/bin/env python3
""" Tests for the client """
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ Test case for GithubOrgClient class """
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test org method """
        mock_get_json.return_value = {"name": org_name}
        github_client = GithubOrgClient(org_name)
        org_data = github_client.org
        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(org_data, {"name": org_name})


class TestGithubOrgClient(unittest.TestCase):
    def test_public_repos_url(self):
        known_payload = {'repos_url': 'https://api.github.com/orgs/alxgithub/repos'}
        with patch.object(GithubOrgClient, 'org', PropertyMock(return_value=known_payload)):
            client = GithubOrgClient('alxgithub')
            result = client._public_repos_url
            self.assertEqual(result, known_payload['repos_url'])

import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        # Mocking get_json to return a specific payload
        mock_payload = [{"name": "repo1", "license": {"key": "MIT"}}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload

        # Mocking _public_repos_url property
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=Mock(return_value="https://api.github.com/orgs/org/repos")):
            client = GithubOrgClient("org")

            # Calling the method to be tested
            repos = client.public_repos()

            # Asserting that get_json was called once
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/org/repos")

        # Asserting the result
        self.assertEqual(repos, ["repo1", "repo2"])


import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        # Test case 1: repo with matching license key
        [{"license": {"key": "my_license"}}, "my_license", True],
        # Test case 2: repo with non-matching license key
        [{"license": {"key": "other_license"}}, "my_license", False]
    ])
    def test_has_license(self, repo, license_key, expected):
        returned_value = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(returned_value, expected)


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient

@parameterized_class(("org_payload", "repos_payload"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            Mock(json=lambda: cls.org_payload),
            Mock(json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("org")
        repos = client.public_repos()

        expected_repos = [repo["name"] for repo in self.repos_payload]
        self.assertEqual(repos, expected_repos)

if __name__ == '__main__':
    unittest.main()
