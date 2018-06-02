import config
import requests as rs

_TWITTER_API_ROOT = 'https://api.twitter.com/'
_TWITTER_API_VERSION = '1.1'

def _poll_feed(user_ids):
	rs.get(_TWITTER_API_ROOT)


def most_recent_post(user_id):
	return config.state.twitter.most_recent_posts[user_id]

def watched_users():
	return ['177366676'] # Path of exile account


def new_tweets_for_user(user_id):
	# Function sketch:
	# - Grab timeline
	# - take while tweet_id != config.state.twitter.most_recent_tweet[user_id]
	# - update most recent tweet to the newest one in this poll
	# - return all the new ones
	pass

def _refresh_bearer_token():
	user_key = config.bot.twitter.user_key
	user_secret = config.bot.twitter.user_secret
	config.state.twitter.bearer_token = _get_bearer_token(user_key, user_secret)

def post_to_discord(tweet_dict):
	screen_name = tweet_dict['user']['screen_name']
	tweet_id = tweet_dict['id_str']
	message = "https://twitter.com/" + screen_name + "/" + tweet_id

def _get_bearer_token(user_key, user_secret):
	res = rs.post(
			_TWITTER_API_ROOT + 'oauth2/token',
			auth=(user_key, user_secret),
			params={'grant_type': 'client_credentials'},
	)

	# Token might get invalidated by twitter, need error handling here in case
	# that is the case. They say they currently do not automatically invalidate
	# these tokens, so other things first.
	if res.status_code == 200:
		return res.json()['access_token']
	elif res.status_code == 403:
		print('Bad twitter credentials, no bearer token can be fetched')
