from requests import request
import random
import datas


def register_api(username, email, password):
    # 拼接注册地址：url_inter 已带末尾 /，这里只接 'auth/register'（不要写成 '/auth/register'）
    try:
        register_url = datas.url_inter + 'auth/register'
        resp = request(
            method='post',  # 注册一般是 POST，参数放 body
            url=register_url,
            # 账号信息由调用方传入；用了 json= 时 requests 会自动带 Content-Type: application/json
            json={
                "username": username,
                "email": email,
                "password": password,
            },
            timeout=20,  # 最多等 20 秒，避免公网/隧道卡住一直不返回
        )
        # 当前返回元组：(业务字典 resp.json(), HTTP状态码)，靠位置取
        # 更推荐以后改成字典，例如 {"body": resp.json(), "status_code": resp.status_code}，按名字取
        return resp.json(), resp.status_code
    except Exception as e:
        # 客户端异常（连不上等）：错误信息 + 自约定 500，不是服务端真实状态码
        return str(e), 500


# 直接运行本文件时才执行；被 import 时不会跑
if __name__ == "__main__":
    # 随机后缀放在入口生成，避免用户名/邮箱重复导致注册失败
    n = random.randint(1000, 9999)
    username = f"wkang{n}"
    email = f"{n}@wkangs.com"
    password = f"password{n}"
    print(register_api(username, email, password))
