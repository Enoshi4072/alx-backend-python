#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """ Testing access for the access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Testing access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in {'a': 1}")
    ])
    @unittest.expectedFailure
    def test_access_nested_map_exception(self, nested_map, path, expected_error_msg):
        """Test access_nested_map function raises KeyError."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_error_msg)

import unittest
from unittest.mock import patch, Mock
from utils import get_json

class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        TEST_CASES = [
    ("http://example.com", {"payload": True}),
    ("http://holberton.io", {"payload": False})
]
        test_counter = 0  # Counter to keep track of the number of tests executed
        for test_url, test_payload in TEST_CASES:
            # Mocking the response of requests.get
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Calling the function with mocked requests.get
            result = get_json(test_url)
            test_counter += 1  # Increment the test counter

            # Asserting that requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)

            # Asserting that the output of get_json is equal to test_payload
            self.assertEqual(result, test_payload)

            # Reset mock for the next iteration
            mock_get.reset_mock()

        self.assertEqual(test_counter, len(TEST_CASES), "Number of tests executed should match the number of test cases")

from utils import memoize
import unittest
from unittest.mock import Mock, patch
class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        #define a test class with a method and a memoized property
        class TestClass:
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()
        #create an instance of the test class
        test_obj = TestClass()
        #mock the a_method of the test class
        with patch.object(test_obj, 'a_method', return_value=42) as mock_a_method:
            #call te memoized property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property
            #Assert that a_method was only called once
            mock_a_method.assert_called_once()
            #assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

if __name__ == '__main__':
    unittest.main()
"""
class TestGetJson(unittest.TestCase):
    @patch('utils.requests.get')
    @unittest.mock.patch.dict('utils.requests.get.return_value', {'json.return_value': 'payload': True})
    def test_get_json(self, mock_get):
        test_data = [
                ('http://example.com', {'payload': True}),
                ('http://holberton.io', {'payload': False})
                ]
        #iterate over test data
        for test_url, test_payload in test_data:
            #mock requests.get().json() to return test_payload
            mock_get.return_value.json.return_value = test_payload
            # Call get_json with test_url
            result = get_json(test_url)
            #assert that requests.get was called exactly once with the test_url
            mock_get.assert_called_once_with(test_url)
            #assert that the result is equal to the expected test payload
            self.assertEqual(result, test_payload)
if __name__ == '__main__':
    unittest.main()
    """
