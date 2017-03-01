# Twitter Bot

This is a project to demonstrate retrieving information from Twitter API using python. I created my own API with flask to allow these results to be easily retrieved.

# API reference  

_Note: This is a sample project._

## Endpoints  

### GET /hashtag/ _input_

Get tweets by hashtag.

**Request Parameters:**  

Parameter| Type | Value
--- | --- | ---
`input`| string | name of hashtag to search for

**Return information:**  

Information| Format | Value
--- | --- | ---
Tweets | HTML | Most recent few tweets containing the hashtag.

### GET /keyword/ _input_

Get tweets by keyword.

**Request Parameters:**  

Parameter| Type | Value
--- | --- | ---
`input`| string | keyword to search for in tweets

**Return information:**  

Information| Format | Value
--- | --- | ---
Tweets | HTML | Most recent few tweets containing the keyword.

### GET /geo/ _input_

Get tweets by location.

**Request Parameters:**  

Parameter| Type | Value
--- | --- | ---
`long`| float | longitude
`lat`| float | latitude
`radius`| float | radius to search within


**Return information:**  

Information| Format | Value
--- | --- | ---
Tweets | HTML | Most recent few tweets within radius
