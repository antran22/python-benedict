# -*- coding: utf-8 -*-

from benedict import benedict

import json
import unittest


class github_issue_0034_test_case(unittest.TestCase):

    """
    https://github.com/fabiocaccamo/python-benedict/issues/34

    To run this specific test:
    - For each method comment @unittest.skip decorator
    - Run python -m unittest tests.github.test_issue_0034
    """

    def test_json_dumps(self):
        b = benedict({
            'a': 1,
            'b': {
                'c': {
                    'd': 2,
                },
            },
        })
        dumped = json.dumps(b, sort_keys=True)
        self.assertEqual(dumped, '{"a": 1, "b": {"c": {"d": 2}}}')

    def test_json_dumps_after_pointer_update(self):
        d = {
            'a': 1,
            'b': {
                'c': {
                    'd': 2,
                },
            },
        }
        b = benedict(d)
        d['a'] = 2
        d['b']['c']['d'] = 3
        self.assertEqual(d, b.dict())
        self.assertEqual(b, b.dict())
        dumped = json.dumps(b, sort_keys=True)
        self.assertEqual(dumped, '{"a": 2, "b": {"c": {"d": 3}}}')
