from requests import request
import datas


def login_api(account, password):
    # 拼接登录地址：datas 里已有末尾 /，这里只接 'auth/login'
    try:
        login_url = datas.url_inter + 'auth/login'
        resp = request(
            method='post',  # 登录一般是 POST，参数放 body
            url=login_url,
            # 本接口字段是 account + password（不是 username）；账号密码由调用方传入
            json={"account": account, "password": password},
            timeout=20,  # 练超时时可临时改很小（如 0.01）；正常联调改回 20
        )
        # 成功：返回三个值——token、完整响应体、HTTP 状态码
        access_token = resp.json()['access_token']
        return access_token, resp.json(), resp.status_code

    except KeyError as a:
        # 能进到这里，通常说明 resp 已有（request / json 已成功），只是缺 access_token
        # 业务失败原因在响应体里，不在 KeyError 文案里（str(a) 往往只是 'access_token'）
        body = resp.json()
        # get：有 detail 用 detail；没有则退回整个 body，避免处理错误时再 KeyError
        reason = body.get('detail', body)
        return f'未返回{a}，请检查。原因：{reason}', resp.status_code

    except Exception as e:
        # 兜底：超时/连不上等，可能还没有 resp，不要去取 resp / detail
        # 自约定 500，表示客户端侧异常（不是服务端真实状态码）
        return str(e), 500


# 直接运行本文件时才执行；被别的文件 import 时不会跑
if __name__ == "__main__":
    # 成功时 [0] 是 token；失败时返回的是 (说明, 状态码)，不要默认当成功解包三个值
    print(login_api("wkang", "your-password"))
