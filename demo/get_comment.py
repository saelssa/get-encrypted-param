import json
import time
from hashlib import md5
from urllib.parse import urlencode, quote

import requests

from demo.api.api import XLadon, XGorgon, XArgus
from demo.bean.device_info import DeviceApp


class TestCommon:

    @classmethod
    def encrypt_header(cls, query_str: str, body: bytes, did):
        x_ss_stub = None
        if did is None or len(did) == 0:
            did = None

        if body is not None:
            x_ss_stub = md5(body).hexdigest().upper()

        x_khronos = int(time.time())
        x_ladon = XLadon.encrypt(x_khronos, DeviceApp.license_id)
        x_gorgon = XGorgon.build(query_str, x_ss_stub, DeviceApp.sdk_version, x_khronos)
        x_argus = XArgus.build_local({
            'deviceID': did,
            'licenseID': DeviceApp.license_id,
            'appVersion': DeviceApp.app_version,
            'sdkVersionStr': DeviceApp.sdk_version_str,
            'sdkVersion': DeviceApp.sdk_version,
            'x_khronos': x_khronos,
            'x_ss_stub': x_ss_stub,  # request for get is null
            'secDeviceToken': '',  # can be null
            'query': query_str,
            'x_bd_lanusk': None,  # return after login
        })

        return {
            'tt-request-time': str(int(time.time() * 1000)),
            'x-khronos': str(x_khronos),
            'x-ss-stub': x_ss_stub,
            'x-argus': x_argus,
            'x-gorgon': x_gorgon,
            'x-ladon': x_ladon,
        }

    @classmethod
    def get_feed(cls):
        query = {
            "action_mask": "-1",
            "audio_value": "0.06",
            "cached_item_num": "3",
            "count": "6",
            "feed_recommend_req_index": "4",
            "feed_style": "1",
            "filter_warn": "0",
            "font_category": "UICTContentSizeCategoryL",
            "gps_access": "0",
            "is_order_flow": "0",
            "last_ad_show_interval": "-1",
            "launch_times": "10",
            "location_permission": "false",
            "mac_address": "02:00:00:00:00:00",
            "max_cursor": "0",
            "pull_type": "2",
            "screen_type": "0",
            "sp": "5194",
            "type": "0",
            "volume": "0.06",
        }
        common = {
            "ac": "WIFI",
            "address_book_access": "2",
            "aid": "1128",
            "appTheme": "light",
            "app_name": "aweme",
            "app_version": "22.0.0",
            "build_number": "220015",
            "cdid": "B08223A7-06E2-443C-BBFD-AA47B5359739",
            "channel": "App Store",
            "device_id": "629334861677687",
            "device_platform": "iphone",
            "device_type": "iPhone8,1",
            "idfa": "E2CBBF07-B31C-4AC9-83CC-13347E3D4354",
            "iid": "1508946220164670",
            "is_guest_mode": "0",
            "is_vcd": "1",
            "js_sdk_version": "2.63.1.2",
            "minor_status": "0",
            "need_personal_recommend": "1",
            "openudid": "6d0cc0c63a86d6af9751e11de78ef406e323822b",
            "os_api": "18",
            "os_version": "12.1.4",
            "package": "com.ss.iphone.ugc.Aweme",
            "screen_width": "750",
            "slide_guide_has_shown": "1",
            "tma_jssdk_version": "2.63.1.2",
            "user_avatar_shrink": "96_96",
            "version_code": "22.0.0",
            "vid": "A4457E89-2843-4ADA-87AB-53A3FE84C7B0"
        }

        header = {
            "accept-encoding": "gzip, deflate, br",
            # "cookie": "odin_tt=e57a0183112cec841ef6396b71f38a571c07c3701b12a2b9102a56fddc4ae4fb0da5dd9a8f20858d62ca757ee0466023c75bce75ea8e8f35238f69861025bd6a; passport_csrf_token=9705fd14b1484c786d2d020cf830e37b; passport_csrf_token_default=9705fd14b1484c786d2d020cf830e37b; install_id=1508946220164670; ttreq=1$9d823d1483d5dc9840198e8b7e7705f9af543b99; msToken=_6QBt_L0VNlLRQruYoFGMaNYaegWuhbaB81VfkAstZvd7fMgh_KiibJgqwCh9K1-8SwE86pP9FRnkm9Ejj0dOpWB",
            "passport-sdk-version": "5.12.1",
            "sdk-version": "2",
            "user-agent": "Aweme 22.0.0 rv:220015 (iPhone; iOS 12.1.4; zh_CN) Cronet",
            # "x-argus": "jIzXaG/Ga4GvZhauoVz88N1cEILyr62hr6W6iZtPjTg4/f4XkCYLbmaQ/5M3e001J0k4VSBgDmLNIgC8waJuV50RCzfnToKaTtIB0d2Wf1nV3MLq2gimRO6jtHp9Cyhy1DABGM4KqwmsBJfsd+0dmgtq6RGb0vimNLZcz4Xkst6z12vXWA+6LhHL38I/70x2vumsKfOnUgElpWUNpYRQcPgv5yuNEGmAi3lXlS+xvOma7LwzmrbF1NmZHZFm81kviaY=",
            # "x-common-params-v2": "device_id=629334861677687&os_version=12.1.4&iid=1508946220164670&app_name=aweme&slide_guide_has_shown=1&ac=WIFI&appTheme=light&js_sdk_version=2.63.1.2&version_code=22.0.0&channel=App%20Store&is_vcd=1&tma_jssdk_version=2.63.1.2&os_api=18&need_personal_recommend=1&device_platform=iphone&device_type=iPhone8,1&is_guest_mode=0&build_number=220015&minor_status=0&aid=1128&mcc_mnc=&screen_width=750&package=com.pzkah.MonkeyTT&cdid=B08223A7-06E2-443C-BBFD-AA47B5359739&app_version=22.0.0&user_avatar_shrink=96_96&vid=A4457E89-2843-4ADA-87AB-53A3FE84C7B0&openudid=6d0cc0c63a86d6af9751e11de78ef406e323822b&idfa=E2CBBF07-B31C-4AC9-83CC-13347E3D4354&address_book_access=2",
            # "x-gorgon": "84046039b801fa804795943616110da0ed0b898d73b8d8fe6d65",
            # "x-khronos": "1662445522",
            # "x-ladon": "kmAtWzTM3+Z1otEPr9iCAnWe5ezCvZ+JZHDKK/WxVzPUWSnx",
            "x-ss-dp": "1128",
            # "x-tt-dt": "AAA4AYTGENURLVGEIKGJYF7XUTGUW26OZIQGNFZOOGQ2QZYVBQFGJPOPOGGCO4OKBUIUOBKJ2PKSE5DJTFVNHF3NHZRY3N5LMZG2ODVN63TXEJOKT5C3H2IWXAWFC32V4GMSXYIA2NOVDG54GLAZZ3A",
            "x-tt-request-tag": "s=-1",
            "x-tt-trace-id": "00-11798f870d23c6070e00477647bd0468-11798f870d23c607-01"
        }

        query_str = urlencode(query, safe='/', quote_via=quote) + '&'
        print(query_str)
        common_str = urlencode(common)
        header['x-common-params-v2'] = common_str
        headers = header | cls.encrypt_header(f"{query_str}{common_str}", None, common['device_id'])

        print(headers)
        requests.packages.urllib3.disable_warnings()
        resp = requests.get(
            url=f"https://api5-core-c-lf.amemv.com/aweme/v2/feed/?{query_str}",
            headers=headers,
            verify=False,
            proxies={},
            timeout=15)
        print(resp.content)

    @classmethod
    def get_comment(cls):
        # https://api5-normal-c-hl.amemv.com/aweme/v2/comment/list/?hotsoon_filtered_count=0&top_query_word=&aweme_id=7136036092108672296&count=20&hotsoon_has_more=0&is_familiar=0&forward_page_type=1&channel_id=0&item_type=0&city=350200&cursor=0&gps_access=5&follower_count=0&insert_ids=&page_resource=0&
        query = {
            "aweme_id": "7104196251775716643",
            "channel_id": "0",
            "city": "350200",
            "count": "20",
            "cursor": "0",
            "follower_count": "0",
            "forward_page_type": "1",
            "gps_access": "5",
            "hotsoon_filtered_count": "0",
            "hotsoon_has_more": "0",
            "is_familiar": "0",
            "item_type": "0",
            "page_resource": "0"
        }

        common = {
            "ac": "WIFI",
            "address_book_access": "2",
            "aid": "1128",
            "appTheme": "light",
            "app_name": "aweme",
            "app_version": "22.0.0",
            "build_number": "220015",
            "cdid": "D2FBD885-164C-47CD-A834-73073425F95D",
            "channel": "App Store",
            "device_id": "2019121803839694",
            "device_platform": "iphone",
            "device_type": "iPhone11,8",
            "iid": "3373720129246568",
            "is_guest_mode": "0",
            "is_vcd": "1",
            "js_sdk_version": "2.66.0.9",
            "mcc_mnc": "46011",
            "minor_status": "0",
            "need_personal_recommend": "1",
            "os_api": "18",
            "os_version": "12.4.1",
            "package": "com.ss.iphone.ugc.Aweme",
            "screen_width": "750",
            "tma_jssdk_version": "2.66.0.9",
            "user_avatar_shrink": "64_64",
            "version_code": "22.0.0"
        }
        headers = {
            # "accept-encoding": "gzip, deflate, br",
            # "cookie": "odin_tt=bd5f7430dca46da078aab1809e9edecc262e2b7e2d374ac0e5816bed8373f8f35d3b79c3dbdfabf20497c531b83e3ed7dad4ab2def3bea191edc61e68ad600b8f38495e0be45b374225d515a48c4c4fc; install_id=3373720129246568; ttreq=1$62088ad9bc3c2a8e3f39a1477b81a775d566944c; passport_csrf_token=178881ed4e940dd27ef367d076bf0709; passport_csrf_token_default=178881ed4e940dd27ef367d076bf0709",
            "passport-sdk-version": "5.12.1",
            "sdk-version": "2",
            "user-agent": "Aweme 22.0.0 rv:220015 (iPhone; iOS 12.4.1; zh_CN) Cronet",
            # "x-argus": "A8bNjDTeKoO6RWSF4L7VLXhq9nyFaxts/Ju37RCJpztcoky8NbFS3Uy9/zlawDMNUI8qrJbRDscYxnAc7VIRK3pv1lYHQxyMiKZRJih6xXbEXZasZ0Xyn3acfz1mxvYMKpJZJQ3wgiQ2ejMzal9qa3bfKgy1O5PfzekiJoBJwfsGfLqjfse9JJlO4P1TIghPD60KI6jaJP3L9NtUc3liAU53wJ9Ix59WUP6MOWbCAX9jN4iWGV0gNCwUeozb6ixKVoA=",
            # "x-common-params-v2": "device_id=2019121803839694&os_version=12.4.1&iid=3373720129246568&app_name=aweme&ac=WIFI&appTheme=light&js_sdk_version=2.66.0.9&version_code=22.0.0&channel=App%20Store&is_vcd=1&tma_jssdk_version=2.66.0.9&os_api=18&need_personal_recommend=1&device_platform=iphone&device_type=iPhone11,8&is_guest_mode=0&build_number=220015&minor_status=0&aid=1128&mcc_mnc=46011&screen_width=750&package=cn.zxlee.ZXHookUtil.ZXHookUtilMoney&cdid=D2FBD885-164C-47CD-A834-73073425F95D&app_version=22.0.0&user_avatar_shrink=64_64&address_book_access=2",
            # "x-gorgon": "84042001f8012ec7f3b6ff4fd6dc329696f2e1f93b5c84878de2",
            # "x-khronos": "1662449787",
            # "x-ladon": "9hwmYYbqnz1Xxv0zMsGzbvQsymNvv7ZVC3VhgAJ8TVP9VBZK",
            "x-ss-dp": "1128",
            # "x-tt-dt": "AAA3DKFBFZGJTH7D4YJYZQZRKZCMWBPNT74VGCYQDTJJMMPBZ2VCUWOSEMZZ4CRWNNY3LFM7POXI2PCESLBMHCJ4HTC3BJM2WTHEHTGDENN74TIQ3QTV242PRU5FQFF6OXK5I7SOUUNTA5HUEWYQL4A",
            "x-tt-request-tag": "s=-1",
            # "x-tt-trace-id": "00-11ba9c5e0d72c616de048ce017590468-11ba9c5e0d72c616-01",
            "x-vc-bdturing-sdk-version": "2.2.7"

        }

        query_str = urlencode(query, safe='/,', quote_via=quote) + '&'
        print(query_str)
        common_str = urlencode(common)
        headers['x-common-params-v2'] = common_str
        headers = headers | cls.encrypt_header(f"{query_str}{common_str}", None, common['device_id'])
        requests.packages.urllib3.disable_warnings()
        resp = requests.get(
            url=f"https://api5-normal-c-hl.amemv.com/aweme/v2/comment/list/?{query_str}",
            headers=headers,
            verify=False,
            timeout=30)
        # print(resp.text)
        # print(str(resp.content, "utf-8"))
        data = json.loads(str(resp.content, "utf-8"))
        print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    # TestCommon.get_feed()
    TestCommon.get_comment()
