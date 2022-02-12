import snscrape.modules.twitter as sntwitter
import pandas as pd
from bs4 import BeautifulSoup

def scrape_tweets(keyword,start,until,no_of_tweets):
    # Creating list to append tweet data to
    tweets_list = []

    hashtag = f"{keyword} since:{start} until:{until}"
    
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(hashtag).get_items()):
        if i > (no_of_tweets-1):
            break
            
        data = tweet.source
        soup = BeautifulSoup(data)
        tweets_list.append({
                "tweet_id":      tweet.id, 
                "tweet_url":     tweet.url,
                "tweet_content": tweet.content.replace("\n",''), 
                "tweeted_on":    tweet.date.strftime('%A, %d %b %Y %I:%M %S %p'),
                "username":    tweet.user.username, 
                "verified":         tweet.user.verified,
                "follower_count":  tweet.user.followersCount,
                "following_count": tweet.user.friendsCount,
                "status_count":     tweet.user.statusesCount,
                "website":      tweet.user.linkUrl,
                "reply_count":     tweet.replyCount,
                "retweet_count":   tweet.retweetCount,
                "tweet_likes":      tweet.likeCount,
                "tweet_quote_count":tweet.quoteCount,
                "tweet_lang":       tweet.lang,
                "tweet_source":     soup.find('a').contents[0],
            })
    return tweets_list

