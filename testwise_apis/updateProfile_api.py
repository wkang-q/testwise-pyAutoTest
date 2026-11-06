import requests
import datas
import random
# from 模块 import 函数：后面直接 login_api(...)，不用再写 login_api.login_api(...)
from login_api import login_api
from getProfile_api import getProfile_api


def updateProfile_api(account, password):
    try:
        # 与 getProfile 同一路径；用 PATCH 做局部更新
        updateProfile_url = datas.url_inter + 'profile'
        # 只要 token；*_ 吃掉后面的 json、状态码
        access_token, *_ = login_api(account, password)
        # 4 位随机数；拼成 11 位手机号 199xxxxYYYY，避免每次测同一数据
        n4 = random.randint(1000, 9999)
        resp = requests.patch(
            url=updateProfile_url,
            # Bearer 后面必须有空格
            headers={'Authorization': 'Bearer ' + access_token},
            json={'phone': f'199{n4}{n4}', 'nickname': f'昵称{n4}'},
        )
        # 成功：返回响应体 + 状态码
        return resp.json(), resp.status_code
    except Exception as e:
        # 失败：错误信息 + 自约定状态码
        return str(e), 500


# 直接运行本文件时才执行；被 import 时不会跑
if __name__ == "__main__":
    account = "wkangsss"
    password = "your-password"
    # 先改资料，再 getProfile 回查是否生效
    print(updateProfile_api(account, password))
    print(getProfile_api(account, password))
