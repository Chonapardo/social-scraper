from bs4 import BeautifulSoup
from Post import Post

def parseArticles(html):

	soup = BeautifulSoup(html, "html.parser")

	
	articles = soup.findAll("div", class_='pinWrapper')


	return articles

def createPosts(htmlArticles):
	posts = []
	
	for article in htmlArticles:

		divs = article.findAll('div', class_='XiG zI7 iyn Hsu')

		img = divs[0].find('img')
		image = img['src']
		if 'image' in image:
			image = None
			break
			
		a = img.parent.parent.parent.parent.parent.parent.parent
		if not a.name == 'a':
			break
		url = 'https://www.pinterest.com' + a['href']

		posts.append(Post(article, 'Pinterest', image=image, url=url))

	return posts

		

