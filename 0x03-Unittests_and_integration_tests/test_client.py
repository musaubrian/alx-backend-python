#!/usr/bin/env python3
"""unittests for the client package"""

from typing import Dict
import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json) -> None:
        """
        unit-tests for GithubOrgClient.public_repos
        """
        mock_payload = [{"pay": "load1"}, {"pay2": "load2"}]
        mock_get_json.return_value = mock_payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://someurl.com"
            org_client = GithubOrgClient("some_org")
            result = org_client.public_repos()

            self.assertEqual(result, mock_payload)
            mock_public_repos_url.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(
        self, repo: Dict[str, Dict], license_key: str, expected: bool
    ) -> None:
        """
        unit-test for GithubOrgClient.has_license
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
