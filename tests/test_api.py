from unittest import TestCase

from helper.config import Config
from helper.helper import Helper
from library.api import Api
from library.session import Session


class TestApi(TestCase):
    ses = Session()
    config = Config()
    helper = Helper()
    api = Api(config=config, helper=helper)
    def test_read_messages(self):
        data = self.api.read_messages(read_type="all")
        self.assertIsNotNone(data)
    def test_read_messages_news(self):
        data = self.api.read_messages(read_type="news")
        self.assertIsNotNone(data)
