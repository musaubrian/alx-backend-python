#!/usr/bin/env python3
"""unittests for the client package"""

import unittest
from unittest.mock import PropertyMock, patch
import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """defines unittests for GithubOrgClient.org"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json) -> None:
        """
        test that GithubOrgClient.org returns the correct value
        """
        url = f"https://api.github.com/orgs/{org_name}"
        org_client = GithubOrgClient(org_name)
        org_client.org()
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self) -> None:
        """
        unittests the method GithubOrgClient._public_repos_url
        """
        mock_payload = {"repos_url": "https://api.github.com/orgs/google"}

        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_payload
            org_client = GithubOrgClient("google")
            result = org_client._public_repos_url
            self.assertEqual(result, "https://api.github.com/orgs/google")
