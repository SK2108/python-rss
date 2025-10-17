"""Module providing a function to parse a feed"""
import feedparser

# This will parse the RSS feed
feed = feedparser.parse("https://www.positive.news/rss")


def parse_feed():
    """Function to parse the feed"""
# This will extract and display information
    for entry in feed.entries:
        print("Post title:", entry.title)
        print("Author:", entry.author)
        print("Date:", entry.published)
        print("Summary:", entry.summary)
        print("Link:", entry.link)


if __name__ == "__main__":
    parse_feed()  # call the function on line 8
