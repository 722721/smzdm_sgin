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
userCookie = "shshshfpa=0148829e-6013-eb74-e37c-ed2d6efcc629-1532913919; shshshfpb=19194cf974b4e44878b73dc456249c614c10d2eff2b2b83635a0654e65; pinId=sjrAwACEpsgpNMjjEToPnQ; unick=%E4%B8%80%E4%B8%AA%E6%AF%94%E8%BE%83%E8%8B%B1%E4%BF%8A%E7%9A%84%E4%B9%B0%E5%AE%B6; _tp=UUinbWQXyVv0WP%2FhgabBOQ%3D%3D; _pst=774584347_m; pin=774584347_m; user-key=e96bd5ca-8d3a-4b97-bb35-bcbdf478d151; areaId=16; ipLoc-djd=16-1315-3486-59641; TrackID=1WhmzsMP2Ada9KCxgpGaNJzMK99yRzIfCZxy6Ps844DHNHKJF8dGsy654oq5gnvpQzlBV_BoKD7rann6K653lNf3BahC-NIRicH5-wxU0HHg; ceshi3.com=201; cn=178; webp=1; visitkey=50147673626491242; TrackerID=bHQo_SjUnVM9JDlmq9sv6BlFm5t86MFet-TkO3FW6J5hxWb5rd0ePu83I2AOYyTzc5KVTvXMdvuGIitt6dUk4Q7ltk-ZOYs9ZMj--ZKVnU1IM1fiCMRn7F0GetUPtEy_; pt_key=AAJgQaPMADCYVyqEwfgBpYpKWj004pSzlVkN_Jpkid9LllMzSKGAR0yjTTmK-cMjRoehNi_bKAM; pt_pin=774584347_m; pt_token=k5idl04l; pwdt_id=774584347_m; sfstoken=tk01mae901c3ea8sMSszeDJlV3pYXUAPZ7hBND1e25QbxNJ2jgVz04owqPSEpGkquSkkGXCfT/lKo7NOYOs3vnOT8MHm; sc_width=1024; retina=0; __jdc=122270672; CCC_SE=ADC_45QoTmhg6iTf%2fCIu3gG5rq8no%2fHTGrSh5AslJ%2bNY0ouP5SE3wIJwGC%2fL9VFhr2vr8Sg4nSufzY2boDr8qHvdoNjTIY9WUmedXO1DGnzRkVpI971V%2flK%2flcdzv9c5UR30vm%2btvTwudmgl%2b6BymqHpNwzPDLRa%2bss3gRm9Gkdr%2f1g7ju6MAoTPXKCCbw21ahoELUXgXEoSSg%2bu7jm8bZHrfd7PgJB0Rq65%2bNzChO1wjQzQwkCKV9fprOTRcHAe4Fnh3QeoORagwbeVfdrhzq0su9d%2fZrGQFeXAdQE3TOkyjgHhTL6u50%2fg0j%2bP7GaMTywTCsW0cyNwYrXXafJtFn0B3mWCw%2fOHneoxr49pG9xLV0O2TZ7E%2bl8HPThrLmhYFOMpy%2fSv%2fW3GGAkpJcAF6clgSk8KvuecJgcJl4xrdTIyhgol1UD9hjWlmTvJR6FWA6SttBAZseZ937IXTOYD6AzH%2fekce7gcpNsLRWczO9XM%2bXFevRnyBqm18WbT%2bEspRkB56%2bQrFfsQxzaI82DtMhFh58YD50U3ALyl9eb848H5L9JIK0ZjVf1ZL%2f1C0KpiePPLNNTEabCJtpvuCQ7kK3eyyYmO%2faroLzDUhjPMMmoTCv0%3d; unpl=V2_ZzNtbUoCS0d1DE9VKxoLUGJUEAlLAENHcQhCVnMQDFY3U0IIclRCFnUUR1ZnGFUUZwQZXkVcQh1FCEdkexhdBGYKGlRKVXMVcQ8oVRUZVQAJbUVeFVQQEH0MTgMrHg4AbgoibUFXcxV0OEZTehhfBm4GFlhAX0IVdwtPVHkZVARuMyJdSlNzJaKh6IL3v4i8zdSg33JTRRZzDEdVehpsBFcCIhYsVg4VcglHV3gQWQFiARpcQlVAHHUKRlx6EGwEVwA%3d; __jdv=122270672%7Cwww.linkstars.com%7Ct_1000089893_156_0_184__f2f2b4959fa6c488%7Ctuiguang%7C9d9c1580a2fd4f3e8f1c515398abaaad%7C1615191926806; rurl=%2F%2Fwq.jd.com%2Fpinbind%2FpinTokenRedirect%3Ftype%3D1%26biz%3Dtttwxapp%26rurl%3Dhttps%253A%252F%252Fpro.m.jd.com%252Fwq%252Factive%252F3cDksxhKNBq4UgX2sXcMMHrnT6Fy%252Findex.html%253Fcu%253Dtrue%2526utm_source%253Dwww.linkstars.com%2526utm_medium%253Dtuiguang%2526utm_campaign%253Dt_1000089893_156_0_184__f2f2b4959fa6c488%2526utm_term%253D9d9c1580a2fd4f3e8f1c515398abaaad%26scope%3D0%26sceneid%3D9001%26btnTips%3D%26hideApp%3D0; __jda=122270672.16002284543901328131908.1600228454.1615191395.1615255508.125; __jdb=122270672.2.16002284543901328131908|125.1615255508; 3AB9D23F7A4B3C9B=V6U2IRLCBQGZKHNLH2GWDHH7F5UKJDDFJ5SQ7SLBRL7X55VB3U7F5RILW3XO7KYQ3DWD2BHRCZ3ASDQYHS3ONPTNXM; wxa_level=1; jxsid=16152555232997888317; cid=9; PPRD_P=LOGID.1615191926838.714490448-UUID.16002284543901328131908; jxsid_s_u=https%3A//home.m.jd.com/myJd/newhome.action; shshshfp=4d0b1684941931751772a6c510a7c309; shshshsID=b6e7b66c5f4370d08c260a5a12947a0b_1_1615255527970; wqmnx1=MDEyNjM5Ni9qSmUxNk0udzt4ZTNUIGgwNTUyNy00UkghKQ%3D%3D; __wga=1615255544549.1615255527108.1614914468266.1614914468266.2.2; jxsid_s_t=1615255544662"
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
 
