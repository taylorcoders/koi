'''
Version=20220615
cron: 5 0 * * *
new Env('安静的锦鲤');
入口: 京东首页>领券>锦鲤红包
变量: JD_COOKIE,kois,WindfggJinliToken,Proxy_Url
export Proxy_Url='代理网址 推荐星空 生成选择txt 一次一个'
export WindfggJinliToken="windfgg 锦鲤 token" 
export JD_COOKIE="第1个cookie&第2个cookie"
export kois=" 第1个cookie的pin & 第2个cookie的pin "
环境变量kois中填入需要助力的pt_pin，有多个请用 '@'或'&'或空格 符号连接,不填默认全部账号内部随机助力
脚本内或环境变量填写，优先环境变量
'''
import re
import json
import datetime
import os
import time
import logging  # 用于日志输出
import requests
from urllib.parse import quote_plus, unquote_plus
import urllib3
urllib3.disable_warnings()

if "LOG_DEBUG" in os.environ:  # 判断调试模式变量
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')  # 设置日志为 Debug等级输出
    logger = logging.getLogger(__name__)  # 主模块
    logger.debug("\nDEBUG模式开启!\n")  # 消息输出
else:  # 判断分支
    logging.basicConfig(level=logging.INFO, format='%(message)s')  # Info级日志
    logger = logging.getLogger(__name__)  # 主模块


requests.packages.urllib3.disable_warnings()


def get_log(functionId,pin):
    windfgg_token= os.environ.get("WindfggJinliToken", '')
    windfgg_url = f"http://20.24.232.57/jd/jinli?pin={pin}&token={windfgg_token}"
    for i in range(5):
        try:
            res = requests.get(windfgg_url,timeout=20,verify=False)
            res = res.json()
            if not res["data"]["log"]:
                logger.info("获取log失败： ", res["msg"])
                continue
            resp = res['data']
            return resp["log"], resp["random"], resp["ck"], res['msg']
        except Exception as e:
            logger.info(f"获取log出错 等待十秒 {res}")
            time.sleep(10)
            count=i+1;
            logger.info(f"第{count}次重试")
    else:
        logger.info("5次重试失败，退出程序")
        exit()


# 13位时间戳
def gettimestamp():
    return str(int(time.time() * 1000))

# 获取pin
cookie_findall = re.compile(r'pt_pin=(.+?);')
cookie_findall_key = re.compile(r'pt_key=(.+?);')
def get_pin(cookie):
    try:
        return cookie_findall.findall(cookie)[0]
    except:
        logger.info('ck格式不正确，请检查')
        
def get_key(cookie):
    try:
        return cookie_findall_key.findall(cookie)[0]
    except:
        logger.info('ck格式不正确，请检查')

def get_proxy(url):
    payload={}
    headers = {}
    for n in range(3):
        try:
            response = requests.request("GET", url, headers=headers, data=payload,verify=False)
            sss=response.text
            proxies = {
                "http": f"http://{sss}",
                'https': f'http://{sss}'
            }
            res = requests.get('https://www.baidu.com', proxies=proxies, timeout=10,verify=False)
            if res.status_code == 200:
                return proxies,sss
        except Exception as e:
            logger.info(f"代理超时或错误 重新获取")
            logger.info(f"第{n}次重试")
      
