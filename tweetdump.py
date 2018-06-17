!/usr/bin/env python

import tweepy
import secrets.py

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

if __name__ == '__main__':
    # Get object for user passed in at command line
    user = api.get_user('twitter')
    print('Getting tweets from user ' + user.screen_name)
