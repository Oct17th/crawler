# -*- coding:utf8 -*-
# python抓取解析网页
# 慕课网自定义python接口测试练习
from urllib import parse
from urllib import request

'''
GET请求
'''
url = "http://reg.haibian.com/login/ajax_login"
# 定义请求数据，并对数据赋值
data = {}
data['loginname'] = 'student@qq.com'
data['password'] = '96e79218965eb72c92a549dd5a330112'  # 百度MD5加密111111
# 对请求数据进行编码
data = parse.urlencode(data)
# 将数据和URL进行连接
request0 = url + '?' + data
# 打开请求获取对象
requestResponse = request.urlopen(request0)
# 读取服务端返回数据
responseStr = requestResponse.read()
# 将获得的结果转码
responseStr = bytes(responseStr).decode('unicode_escape')  # python3里，decode(解码)表示将“字节流”按照某种规则转换成“文本”，为bytes的方法，str没有该方法
# 打印数据
print(responseStr)

'''
POST请求
'''
url0 = "http://xapi.kybyun.com/user/login"
headers = {
    "Host": "xapi.kybyun.com",
    "Connection": "keep_alive",
    "User-Agent": "BangXueTang AipBot/1.0(BangXueTang-IOS/2.1.3.1; iOS/9.30; iPhone 6 Plus",
    "KY-UKEY": "940cd0dffd371d41eb0acbb7694fd5e9",
    "KY-SYSDEV": "iPhone 6 Plus",
    "KY-SPEID": "10010101",
    "KY-SCHID": "1044",
    "KY-APPCHG": "AppStore",
    "Connection": "keep_alive",
    "KY-UUID": "6ff7563dbd47c8077905c392bc0d8b3",
    "KY-YEAR": "2017",
    "Accept-Language": "zh-Hans-CN;q=1",
    "KY-SYSVER": "9.3",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "KY-APPVER":"2.1.3.1",
    "KY-APPVERS":"4",
    "KY-APPTYPE":"21"
}
data0 = {
    "appchg": "AppStore",
    "apptype": "21",
    "appver": "2.1.3.1",
    "email": "mushishi01",
    "isbind": "0",
    "passwd": "111111",
    "sysdev": "iPhone 6 Plus",
    "sysver": "9.3",
    "uuid": "6ff7563dbd47c8077905c392bc0d8b3"
}
# 编码
data0 = parse.urlencode(data0).encode(encoding='UTF8')
req = request.Request(url0, data0,headers)
# 打开地址赋值变量
responseStr0 = request.urlopen(req)
responseStr0 = responseStr0.read()
responseStr0 = bytes(responseStr0).decode('unicode_escape')
print(responseStr0)
