import requests
import datas
import login_api


def getProfile_api(account, password):
    # 调用地址是 /api/profile（不是服务名 getProfile）；url_inter 已带末尾 /
    getProfile_url = datas.url_inter + 'profile'
    # login_api 是模块，函数写成 login_api.login_api(...)
    # 返回三个值：token、json、状态码；只要第一个用 token, *_ = ...（*_ 可吃掉后面多出来的）
    access_token, *_ = login_api.login_api(account, password)
    try:
        # try 包住 request：登录失败/网络异常时才能进 except
        resp = requests.get(
            url=getProfile_url,
            # Bearer 后面必须有空格，否则会变成 BearereyJ...，服务端当未登录
            headers={'Authorization': 'Bearer ' + access_token},
        )
        return resp.json()
    except Exception as e:
        # 失败：返回错误信息 + 自约定状态码，方便后面判断
        return str(e), 500


# 直接运行本文件时才执行；被别的文件 import 时不会跑
if __name__ == "__main__":
    # 函数已要求 account、password，直接跑时要传参
    print(getProfile_api("wkangs", "your-password"))
