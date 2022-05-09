
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def getcompany(page):
    url = "https://www.butian.net/Reward/pub"
    body = {"s": "1", "p": page, "token": ""}
    headers = {
        'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
    }
    # 移除警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # 模拟浏览器将包体发送请求，获取响应数据
    rp = requests.post(url, headers=headers, data=body, verify=False, timeout=10)
    # 查看响应数据
    data = rp.text
    # print(data)
    # 解析数据，将json字符串转换成python可交互的数据类型字典
    dict_data = json.loads(data)
    # print(dict_data)
    # 拿到company_name数据
    data_com = dict_data['data']['list']
    print(data_com)
    # 遍历列表下的字典
    for data_com in data_com:
        target = data_com['company_name']
        # 保存数据，将获取到到公司名字存放到一个文档中
        with open("butiancompayname4.txt", mode="a") as response:
            target = response.write(target + "\n")

# 遍历page页
count = 1
for count in range(190):
    count += 1
    page = count
    getcompany(page)
