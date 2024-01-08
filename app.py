from email import feedparser
import feedparser as feed

# This will parse the RSS feed
RssFeed = feedparser.parse("https://somewebsite.com/feed")
RssFeed[""][""]

# This will extract and display information
for entry in RssFeed.entries:
    print("Post Title:", entry.title)
    print("Summary:", entry.summary)
    print("Link:", entry.link)
