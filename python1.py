import requests
import execjs
def name_password(data):
    jsstr=get_js()
    ctx=execjs.compile(jsstr)#加载JS文件
    # 调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数
    return (ctx.call('encodeInp', data))
def get_js():
    f = open("conwork.js", 'r', encoding='utf-8')  # 打开JS文件1
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr
truepassword=name_password(username)+"%%%"+name_password(password)
# 创建session对象，可以保存Cookie值
ssion = requests.session()
# 处理 headers
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
# 3需要登录的用户名和密码
data = {
        'username': '', # 学生账号
        'password': '', # 账号的密码
        'encoded':truepassword
}  
# 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
response = ssion.post("http://jwxt.gduf.edu.cn/jsxsd/xk/LoginToXk", headers = headers,data = data)
#  ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = ssion.get("http://jwxt.gduf.edu.cn/jsxsd/xskb/xskb_list.do")
# 打印响应内容
print (response.text)
fb = open('KB.txt','w',encoding='utf-8')
fb.write(response.text)
fb.close()
