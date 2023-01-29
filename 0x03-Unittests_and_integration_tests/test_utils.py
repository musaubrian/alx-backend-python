#!/usr/bin/env python3
"""Module contains test cases for the utils file"""

from sys import exception
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence
from utils import access_nested_map, get_json
import unittest
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """defines test cases for utils"""

    @parametarized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parametarized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence):
        """test if KeyError is raised"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
            exception = cm.exception
            self.assertTrue(str(exception) not in path)

    class TestGetJson(unittest.TestCase):
        """test getJson methods"""

        @parametarized.expand(
            [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False}),
            ]
        )
        def test_get_json(self, test_url: str, test_payload: Dict) -> None:
            """test get_json function"""
            attr = {"json.return_value": test_payload}
            with patch("requests.get", return_value=Mock(**attr)) as get_r:
                self.assertEqual(get_json(test_url), test_payload)
                get_r.assert_called_once_with(test_url)
