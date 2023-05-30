import json

import requests


class ArgsApi:

    url = "http://a.argso.vip/api/dy/encrypt"

    @classmethod
    def send(cls, u):
        payload = {
            "url": u,
            "headers": {
                "Cookie": "install_id=3285777376617822;",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "passport-sdk-version": "20352",
                "x-ss-req-ticket": "1667204506545",
            },
        }
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            "x-token": "MDdhY2RkOWUtZGQxYS1jM2ZiLTY3YTYtYzU4NjE1YjgzYTJi"
        }
        response = requests.post(cls.url, json=payload, headers=headers)
        if response.status_code != 200:
            raise Exception("network error", response.text)

        return json.loads(response.text)


def other3():
    # {'device_id': '3567263506787613', 'iid': '2511732343843591', 'openudid': 'b8a658dabc2d5fe6'}
    did = '3567263506787613'
    iid = '2511732343843591'
    sec_user_id = 'MS4wLjABAAAAO5m5SvCQ9Wx-zlXpNqGAqcoplSx_hfQ0Iw57RgmZmmM'
    url = f'https://aweme.snssdk.com/aweme/v1/user/profile/other/?sec_user_id={sec_user_id}&address_book_access=2&from=0&source=UserProfileFragment_initUserData&card_partition=0&card_style=0&hit_ab_test=0&btn_in_value=0&publish_video_strategy_type=2&user_avatar_shrink=188_188&user_cover_shrink=750_422&land_to=1&iid={iid}&device_id={did}&ac=wifi&channel=tengxun_1128_64&aid=1128&app_name=aweme&version_code=200800&version_name=20.8.0&device_platform=android&os=android&ssmix=a&device_type=ONEPLUS+A5010&device_brand=OnePlus&language=zh&os_api=27&os_version=8.1.0&openudid=3239f8f74009a54b&manifest_version_code=200801&resolution=1080*2034&dpi=420&update_version_code=20809900&_rticket=1664161220553&package=com.ss.android.ugc.aweme&cpu_support64=true&host_abi=arm64-v8a&is_guest_mode=0&app_type=normal&minor_status=0&appTheme=light&need_personal_recommend=1&is_android_pad=0&ts=1664161219&cdid=7a4a6332-3a89-4272-953e-1fc956b7efd6&uuid=868717030760391'
    encrypt_res = ArgsApi.send(u=url)
    print(encrypt_res)
    headers = {
        # 'Host': 'api26-core-lq.amemv.com',
        # 'x-tt-dt': 'AAAXBTCMI3QCYQHOHGLF35OXDDUTHTRUD27GVOSECDZ3766XE3HPO464IP7FA7XZM3SBW65C23K2ILTJHSPVY2R72KCFGWGHCB54LGVKMH54WHOIFJ35OH3Y3YCTS',
        'activity_now_client': '1669254604748',
        'sdk-version': '2',
        'passport-sdk-version': '18',
        'x-ss-req-ticket': '1669254571963',
        'x-vc-bdturing-sdk-version': '2.1.0.cn',
        'x-ss-dp': '1128',
        # 'x-tt-trace-id': '00-a753694609f9669d921b8fd45fd70468-a753694609f9669d-01',
        'user-agent': 'com.ss.android.ugc.aweme/160001 (Linux; U; Android 8.1.0; zh_CN_#Hans; Pixel; Build/OPM1.171019.012; Cronet/TTNetVersion:f5cbac28 2021-04-21 QuicVersion:47946d2a 2020-10-14)',
        'x-argus': encrypt_res.get('X-Argus'),
        'x-gorgon': encrypt_res.get('X-Gorgon'),
        'x-khronos': encrypt_res.get('X-Khronos'),
        'x-ladon': encrypt_res.get('X-Ladon'),
        'x-tyhon': encrypt_res.get('X-Tyhon'),
    }
    response = requests.get(url, headers=headers)
    print("data:", response.text, "|")

if __name__ == '__main__':
    # url = "https://api5-core-c-lq.amemv.com/aweme/v1/user/profile/other/?sec_user_id=MS4wLjABAAAAnOURxRU1foQZXVSCBO6rM11Y9ezKvL-BeETLcHtPvTkQoHamDzT_Bfe9g1EMUT0H&address_book_access=2&from=0&source=UserProfileFragment_initUserData&card_partition=0&card_style=0&hit_ab_test=1&btn_in_value=0&publish_video_strategy_type=2&user_avatar_shrink=188_188&user_cover_shrink=750_422&land_to=1&iid=1297870126583021&device_id=3271801812029661&ac=wifi&channel=zb_xiaomi_1128&aid=1128&app_name=aweme&version_code=230200&version_name=23.2.0&device_platform=android&os=android&ssmix=a&device_type=HD1910&device_brand=OnePlus&language=zh&os_api=25&os_version=7.1.2&manifest_version_code=230201&resolution=720*1280&dpi=240&update_version_code=23209900&_rticket=1669269713670&package=com.ss.android.ugc.aweme&mcc_mnc=46000&cpu_support64=true&host_abi=armeabi-v7a&ts=1669269713&is_guest_mode=0&app_type=normal&appTheme=light&need_personal_recommend=1&minor_status=0&is_android_pad=0&cdid=1df13891-c76a-4be6-9a36-7d4b315dd6aa&md=0&luckydog_token=qZaiG3SW9YPyv-e2NUdCJvzICuEBosnTUDumBgS30e272N1EStpf0CmlxxLXshOA&luckydog_base=LeTLCv-E2PoXHkVsU-_xsjDMHlpRwSqTq8tO1u5AIWhuX78tkGJDBleYvePlF-nFHWKDe3MoAgYY8kZ2FWd8BNT96ZuLb3us1KWh7cTFo1liS68-iiOFzpRd69U8zia5MVfZse_n0nQtjA_JCcJ2iOXxU29qv33BF7vgGru40JM&luckydog_data=MXkI1-ASFFInqJsIGu2aNw"
    # data = ArgsApi.send(u=url)
    # print(data)

    other3()


