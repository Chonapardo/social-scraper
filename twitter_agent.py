import requests
from lxml import html
from bs4 import BeautifulSoup
from pprint import pprint
from Post import Post

def login(username = '@Chona_Pardo', password = 'chonacapo'):

	session_requests = requests.session()

	login_url = "https://twitter.com/login"
	result = session_requests.get(login_url)

	CSRF_TOKEN = result.text.split('" name="authenticity_token">')[0].split('"')[-1]

	payload = {
		"session[username_or_email]": username, 
		"session[password]": password, 
		"authenticity_token": CSRF_TOKEN,
		"scribe_log": None,
		"redirect_after_login": None,
		"remember_me": 1
	}

	sessions_url = 'https://twitter.com/sessions'

	result = session_requests.post(
		sessions_url, 
		data = payload, 
		headers = dict(referer=login_url)
	)

	url = 'https://twitter.com/'
	result = session_requests.get(
		url, 
		headers = dict(referer = url)
	)

	if result.ok:
		return result.text
	else:
		return False
		#raise Exception(result.status_code)

def parseTweets(html):

	soup = BeautifulSoup(html, "html.parser")

	twits =soup.find_all("div", class_='tweet')

	classes = ["tweet", "js-stream-tweet", "js-actionable-tweet", "js-profile-popup-actionable", "dismissible-content", "original-tweet", "js-original-tweet", "tweet-has-context", "has-cards", "has-content"]

	cards = soup.findAll('div', {'class': classes})

	return cards

def createPosts(htmlTweets):

	posts = []

	for tweet in htmlTweets:

		try:

			url = 'https://www.twitter.com'

			classes = ['TweetTextSize', 'js-tweet-text', 'tweet-text']

			text = tweet.find('p', {'class': classes})
			
			classes = ['account-group', 'js-account-group', 'js-action-profile', 'js-user-profile-link', 'js-nav']

			aTags = tweet.findAll('a')

			texts = tweet.findAll(['a', 'p'])

			text = ' '.join([t.text for t in texts if 'Hace' not in t.text and 'pic' not in t.text][1:])

			image = [t.text for t in texts if 'pic' in t.text]

			author = tweet.find('a', class_='account-group').text

			url += [a['href'] for a in aTags if 'status'in a['href']][0]

			posts.append(Post(tweet, 'Twitter', text=text, image=image, url=url, author=author))

		except:
			pass

	return posts


		
