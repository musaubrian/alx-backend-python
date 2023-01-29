#!/usr/bin/env python3
"""Module contains test cases for the utils file"""

from typing import Any, Mapping, Sequence
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """defines test cases for utils"""

    @parametized.expand(
        [
            ({"a": 1}, ("a"), 1),
            ({"a": {"b": 2}}, ("a"), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
