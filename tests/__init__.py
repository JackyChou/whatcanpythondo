# coding: utf-8

import unittest

from app import create_app


class BaseTestCase(unittest.TestCase):
    """
    base test case
    """

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.content_type_json = 'application/json'

    def tearDown(self):
        self.app_context.pop()
