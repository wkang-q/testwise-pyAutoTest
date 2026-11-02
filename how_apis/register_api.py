from requests import request
import random
import datas

def register_api():
    # 随机后缀，避免用户名/邮箱重复导致注册失败
    n = random.randint(1000, 9999)
    # mobile = f"138{random.randint(10000000, 99999999)}"  # 需要手机号时再打开

    # 拼接时不要写成 '/auth/register'，否则会多一个 /
    register_url = datas.url_local + 'auth/register'
    resp = request(
        method='post',
        url=register_url,
        # 用了 json= 时，requests 通常会自动带 Content-Type: application/json
        # headers={"Content-Type": "application/json"},
        json={
            "username": f"wkang{n}",
            "email": f"{n}@wkangs.com",
            "password": f"password{n}",
        },
        timeout=20,  # 最多等 20 秒，避免公网/隧道卡住一直不返回
    )
    print(resp.status_code)
    print(resp.json())  # .json() 要加括号，否则打印的是方法本身

if __name__ == "__main__":
    # 入口：必须写 register_api()，漏括号只是拿到函数对象，不会发请求
    register_api()
