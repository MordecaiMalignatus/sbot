import config
import requests as rs

_TWITTER_API_ROOT = 'https://api.twitter.com/'
_TWITTER_API_VERSION = '1.1'

def _refresh_bearer_token():
    user_key = config.bot.twitter.user_key
    user_secret = config.bot.twitter.user_secret
    config.state.twitter.bearer_token = get_bearer_token(user_key, user_secret)

def get_bearer_token(user_key, user_secret):
    res = rs.post(
            _TWITTER_API_ROOT + 'oauth2/token',
            auth=(user_key, user_secret),
            params={'grant_type': 'client_credentials'},
    )

    # Token might get invalidated by twitter, need error handling here in case
    # that is the case.
    if res.status_code == 200:
        return res.json()['access_token']
    elif res.status_code == 403:
        print('Bad twitter credentials, no bearer token can be fetched')
