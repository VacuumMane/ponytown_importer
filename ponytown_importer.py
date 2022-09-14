import requests

# 皮肤信息
## 前两项填入自己的id和name，后一项选择自己想要的pony代码
skin = {'accountId': "", 'accountName': "", 'pony':""}

# 请求标头
headers = {
    'api-bid': 'c9i6g9mv5spu12fl_a_v',
    'api-version': 'Fa2Tp76raI',
    ## 填入从"save"获取的cookie
    'cookie': '_ga=; _gid=; remember_me=; connect.sid=',
    'referer': 'https://pony.town/character',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
}

# 向服务器发送URL请求
save = "https://pony.town/api/pony/save"
r = requests.post(save, data = skin, headers = headers)
## 判断是否成功
if r.status_code == 200:
    print('successfully imported')
else:
    print('failed to import')
