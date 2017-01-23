import webapp2

import random

def getRandomFortune():
	

	fortunes = [
	"I see much code in your future",
	"Eat more fortune cookies",
	"Good job, you learned something. Now Practice it."

	]

	index = random.randint(0, 2)

	return fortunes[index]



class MainHandler(webapp2.RequestHandler):
	def get(self):
		header = "<h1> Fortune Cookie </h1>"

		fortune = "<strong>" + getRandomFortune() +  "</strong>"
		fortune_sentence = "Your fortune is: " + fortune
		fortune_paragraph = "<p>" + fortune_sentence + "</p>"

		lucky_number = "<strong>" + str(random.randint(1, 100)) + "</strong>"
		number_sentence = 'Your lucky number: ' + (lucky_number)
		number_paragraph = "<p>" + number_sentence + "</p>"
		
		cookie_button = "<a href='.'><button>Give me a different fortune!</button></a>"

		content = header + fortune_paragraph + number_paragraph + cookie_button
		self.response.write(content)


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
