import json

import requests
from requests import request


def login(s):
    '''
    :param
    '''
    url = 'https://web422blogapi.herokuapp.com/api'
    loginUrl = f'{url}/login'
    postsUrl = f'{url}/posts'

    userInfo = {
        "_id": 'string',
        "userName": 'bob',
        "password": '123',
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

    # res_Login = request('post', loginUrl,
    #                     json=userInfo)  # :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    #
    # # resLogin = request('post', loginUrl, json=json.dumps(userInfo)) # wrong
    # print(res_Login.text)
    # token = res_Login.json()['token']
    # print(f"{token}")
    #
    print(request('get', postsUrl, params=queryParams))
    # res_GetPosts = request('get', postsUrl, params=queryParams).text
    # print(res_GetPosts)
    #
    # print(request('get', postsUrl, params=queryParams).json())
    # print(json.loads(request('get', postsUrl, params=queryParams).text))

    r = s.post(loginUrl, json=userInfo)
    token = r.json()['token']
    print(r.json())

    r = s.get(postsUrl, params=queryParams)
    print(r.json())


if __name__ == '__main__':
    session = requests.session()
    login(session)
