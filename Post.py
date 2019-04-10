class Post():

	def __init__(self, html, social, text=None, image=None, video=None, url=None, author=None):
		self.author = author
		self.text = text
		self.image = image
		self.url = url
		self.html = html
		self.social = social

	def __str__(self):
		return '<class {} Post> {}'.format(self.social, self.url)


	def html(self):
		html = '<div class="post">'
		html += '<p class="author">{}</p>'.format(self.author)
		html += '<img class="article_img" src="{}">'.format(image)
		html += '<p class="text">{}</p>'.format(self.text)
		html += '</div>'
		return html