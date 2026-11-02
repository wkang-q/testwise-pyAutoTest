from ast import main
from requests import  request
import random
import datas

def register_api():
    n = random.randint(1000,9999)
    # mobile = f"138{random.randint(10000000, 99999999)}"
    register_url = datas.url_local + 'auth/register'
    resp = request(
        method='post',
        url=register_url,
        # headers={"Content-Type": "application/json"},
        json={"username": f"wkang{n}", "email": f"{n}@wkangs.com", "password": f"password{n}"},
        timeout=20,  # 最多等 20 秒，避免一直卡住
    )
    print(resp.status_code)
    print(resp.json())

if __name__ == "__main__":
    register_api()




