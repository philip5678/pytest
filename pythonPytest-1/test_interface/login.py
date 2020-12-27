import json

import requests
from requests import request


def login(s, userName='bob', password='123'):
    '''
    :param
    '''

    url = 'https://web422blogapi.herokuapp.com/api'
    loginUrl = f'{url}/login'
    postsUrl = f'{url}/posts'

    userInfo = {
        "_id": 'string',
        "userName": userName,
        "password": password,
        "password2": 'string',
        "fullName": 'string',
        "role": 'string',
    }

    queryParams = {
        'page': '1',
        'perPage': '10',
        'category': '',
        'tag': '',
    }

    # ________________________________________________________________________________
    # res_Login = request('post', loginUrl,
    #                     json=userInfo)  # :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    #
    # # resLogin = request('post', loginUrl, json=json.dumps(userInfo)) # wrong
    # print(res_Login.text)
    # token = res_Login.json()['token']
    # print(f"{token}")
    #
    # print(request('get', postsUrl, params=queryParams))
    # res_GetPosts = request('get', postsUrl, params=queryParams).text
    # print(res_GetPosts)
    #
    # print(request('get', postsUrl, params=queryParams).json())
    # print(json.loads(request('get', postsUrl, params=queryParams).text))

    # ________________________________________________________________________________
    r = s.post(loginUrl, json=userInfo)
    token = r.json()['token']
    print(r.json())

    r = s.get(postsUrl, params=queryParams)
    print(r.json())

    # ________________________________________________________________________________
    # from postman
    # url = "https://web422blog.herokuapp.com/login"
    # payload="{\r\n    \"userName\": \"rob\",\r\n    \"password\": \"123\"\r\n\r\n}"
    # headers = {
    #   'Content-Type': 'application/json'
    # }
    # response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)

    # ________________________________________________________________________________
    # from postman
    # import http.client
    #
    # conn = http.client.HTTPSConnection("web422blog.herokuapp.com")
    # payload = "{\r\n    \"userName\": \"rob\",\r\n    \"password\": \"123\"\r\n\r\n}"
    # headers = {
    #   'Content-Type': 'application/json'
    # }
    # conn.request("POST", "/login", payload, headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))

    # ________________________________________________________________________________
    # url = "https://web422blog.herokuapp.com/admin"
    # payload = "{\r\n    \"userName\": \"rob\",\r\n    \"password\": \"123\"\r\n\r\n}"
    # headers = {
    #     'Content-Type': 'application/json',
    #     'Authorization': f'jwt {token}'
    # }
    # response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)

    return token


if __name__ == '__main__':
    session = requests.session()
    token = login(session)
    print(token)
