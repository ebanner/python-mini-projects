# python-post

Make a POST request with python

## Running

```
$ python3 main.py
REQUEST

POST
http://httpbin.org/post
None
{
  "User-Agent": "python-requests/2.31.0",
  "Accept-Encoding": "gzip, deflate",
  "Accept": "*/*",
  "Connection": "keep-alive",
  "Content-Length": "0"
}

RESPONSE

{
  "Date": "Mon, 22 Jan 2024 21:58:35 GMT",
  "Content-Type": "application/json",
  "Content-Length": "399",
  "Connection": "keep-alive",
  "Server": "gunicorn/19.9.0",
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Credentials": "true"
}

200
```
