# -*- coding: utf-8 -*-
DEPLOYMENT_MODE = 'dev'
COMPRESS_REVISION_NUMBER = '1.0'

BLOG_PLATFORM = 'wordpress'  # Wordpress or tumblr

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = '[ENTER TUMBLR BLOG URL] ex. rigoneri.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = '[ENTER TUMBLR API KEY HERE, SEE TUMBLR SETUP INSTRUCTIONS]'

#Blog Integration: Wordpress
WORDPRESS_BLOG_URL = 'iraindolf.wordpress.com'
WORDPRESS_API_URL = 'https://public-api.wordpress.com/rest/v1/sites/{0}'.format(WORDPRESS_BLOG_URL)

#RSS Feed Integration: (by default use Tumblr rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = '6Af3UupbNTB1Jtz6RL0tg'
TWITTER_CONSUMER_SECRET = 'sHBoHr9SjRgp1wku65zhcXgkONhQjLVOLAuN5NriV0'
TWITTER_USER_KEY = '496212686-KMy0mSAYrxPN5nVoXBeR9nerMygUXdjq7v3j8g4x'
TWITTER_USER_SECRET = 'dCJv2tgWXvxmR0O6KffEo3UXcTbtv52fXVIGTyYiUPMvD'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '528e3c5a4dfbe2599f75aa71a98c5beca3adf023'

GITHUB_OAUTH_ENABLED = False
GITHUB_CLIENT_ID = '8807202044db98e6eb66'
GITHUB_CLIENT_SECRET = '15debf8caab1e2b3f79222312834df5972771b34'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Stack Overflow Integration
STACKOVERFLOW_INTEGRATION_ENABLED = False
STACKOVERFLOW_API_URL = 'http://api.stackoverflow.com/1.1/'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '281543182.b45f170.5d9d686b6397416087924dbb4b12a53f'
INSTAGRAM_USER_ID = '281543182'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = 'b45f170805e64701925a70a9362edebf'
INSTAGRAM_CLIENT_SECRET = 'ed9844f9b9d44de89e720fd0a228ec79'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = False
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = '[ENTER FOURSQUARE ACCESS TOKEN HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = False
FOURSQUARE_CLIENT_ID = '[ENTER FOURSQUARE CLIENT_ID HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_CLIENT_SECRET = '[ENTER FOURSQUARE CLIENT_SECRET HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#ShareThis
SHARETHIS_PUBLISHER_KEY = ''


#Woopra
WOOPRA_TRACKING_DOMAIN = ''
WOOPRA_TRACKING_IDLE_TIMEOUT = 300000  # 5 minutes
WOOPRA_TRACKING_INCLUDE_QUERY = False


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = ''


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = True
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = '[ENTER LASTFM API_KEY HERE, SEE LASTFM SETUP INSTRUCTIONS]'

#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = True
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = '[ENTER SOUNDCLOUD APPLICATION CLIENT_ID HERE]'
SOUNDCLOUD_SHOW_ARTWORK = False
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = True
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False


#Tent.io Integration
TENT_INTEGRATION_ENABLED = True
TENT_ENTITY_URI = '[ENTER YOUR ENTITY URI HERE] ex. https://yourname.tent.is'
TENT_FEED_URL = '[ENTER A URL TO YOUR FEED] ex. https://yourname.tent.is'


#Steam Integration
STEAM_INTEGRATION_ENABLED = True
STEAM_API_URL = 'http://api.steampowered.com/ISteamUser'
STEAM_API_KEY = '[ENTER YOUR STEAM API KEY HERE, SEE STEAM SETUP INSTRUCTIONS]'


#Flickr Integration
FLICKR_INTEGRATION_ENABLED = True
FLICKR_ID = '[ENTER YOUR FLICKR ID (NOT USERNAME) HERE]' # You do your username->ID lookup here: http://idgettr.com/

#LinkedIn Integration
LINKEDIN_INTEGRATION_ENABLED = True
LINKEDIN_CONSUMER_KEY = '77o9f6p70qaxce'
LINKEDIN_CONSUMER_SECRET = 'xJSTcEelbYTfuRp6'
LINKEDIN_USER_TOKEN = '50cbad4a-a0aa-4260-a4e6-f86884e5549f'
LINKEDIN_USER_SECRET = '468442ee-4f56-40a2-8008-c0dc544486c0'

SITEMAP_ENABLED = False

if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://raindolf.herokuapp.com/'
    ALLOWED_HOSTS = ['*']
    DEBUG = True
else:
    DEBUG = False
    ALLOWED_HOSTS = ['raindolf.herokuapp.com']
    SITE_ROOT_URI = 'http://raindolf.herokuapp.com/'
