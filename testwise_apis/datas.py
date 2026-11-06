# 本地 UAT 基地址（末尾带 /，后面拼接时不要再写 '/auth/...'，写成 'auth/...'）
# 否则会变成 api//auth/...，双斜杠会进鉴权中间件，报「请先登录」
url_local = 'http://127.0.0.1:12865/api/'

# 公网地址，走 Cloudflare 隧道；隧道不稳时会慢或 530，学习优先用上面本地
url_inter = 'https://testwise-uat.wkangs.cn/api/'
