from requests import request
import datas

def health_api():
    # 健康检查地址（UAT 正常端口是 12865；写成 12866 可故意练 ConnectionError）
    health_url = 'https://testwise-uat.wkangs.cn/health'
    try:
        # try 要包住 request：连不上时异常出在这里，包在外面接不住
        resp = request(
            method='get',  # GET 查询，字符串不要写成函数 get
            url=health_url,
            timeout=10,
        )
        # 成功：返回响应体 + 状态码（两个值用逗号一次 return）
        return resp.json(), resp.status_code
    except Exception as e:
        # 失败：返回错误信息，自己约定一个状态码方便后面判断
        return str(e), 500

# 只有直接运行本文件时才会执行；被 import 时不会跑
if __name__ == '__main__':
    print(health_api())
