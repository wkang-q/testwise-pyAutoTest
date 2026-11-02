from requests import request
import datas

def login_api():
    login_url = datas.url_local + 'auth/login'
    resp = request(
        method='post',
        url=login_url,
        json={"account": "wkang", "password": "your-password"}
    )
    return resp.json(), resp.status_code

if __name__ == "__main__":
    print(login_api()[0])

