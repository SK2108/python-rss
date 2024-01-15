import unittest
import feedparser


class TestFeedParsing(unittest.TestCase):
    def test_parsing_feed(self):
        feed = feedparser.parse("https://www.positive.news/rss")
        self.assertFalse(feed.bozo)
        for entry in feed.entries:
            self.assertTrue(entry.title)
            self.assertTrue(entry.summary)
            self.assertTrue(entry.link)


if __name__ == '__main__':
    unittest.main()
