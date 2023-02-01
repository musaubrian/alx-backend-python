#!/usr/bin/env python3
"""unittests for the client package"""

from unittest.mock import patch
import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """defines unittests for GithubOrgClient.org"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json):
        """
        test that GithubOrgClient.org returns the correct value
        """
        url = f"https://api.github.com/orgs/{org_name}"
        org_client = GithubOrgClient(org_name)
        org_client.org()
        mock_get_json.assert_called_once_with(url)
