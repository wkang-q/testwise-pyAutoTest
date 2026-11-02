from requests import request
import datas

def login_api():
    # 拼接登录地址：datas 里已有末尾 /，这里只接 'auth/login'
    login_url = datas.url_local + 'auth/login'
    resp = request(
        method='post',  # 登录一般是 POST，参数放 body
        url=login_url,
        # 本接口字段是 account + password（不是 username）
        json={"account": "wkang", "password": "your-password"},
        timeout=20,
    )
    # 一次返回两个值：响应体、状态码；调用方用 a, b = login_api() 解包
    return resp.json(), resp.status_code

# 直接运行本文件时才执行；被别的文件 import 时不会跑
if __name__ == "__main__":
    # [0] 只取返回的第一个值（json 身体）；不要写两个 return
    print(login_api()[0])
