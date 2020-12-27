import requests
# https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html#id2
r = requests.get('https://api.github.com/events')
# r = requests.get('https://web422blog.herokuapp.com/login')
print(f'\n{r.url=}')
print(f'\n{r.status_code=}')
# 200
print(f'\n{r.headers["content-type"]=}')
# 'application/json; charset=utf8'
print(f'\n{r.headers=}')
print(f'\n{r.encoding=}')
print(f'\n{r.cookies=}')
# 'utf-8'
# print(f'\n{r.text=}')
# u'{"type":"User"...'
print(f'\n{r.json()=}')
# {u'private_gists': 419, u'total_private_repos': 77, ...}
print(f'\n{r.content=}')

queryParams = {
    'page': '1',
    'perPage': '10',
    'category': '',
    'tag': '',
}
r = requests.get('https://web422blogapi.herokuapp.com/api/posts', params=queryParams)
print(f'\n{r.status_code=}')
print(f'\n{r.json()=}')

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(f'\n{r.status_code=}')
print(f'\n{r.raw=}')
print(f'\n{r.raw.read(10)=}')
print(f'\n{r.content=}')
print(f'\n{r.text=}')
print(f'\n{r.json()=}')
r = requests.put('http://httpbin.org/put', data={'key': 'value'})
r = requests.delete('http://httpbin.org/delete')
print(f'\n{r.status_code=}')
r = requests.head('http://httpbin.org/get')
print(f'\n{r.status_code=}')
r = requests.options('http://httpbin.org/get')
print(f'\n{r.status_code=}')

r = requests.get('https://api.github.com/events', stream=True)
print(f'\n{r.raw=}') #确保在初始请求中设置了 stream=True
# <requests.packages.urllib3.response.HTTPResponse object at 0x101194810>
r.raw.read(10)
print(f'\n{r.raw.read(10)=}')
# '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