def taskPostUrl(functionId, body, cookie):
    pt_pin=get_pin(cookie)
    pt_key=get_key(cookie)
    proxy_url=os.environ.get("Proxy_Url", '')
    proxies,sss=get_proxy(proxy_url)
    log, randoms, ck, msg = get_log(functionId,pt_pin)
    body.update({"log": log, "random": randoms})
    
    logger.info(f'[{pt_pin}]使用代理:'+sss)
    logger.info("Log剩余次数:"+str(msg))
    cookie=f'pt_pin={pt_pin};pt_key={pt_key};'
    url = f'https://api.m.jd.com/api?appid=jinlihongbao&functionId={functionId}&loginType=2&client=jinlihongbao&t={gettimestamp()}&clientVersion=10.1.4&osVersion=-1'
    headers = {
        'Cookie': cookie,
        'Host': 'api.m.jd.com',
        'Connection': 'keep-alive',
        'origin': 'https://happy.m.jd.com',
        'referer': 'https://happy.m.jd.com/babelDiy/zjyw/3ugedFa7yA6NhxLN5gw2L3PF9sQC/index.html?channel=9&un_area=4_134_19915_0',
        'Content-Type': 'application/x-www-form-urlencoded',
        "User-Agent": 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1654650382027%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22EG%3D%3D%22%2C%22ad%22%3A%22CzDuCQGzZNOnEJc5DNS4Dq%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctq%3D%22%2C%22ud%22%3A%22CzDuCQGzZNOnEJc5DNS4Dq%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 9; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046010 Mobile Safari/537.36',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    data = f"body={json.dumps(body)}"
    for n in range(3):
        try:
            res = requests.post(url, headers=headers, proxies=proxies,data=data,verify=False).text
            return res
        except Exception as e:
            if n == 2:
                logger.info('API请求失败，请检查网路重试❗\n')
                
def taskPostUrlNoLog(functionId, body, cookie):
    proxy_url=os.environ.get("Proxy_Url", '')
    proxies,sss=get_proxy(proxy_url)
    pt_pin=get_pin(cookie)
    pt_key=get_key(cookie)
    cookie=f'pt_pin={pt_pin};pt_key={pt_key};'
    logger.info(f'[{pt_pin}]使用代理:'+sss)
    url = f'https://api.m.jd.com/api?appid=jinlihongbao&functionId={functionId}&loginType=2&client=jinlihongbao&t={gettimestamp()}&clientVersion=10.1.4&osVersion=-1'
    headers = {
        'Cookie': cookie,
        'Host': 'api.m.jd.com',
        'Connection': 'keep-alive',
        'origin': 'https://happy.m.jd.com',
        'referer': 'https://happy.m.jd.com/babelDiy/zjyw/3ugedFa7yA6NhxLN5gw2L3PF9sQC/index.html?channel=9&un_area=4_134_19915_0',
        'Content-Type': 'application/x-www-form-urlencoded',
        "User-Agent": 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1654650382027%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22EG%3D%3D%22%2C%22ad%22%3A%22CzDuCQGzZNOnEJc5DNS4Dq%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctq%3D%22%2C%22ud%22%3A%22CzDuCQGzZNOnEJc5DNS4Dq%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 9; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046010 Mobile Safari/537.36',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    data = f"body={json.dumps(body)}"
    for n in range(3):
        try:
            res = requests.post(url, headers=headers,data=data,verify=False,proxies=proxies).text
            return res
        except Exception as e:
            if n == 2:
                logger.info('API请求失败，请检查网路重试❗\n')
                

    ''' 测试代码
if __name__ == '__main__':

    try:
        cookie_list = os.environ["JD_COOKIE"].split("&")
    except:
        with open('cklist.txt', 'r') as f:
            cookie_list = f.read().split('\n')
    for cookie in cookie_list:
        body={"redPacketId": 458767747, "followShop": 0, "sceneid": 'JLHBhPageh5'}
        res= taskPostUrl('jinli_h5assist',get_pin(cookie),body,cookie)
        print(res)

    stop=True
    count=0
    while stop == True:  # 循环控制条件
        pin=''
        cookie=''
        body={"redPacketId": 459177504, "followShop": 0, "sceneid": 'JLHBhPageh5'}
        res= taskPostUrl('jinli_h5assist',pin,body,cookie)
        if res.find('403')<=1:
            print(res)
            count = count+1;
        else:
            print(res)
            print(datetime.datetime.now())
            print(count)
            stop=False
    '''
