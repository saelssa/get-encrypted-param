import requests

from api import SignApi


class Demo:
    # https://www.douyin.com/
    path = "aweme/v1/web/comment/list/"
    query = {
        "aid": "6383",
        "aweme_id": "7158666747749338382",
        "browser_language": "zh-CN",
        "browser_name": "Chrome",
        "browser_online": "true",
        "browser_platform": "Win32",
        "browser_version": "106.0.0.0",
        "channel": "channel_pc_web",
        "cookie_enabled": "true",
        "count": "20",
        "cpu_core_num": "6",
        "cursor": "0",
        "device_memory": "8",
        "device_platform": "webapp",
        "downlink": "10",
        "effective_type": "4g",
        "engine_name": "Blink",
        "engine_version": "106.0.0.0",
        "item_type": "0",
        "os_name": "Windows",
        "os_version": "10",
        "pc_client_type": "1",
        "platform": "PC",
        "rcFT": "AAJsDIiJw",
        "round_trip_time": "50",
        "screen_height": "1440",
        "screen_width": "2560",
        "version_code": "170400",
        "version_name": "17.4.0"
    }
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    # replace you cookie
    cookie = "odin_tt=04f97e208f212ae5dd70c79200de62988eb27c0d87ece13e857953b62d704895657a050d0d177c528ec5e26394d703a60002051d730b1f569957e7fae1ba436c787af5b92e85e3a142f6915577f53fd8; MONITOR_WEB_ID=7c1aa56d-b7e1-4d5f-9817-1590ae6933aa; ttwid=1%7CXosrf_GNjk89-RDyKpFCpJ6DAJk-F09WKfYDh8yNTko%7C1663743163%7C9df3534d2102eedcf273103e4139f949e076c3e6b5ec9420212b895656d814cf; __ac_signature=_02B4Z6wo00f01moJ6xQAAIDC6gsRV5-USBpqKe-AAPm-KPdaYRjoHXAQVr3f92HeyukntzKMyks676Gl2Hq0J-M7QsK3zNpdas4gEa4EuQXW.XfVvYRyJp3ZIBbm7IpJOmS7SWlfFv5cnIGee3; home_can_add_dy_2_desktop=%220%22; douyin.com; strategyABtestKey=1664012460.446; s_v_web_id=verify_l8fq201n_GwbGxFv2_HZFb_4X8p_Bt3x_Gcfi3TumQHCt; passport_csrf_token=2e3a334768b92dfcfe2e0a9f738c1881; passport_csrf_token_default=2e3a334768b92dfcfe2e0a9f738c1881; __ac_nonce=0632ed0ad00d8d502ff02; tt_scid=nLHFkArpkZRmg0vIxIroZoSkpskAOsYcV3USZ9E--mmlhlx52kL8SPsdUf2rbVXP3c87; download_guide=%222%2F20220924%22; msToken=2xrDNYP3lD4uFm0rob1fpXZtb9_vnAb8rbhp7i2tFJni24Fjn41W2MlxYqo30FrlMgMmnAYPF8k18fCpkcTMo8Wmm89GHtX_WLuvNnbKvgwcG3EwfiMqvsiM54F34YM=; msToken=bCIMgTU8pSgG9tZc2S4pCsi85YQW4W_4pdT4QPtCCaLG6ldu4hHr-ll2wh5b2OdqArjJcbDWLXE7t_PqbK0el23efiLrMpb880VKFly5KxqPAxokdpl3a9-AA-Neat0="

    @classmethod
    def comment(cls):
        if not cls.cookie or cls.cookie is None:
            raise Exception("replace you cookie")
        sign_url = SignApi.get_sign(cls.query, cls.path, cls.ua)
        print(sign_url)
        headers = {
            'Host': 'www.douyin.com',
            'Cookie': cls.cookie,
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'Connection': 'keep-alive',
            'sec-fetch-dest': 'empty',
            # 'referer': f'https://www.douyin.com/video/{aweme_id}',
            'referer': f'https://www.douyin.com/',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
        response = requests.get(
            url=sign_url,
            headers=headers,
            timeout=20)
        print(response.status_code)
        # print(response.text)
        data = response.json()
        print(data)
        comments = data['comments']
        for i in comments:
            print(i)


if __name__ == '__main__':
    Demo.comment()