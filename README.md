# Twitter Bot

This is a project to demonstrate retrieving information from Twitter API using python. I created my own API with flask to allow these results to be easily retrieved.

# API reference  

_Note: This is a sample project._

## Endpoints  

### GET /hashtag/<input>

Get tweets by hashtag.

**Request Parameters:**  

Parameter| Type | Value
--- | --- | ---
`input`| string | the name of the artist, you could do any funky name you like ;)

**Return information:**  

Information| Format | Value
--- | --- | ---
Wikipedia | string | the related Wikipedia, but sometimes the input is not specific enough to identify a single artist, this will return a empty string
Spotify | string | the trending playlist of the artist, with all the songs concatenated in a string, go figure it out!
twitter | string | all the twitter with related information, every line is a new tweet
