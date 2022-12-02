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
    cookie = ""

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