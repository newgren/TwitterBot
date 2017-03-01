#!flask/bin/python
from flask import Flask, request
import base64
import urllib
import urllib2
import json

app = Flask(__name__)

consumerKey = ""
consumerSecret = ""
keySecret = consumerKey+":"+consumerSecret
encoded = base64.b64encode(keySecret)
authUrl = 'https://api.twitter.com/oauth2/token'
headers = {'Authorization':'Basic ' + encoded, 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
values = {'grant_type':'client_credentials'}
data = urllib.urlencode(values)
authRequest = urllib2.Request(authUrl,data,headers)
authResponse = urllib2.urlopen(authRequest).read()
authJson = json.loads(authResponse)

token = authJson['access_token']

@app.route('/')
def index():
	return "Main"

@app.route('/hashtag/<hashtag>')
def hashtag(hashtag):
	url = "https://api.twitter.com/1.1/search/tweets.json?q=%23"+hashtag;
	#headers = {'Authorization':'Bearer '+token}
	searchRequest = urllib2.Request(url)
	searchRequest.add_header('Authorization', 'Bearer '+token)
	response = urllib2.urlopen(searchRequest).read()
	jsonObject = json.loads(response)
	try:
		printJob=""
		for status in jsonObject['statuses']:
			printJob = printJob + status["text"].encode('utf-8') + '<br/>'
		return "<h1>#"+str(hashtag)+"</h1></br>"+str(printJob)
	except ValueError as a:
		return "Your request hit the following error:\n"+ str(a)
	return "Bad request"

@app.route('/keyword/<word>')
def keyword(word):
	url = "https://api.twitter.com/1.1/search/tweets.json?q="+word;
	#headers = {'Authorization':'Bearer '+token}
	searchRequest = urllib2.Request(url)
	searchRequest.add_header('Authorization', 'Bearer '+token)
	response = urllib2.urlopen(searchRequest).read()
	jsonObject = json.loads(response)
	try:
		printJob=""
		for status in jsonObject['statuses']:
			printJob = printJob + status["text"].encode('utf-8') + '<br/>'
		return "<h1>"+str(word)+"</h1></br>"+str(printJob)
	except ValueError as a:
		return "Your request hit the following error:<br/>"+ str(a)
	return "Bad request"

@app.route('/geo/<geo>')
def geocode(geo):
	stuff = geo.split(',')
	print stuff[0]
	try:
		float(stuff[0])
		float(stuff[1])
	except ValueError:
		return "Endpoint format:<br/>/geo/long,lat,radius"

	url = "https://api.twitter.com/1.1/search/tweets.json?q=love&geocode="+geo;
	#headers = {'Authorization':'Bearer '+token}
	searchRequest = urllib2.Request(url)
	searchRequest.add_header('Authorization', 'Bearer '+token)
	try:
		response = urllib2.urlopen(searchRequest).read()
	except ValueError as a:
		return "Your request hit the following error:<br/>"+ str(a)
	jsonObject = json.loads(response)
	try:
		printJob=""
		for status in jsonObject['statuses']:
			printJob = printJob + status["text"].encode('utf-8') + '<br/>'
		return str(printJob)
	except ValueError as a:
		return "Your request hit the following error:<br/>"+ str(a)
	return "Bad request"


if __name__ == '__main__':
	app.run(debug=True)
