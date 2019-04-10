import requests
from lxml import html
from bs4 import BeautifulSoup
from pprint import pprint
from Post import Post

def login(username = '@Chona_Pardo', password = 'Frambuesal'):

	session_requests = requests.session()

	login_url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
	result = session_requests.get(login_url)

	CSRF_TOKEN = result.text.split('            <script type="text/javascript">window._sharedData = {"config":{"csrf_token":"')[1].split('"')[0]

	payload = {
		"username": username,
		"password": password,
		"queryParams": {"source":"auth_switcher"},
		"optIntoOneTap": False,
		"x-csrftoken": CSRF_TOKEN
	}

	sessions_url = 'https://www.instagram.com/accounts/login/ajax/'

	result = session_requests.post(
		sessions_url, 
		data = payload, 
		headers = dict(referer=login_url)
	)

	url = 'https://www.instagram.com/'
	result = session_requests.get(
		url, 
		headers = dict(referer = url)
	)

	if result.ok:
		return result.text
	else:
		return False
		#raise Exception(result.status_code)

def parseArticles(html):

	soup = BeautifulSoup(html, "html.parser")

	posts = soup.find_all("article")

	

	return posts

#def createPosts(htmlArticles):

def createPosts(htmlArticles):

	posts = []

	for article in htmlArticles:
		try:
			url = 'https://www.instagram.com'
			author = article.findAll('a', class_='FPmhX notranslate nJAzx')[0]['title']
		
			image = article.findAll('img', class_='FFVAD')[0]['src']
		
			try:
				video =  article.findAll('video')[0]['src']
			
			except:
				pass

			text = article.findAll('div', class_='C4VMK')[0].text[len(author):]
		
		except:
			pass

		posts.append(Post(article, 'Instagram', text=text, image=image, author=author))

	return posts
