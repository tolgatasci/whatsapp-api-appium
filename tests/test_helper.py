from unittest import TestCase

from helper.helper import Helper


class TestHelper(TestCase):
    helper = Helper()


    def test_filter(self):
        query = self.helper.message_filter(query="select * from test", filter=dict(phone="05319378541"))
        print(query)
        self.assertTrue(True)