import feedparser

# This will parse the RSS feed
feedparser.parse("https://www.positive.news/rss")
feed = feedparser.parse("https://www.positive.news/rss")

feed['entries']
print(feed)

# This will extract and display information
for entry in feed.entries:
    print("Post Title:", entry.title)
    print("Summary:", entry.summary)
    print("Link:", entry.link)
