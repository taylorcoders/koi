'''
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

import os
import re
import time
import logging  # 用于日志输出
import requests
import os.path



from angryKoi_util1 import taskPostUrl,taskPostUrlNoLog

if "LOG_DEBUG" in os.environ:  # 判断调试模式变量
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')  # 设置日志为 Debug等级输出
    logger = logging.getLogger(__name__)  # 主模块
    logger.debug("\nDEBUG模式开启!\n")  # 消息输出
else:  # 判断分支
    logging.basicConfig(level=logging.INFO, format='%(message)s')  # Info级日志
    logger = logging.getLogger(__name__)  # 主模块

requests.packages.urllib3.disable_warnings()

sceneid = 'JLHBhPageh5'

# 获取pin
cookie_findall = re.compile(r'pt_pin=(.+?);')


def get_pin(cookie):
    try:
        return cookie_findall.findall(cookie)[0]
    except:
        logger.info('ck格式不正确，请检查')


# 13位时间戳
def gettimestamp():
    return str(int(time.time() * 1000))


# 开启助力
code_findall = re.compile(r'"code":(.*?),')


def h5launch(cookie):
    body = {"followShop": 1, "sceneid": sceneid}
    res = taskPostUrlNoLog("h5launch",body, cookie)
    if not res:
        return
    Code = code_findall.findall(res)
    if Code:
        if str(Code[0]) == '0':
            logger.info(f"账号 {get_pin(cookie)} 开启助力码成功\n")
        else:
            logger.info(f"账号 {get_pin(cookie)} 开启助力码失败")
            logger.info(res)
    else:
        logger.info(f"账号 {get_pin(cookie)} 开启助力码失败")
        exit()


# 获取助力码
id_findall = re.compile(r'","id":(.+?),"')


def h5activityIndex(cookie):
    h5launch(cookie)
    global inviteCode_list
    body = {"isjdapp": 1}
    res = taskPostUrlNoLog("h5activityIndex",body, cookie)
    if not res:
        return
    inviteCode = id_findall.findall(res)
    if inviteCode:
        inviteCode = inviteCode[0]
        # inviteCode_list.append(inviteCode)
        logger.info(f"账号 {get_pin(cookie)} 的锦鲤红包助力码为 {inviteCode}\n")
        return inviteCode
    else:
        logger.info(f"账号 {get_pin(cookie)} 获取助力码失败\n")
        exit()


# 助力
statusDesc_findall = re.compile(r',"statusDesc":"(.+?)"')


def jinli_h5assist(cookie, redPacketId):
    body = {"redPacketId": redPacketId, "followShop": 0, "sceneid": sceneid}
    res = taskPostUrl('jinli_h5assist',body, cookie)
    logger.info(f'账号 {get_pin(cookie)} 去助力{redPacketId}')
    if not res:
        return
    statusDesc = statusDesc_findall.findall(res)
    if statusDesc:
        statusDesc = statusDesc[0]
        logger.info(f"{statusDesc}\n")
        if "TA的助力已满" in statusDesc:
            return True
    else:
        logger.info(f"错误\n{res}\n")


# 开红包
biz_msg_findall = re.compile(r'"biz_msg":"(.*?)"')
discount_findall = re.compile(r'"discount":"(.*?)"')


def h5receiveRedpacketAll(cookie):
    body = {"sceneid": sceneid}
    res = taskPostUrl("h5receiveRedpacketAll", body, cookie)
    logger.info(f'账号 {get_pin(cookie)} 开红包')
    if not res:
        return
    try:
        biz_msg = biz_msg_findall.findall(res)[0]
    except:
        logger.info(res)
        return
    discount = discount_findall.findall(res)
    if discount:
        discount = discount[0]
        logger.info(f"恭喜您，获得红包 {discount}\n")
        return h5receiveRedpacketAll(cookie)
    else:
        logger.info(f"{biz_msg}\n")


# 读取环境变量
def get_env(env):
    try:
        if env in os.environ:
            a = os.environ[env]
        else:
            a = ""
    except:
        a = ''
    return a


def main():
    logger.info('🔔安静的锦鲤，开始！\n')
    windfgg_token= os.environ.get("WindfggJinliToken", '')
    if not windfgg_token:
        logger.info("未配置WindfggJinliToken")
        exit()
    proxy_url=os.environ.get("Proxy_Url", '')
    if not proxy_url:
        logger.info("未配置Proxy_Url")
        exit()
    logger.info(f'WindfggJinliToken: {windfgg_token}')
    logger.info(f'Proxy_Url: {proxy_url}')
    try:
        cookie_list = os.environ["JD_COOKIE"].split("&")
    except:
        with open('cklist.txt', 'r') as f:
            cookie_list = f.read().split('\n')
    logger.info(f"共:{len(cookie_list)}个CK")
    if not cookie_list:
        logger.info("没有找到ck")
        exit()
    logger.info(f'====================共{len(cookie_list)}京东个账号Cookie=========\n')

    debug_pin = get_env('kois')
    if debug_pin:
        cookie_list_pin = [cookie for cookie in cookie_list if get_pin(cookie) in debug_pin]
    else:
        cookie_list_pin = cookie_list
    logger.info('*******************助力*******************\n')
    index = 0

    inviteCode = h5activityIndex(cookie_list_pin[index])
    for cookie in cookie_list:
        if cookie.find('app_open')<=0:
            logger.info('*******************当前ck不是appck 跳过助力*******************\n')
            continue
        status = jinli_h5assist(cookie, inviteCode)
        if status:
            logger.info('*******************开红包*******************\n')
            h5receiveRedpacketAll(cookie_list_pin[index])
            index += 1
            if index >= len(cookie_list_pin):
                break
            for i in range(len(cookie_list_pin[index:])):
                index += i
                inviteCode = h5activityIndex(cookie_list_pin[index])
                if inviteCode:
                    break
    else:
        logger.info('*******************开红包*******************\n')
        h5receiveRedpacketAll(cookie_list_pin[index])
        logger.info('没有需要助力的锦鲤红包助力码\n')


if __name__ == '__main__':
    main()
