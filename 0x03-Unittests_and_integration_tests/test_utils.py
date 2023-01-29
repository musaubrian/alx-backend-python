#!/usr/bin/env python3
"""Module contains test cases for the utils file"""

from sys import exception
from typing import Any, Mapping, Sequence
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """defines test cases for utils"""

    @parametized.expand(
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

    @parametized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence):
        """test if KeyError is raised"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
            exception = cm.exception
            self.assertTrue(str(exception) not in path)
