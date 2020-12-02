# coding=utf-8
import requests
import json

# 设置Server酱post地址 不需要可以删除
serverChan = "https://sc.ftqq.com/SCU51384Te154b9ccaddf2889241be0dab32e97445cda1acfeb986.send"
# 状态地址
current_url = 'https://zhiyou.smzdm.com/user/info/jsonp_get_current'
# 签到地址
checkin_url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
# 用用户名和密码登录后获取Cookie
userCookie = "smzdm_user_source=C36AD34D62A48452DA05D0EF2EB5B589; device_id=1851137730151036430938001793bf1aa4c39e6ca867f216a9aafc86ff; userId=1059067167; r_sort_type=score; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1578296195; __ckguid=ooy3nG7GTCWJjNbywBTEj52; __jsluid_s=477dae8faa7e522df0b0b213cb4d367e; wt3_sid=%3B999768690672041; homepage_sug=a; _zdmA.uid=ZDMA.84xqfnMWS.1606803091.2419200; s_his=%E5%AE%9C%E4%B9%B0%E5%AE%B6%20%E8%BD%A6%2C%E4%B8%BB%E6%9C%BA%2Ci3%20%E4%B8%BB%E6%9C%BA%2C%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98%2C%E6%98%BE%E7%A4%BA%E5%99%A8%2C%E6%98%BE%E7%A4%BA%E5%99%A8%2027%2C%E9%9B%AA%E4%BD%9B%E5%85%B0%20%E7%A7%91%E6%B2%83%E5%85%B9%202020%2C%E5%AE%9C%E4%B9%B0%E8%BD%A6%2CDS720%2C%E9%A3%8E%E6%9A%B4; ss_ab=ss20; wt3_eid=%3B999768690672041%7C2160022858800512364%232160680340900823767; sess=NmQ1ZDV8MTYxMjA5NTIzOXwxMDU5MDY3MTY3fDk4ZmMwNTQ5MzdiNGE4ZDRlNmUyZjBiYjIyYzIxMGQ0; user=user%3A1059067167%7C1059067167; smzdm_id=1059067167; smzdm_user_view=2988E4A1382B3F66691C388B79D87BC2"
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
 
