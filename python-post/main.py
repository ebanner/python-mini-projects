import requests
import json


if __name__ == '__main__':
    response = requests.post('http://httpbin.org/post')

    # Request
    request = response.request

    print('REQUEST')
    print()
    print(request.method)
    print(request.url)
    print(request.body)
    print(json.dumps(dict(request.headers), indent=2))
    print()

    # Response
    import json

    print('RESPONSE')
    print()
    print(json.dumps(dict(response.headers), indent=2))
    print()
    print(response.status_code)
