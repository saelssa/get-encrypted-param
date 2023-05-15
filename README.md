# Get-Encrypted-Param | [获取算法参数](README-zh.md)

This is an example of getting 抖音/TikTok encryption algorithm parameters

Support iOS | Android | Web

For example to get x_ladon,x_gorgon,x_argus,x_cylons

## Running the tests

#### REQUEST - [Example one For iOS](demo/iOS/get_param.py)

        @staticmethod
        def get_x_ladon():
            param1 = XLadon.decrypt("ltCyalMN4I88MKaornPKU+LSy5Tl6jDZcJFrMF3eokqTucfp")
            print(param1)

            param2 = XLadon.encrypt(1646098215, "1225625952")
            print(param2)

            param3 = XLadon.decrypt(param2)
            print(param3 == param1)

#### RESULT

        96edab6bc5bf2fbc0000000021080304621d7727
        8404e03220003523b7c16d6cea06cece05f6e6c9d178d376f661
        True

#### REQUEST headers [Example one For Android latest version](demo/Android/args.py)

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

#### RESULT

        {
            'X-Ladon': 'GjVnM5oGh07q8+r1zyFSvBBSdm6CsSfatvZkVGBgFjTKocce', 
            'X-Khronos': '1669644559', 
            'X-Argus': '2OVfa6g340YqI8N32Lrx8bn7boeqGmNpZHG24JtPbUFjfAYzOxI7vvuCUOEAe2UIALIP0BBHKhggZ92BzXwl56RceKLBqSowkEFwGpfHzpiJ/fDDJ+KcjgaezyUf9rDFTrKfccgsNHgfc1TK3KxV7ZJUoARag6Gk7qc7cKyyDYT4CvweecGkNL+mbKpXnA4QyT8c0FDy8bg9GnFZny7BjT4mMAynvD0WpoTRIPB74QzrOA==', 
            'X-Gorgon': '0404c0f20890010ef978d9b83ac6d3c165d6b8cb3c28e37d0c2f', 
            'X-Tyhon': 'wDr8Tj55shx6Y/xOcXiuCms2/AFwZLgbPjb8Pto='
        }

#### REQUEST headers [Example one For Web](demo/web/get_web_comment.py)

##### Need to replace your own cookie

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

#### RESULT  a part

            'aweme_id': '7158666747749338382','can_share': True, 
            'cid': '7158668053982561054', 'create_time': 1666757299, 
            'digg_count': 543, 'image_list': None,'ip_label': '四川', 
            'is_author_digged': False, 
            'is_hot': False, 'is_note_comment': 0, 'label_list': None, 
            'label_text': '作者', 'label_type': 1, 'reply_comment': None, 
            'reply_id': '7158666854272205605', 'reply_to_reply_id': '0', 
            'status': 1, 'text': '我明早还去那，希望你们来。', 'text_extra': [], 
            'text_music_info': None, 'user': {'accept_private_policy': False, 
            'account_region': '', 'ad_cover_url': None, 'apple_account': 0, 
            'authority_status': 0, 
            'avatar_168x168': 
            {
                'height': 720, 'uri': '168x168/aweme-avatar/tos-cn-avt-0015_28b1fbeeb091e03e1e1e06cef5e07795', 
                'url_list': ['https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_28b1fbeeb091e03e1e1e06cef5e07795~c5_168x168.jpeg?from=2956013662'], 
                'width': 720
            }

## Environment requirements

Test with China version,To test the American version or the European version,you need to replace the data
in [this](demo/iOS/bean/device_info.py)

        Support iOS | Android | Web
        Python 3.9.7
        PyCharm 2022.2.1
        China_Android_app_version = '23.2.0'
        China_iOS_app_version = '22.0.0'

## Tip

[Contact](https://t.me/Qtzbyliix)

