# coding=utf-8
import requests
import json

# 设置Server酱post地址 不需要可以删除
serverChan = "https://sctapi.ftqq.com/SCT16742TCvvCPg4nsKGMGAekd2dpbb9i.send"
# 状态地址
current_url = 'https://zhiyou.smzdm.com/user/info/jsonp_get_current'
# 签到地址
checkin_url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
# 用用户名和密码登录后获取Cookie
userCookie = "smzdm_user_source=C36AD34D62A48452DA05D0EF2EB5B589; device_id=1851137730151036430938001793bf1aa4c39e6ca867f216a9aafc86ff; userId=1059067167; r_sort_type=score; __ckguid=ooy3nG7GTCWJjNbywBTEj52; __jsluid_s=477dae8faa7e522df0b0b213cb4d367e; homepage_sug=a; _zdmA.uid=ZDMA.FaoTOANnU.1611557565.2419200; ss_ab=ss58; smzdm_collection_yuanchuang=71293801; wt3_sid=%3B999768690672041; s_his=%E8%A1%8C%E8%BD%A6%E8%AE%B0%E5%BD%95%E4%BB%AA%2C%E8%BD%A6%20%E9%A6%99%E6%B0%B4%2Cdiptyque%2Cdiptyque%20%E8%BD%A6%E8%BD%BD%2C%E8%BD%A6%E8%BD%BD%20%E9%A6%99%E6%B0%B4%2C%E9%95%BF%E9%92%B1%E5%8C%85%2C%E9%95%BF%20%E9%92%B1%E5%8C%85%2C%E5%8C%A1%E5%A8%81%2C%E5%8C%A1%E5%A8%81%20%E7%A7%B0%E6%84%8F%2C%E5%8C%A1%E5%A8%81%20%E5%84%BF%E7%AB%A5; sess=NmQ1ZDV8MTYxNzM3MDUwNnwxMDU5MDY3MTY3fDc3NGEyOWEyN2YzYjQ3ZjNiZTRlMThjY2IxY2VmZjNh; user=user%3A1059067167%7C1059067167; smzdm_id=1059067167; wt3_eid=%3B999768690672041%7C2160022858800512364%232161218648400883621; smzdm_collection_youhui=29670676; smzdm_user_view=108B35B4334A907F8253F2744B60B389"
headers = {
    'Referer': 'https://www.smzdm.com/',
    'Host': 'zhiyou.smzdm.com',
    'Cookie': userCookie,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def req(url):
    url = url
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = json.loads(res.text)
        return data


data = req(current_url)
if data['checkin']['has_checkin']:
    info = '%s ：%s 你目前积分：%s，经验值：%s，金币：%s，碎银子：%s，威望：%s，等级：%s，已经签到：%s天' % (data['sys_date'], data['nickname'], data['point'], data['exp'], data['gold'], data['silver'], data['prestige'], data['level'],data['checkin']['daily_checkin_num'])
    print(info)
    # 通过Server酱发送状态 不需要可以删除
    requests.post(serverChan, data={'text': data['nickname'] + '已经签到过了', 'desp': info})
else:
    checkin = req(checkin_url)['data']
    # print(checkin)
    info = '%s 目前积分：%s，增加积分：%s，经验值：%s，金币：%s，威望：%s，等级：%s' % (data['nickname'], checkin['point'], checkin['add_point'], checkin['exp'], checkin['gold'], checkin['prestige'], checkin['rank'])
    print(info)
    # 通过Server酱发送状态 不需要可以删除
    requests.post(serverChan, data={'text': data['nickname'] + '签到信息', 'desp': info})
 
