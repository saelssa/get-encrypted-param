from __future__ import annotations

import json
import random
from hashlib import md5
from typing import Any

import requests

from demo.bean.protobuf import ProtoBuf
from demo.api.hash import dp_hash


class Api:
    URL = "http://27.50.54.23/result"
    TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJ0aWFsaSIsInBsYXQiOiJ3ZWFhMTIiLCJleHAiOjE2Njk0Mjc0OTUsInVzZXJuYW1lIjoidGlhbGkifQ.PzqR45pew9j4PNSf_WD9Z27pm2L06T03IxiejkRHo_8"

    # You need to replace your own region ID
    appId = 1128  # appId 1180-American 1233-European
    PROXIES = {}

    @classmethod
    def send(cls, func: str, params: list[str]) -> Any | None:
        headers = {
            'content-type': "application/json",
            'x-token': cls.TOKEN
        }
        resp = requests.post(
            url=cls.URL,
            headers=headers,
            json={
                'appId': cls.appId,
                'function': func,
                'params': params
            },
            proxies=cls.PROXIES)
        if resp.status_code != 200:
            raise Exception("Signature network exception!")
        result: dict = json.loads(resp.content)
        if result['code'] != 0:
            print("Signature interface exception:", result['msg'])
            raise Exception(result['msg'])
        return result['data']


class XLadon:
    @staticmethod
    def encrypt(x_khronos: int, lc_id: str) -> str:
        # encrypt X-Ladon String
        return Api.send('XLadon_encrypt', [
            "{}-{}-{}".format(x_khronos, lc_id, Api.appId),
            str(Api.appId)
        ])

    @staticmethod
    def decrypt(x_ladon: str) -> str:
        # encrypt X-Ladon String
        return Api.send('XLadon_decrypt', [
            x_ladon,
            str(Api.appId)
        ])


class XGorgon:
    @staticmethod
    def build(url_query: str, x_ss_stub: str, sdk_ver: int, x_khronos: int) -> str:
        default_str = '00000000'
        if url_query is None or len(url_query) == 0:
            url_query_md5_hex = md5(b'').hexdigest()[0:8]
        else:
            url_query_md5_hex = md5(url_query.encode('utf-8')).hexdigest()[0:8]

        if x_ss_stub is None or len(x_ss_stub) == 0:
            x_ss_stub = default_str
        else:
            x_ss_stub = x_ss_stub[0:8]

        sdk_ver_hex = sdk_ver.to_bytes(4, 'little').hex()
        time_hex = x_khronos.to_bytes(4, 'big').hex()
        build_str = url_query_md5_hex + x_ss_stub + default_str + sdk_ver_hex + time_hex
        return XGorgon.encrypt(build_str)

    @staticmethod
    def encrypt(build_str: str) -> str:
        return Api.send('XGorgon_encrypt', [
            build_str
        ])

    @staticmethod
    def decrypt(x_gorgon: str) -> str:
        return Api.send('XGorgon_decrypt', [
            x_gorgon
        ])


class XCylons:
    @staticmethod
    def encrypt(query_md5_hex: str, lc_id: str, timestamp: int) -> str:
        return Api.send('XCylons_encrypt', [
            query_md5_hex,
            lc_id,
            str(timestamp)
        ])

    @staticmethod
    def decrypt(x_cylons: str) -> str:
        return Api.send('XCylons_decrypt', [
            x_cylons
        ])


class XArgus:
    @staticmethod
    def decrypt(x_argus: str) -> ProtoBuf:
        resp = Api.send('XArgus_decrypt', [x_argus])
        return ProtoBuf(bytes.fromhex(resp))

    @staticmethod
    def encrypt(x_argus: ProtoBuf) -> str:
        return Api.send('XArgus_encrypt', [x_argus.toBuf().hex()])

    @staticmethod
    def build(x_argus_simple_bean: dict) -> str:
        '''
        xargus_simple_bean = {
            'deviceID':         device_id,  #can be null
            'licenseID':        lc_id,
            'appVersion':       app_version,
            'sdkVersionStr':    sdk_ver_str,
            'sdkVersion':       sdk_ver,
            'x_khronos':        x_khronos,
            'x_ss_stub':        x_ss_stub, #request for get can be null
            'secDeviceToken':   "AnPPIveUCQlIiFroHGG17nXK6", #can be null
            'queryHex':         query_str.encode('utf-8').hex(),
            'x_bd_lanusk': '',  #/passport/user/login/ Return header data,If you need to like and follow, you need this
        }
        '''
        return Api.send('XArgus_build', [
            json.dumps(x_argus_simple_bean).encode('utf-8').hex()
        ])

    @staticmethod
    def get_body_hash(x_ss_stub=None):
        if x_ss_stub is None or len(x_ss_stub) == 0:
            return dp_hash(bytes(16))[0:6]
        return dp_hash(bytes.fromhex(x_ss_stub))[0:6]

    @staticmethod
    def get_query_hash(query: str):
        if query is None or len(query) == 0:
            return dp_hash(bytes(16))[0:6]
        return dp_hash(query.encode('utf-8'))[0:6]

    @staticmethod
    def get_psk_hash(x_bd_lanusk: str):
        if x_bd_lanusk is None or len(x_bd_lanusk) == 0:
            return None
        if type(x_bd_lanusk) == bytes:
            return x_bd_lanusk
        return md5(x_bd_lanusk.encode('utf-8')).digest()

    @staticmethod
    def get_psk_cal_hash(query: str, x_ss_stub: str):
        body_hash = bytes(16)
        if x_ss_stub is not None and len(x_ss_stub) != 0:
            body_hash = bytes.fromhex(x_ss_stub)
        buf = query.encode('utf-8') + body_hash + '0'.encode('utf-8')
        return dp_hash(buf)

    @staticmethod
    def build_local(params: dict) -> str:
        '''
        params = {
            'deviceID': '',
            'licenseID': '',
            'appVersion': '',
            'sdkVersionStr': '',
            'sdkVersion': 0,
            'x_khronos': 0,
            'x_ss_stub': '',  #request for get is null
            'secDeviceToken': '', #can be null
            'query': '',
            'x_bd_lanusk': '',    #return after login
        }
        '''
        env_code = 0x120
        queryHash = XArgus.get_query_hash(params['query'])
        bodyHash = XArgus.get_body_hash(params['x_ss_stub'])
        psk_hash = XArgus.get_psk_hash(params['x_bd_lanusk'])
        if psk_hash is not None:
            pskVersion = '0'
            pskCalHash = XArgus.get_psk_cal_hash(params['query'], params['x_ss_stub'])
        else:
            pskVersion = 'none'
            pskCalHash = None

        xa_bean = {
            1: 0x20200929 << 1,  # magic
            2: 2,  # version
            3: random.randint(0, 0x7FFFFFFF),  # rand
            4: str(Api.appId),  # msAppID
            5: params['deviceID'],  # deviceID
            6: params['licenseID'],  # licenseID
            7: params['appVersion'],  # appVersion
            8: params['sdkVersionStr'],  # sdkVersionStr
            9: params['sdkVersion'] << 1,  # sdkVersion
            10: env_code.to_bytes(8, 'little'),  # envcode  prison break detection
            11: 1,  # platform
            12: params['x_khronos'] << 1,  # createTime
            13: bodyHash,  # bodyHash
            14: queryHash,  # queryHash
            15: {
                1: 172,  # signCount
                2: 1388734,  # reportCount
                3: 1388734,  # settingCount
            },
            16: params['secDeviceToken'],  # secDeviceToken
            17: params['x_khronos'] << 1,  # isAppLicense
            18: psk_hash,  # pskHash
            19: pskCalHash,  # pskCalHash
            20: pskVersion,  # pskVersion
            21: 738,  # callType
        }
        xa_pb = ProtoBuf(xa_bean)
        return XArgus.encrypt(xa_pb)


class TokenReqCryptor:
    @staticmethod
    def encrypt(_hex: str) -> str:
        return Api.send('TokenReq_encrypt', [_hex])

    @staticmethod
    def decrypt(_hex: str) -> str:
        return Api.send('TokenReq_decrypt', [_hex])


class TCCryptor:
    @staticmethod
    def encrypt(_hex: str) -> str:
        return Api.send('TCCryptor_encrypt', [_hex])

    @staticmethod
    def decrypt(_hex: str) -> str:
        return Api.send('TCCryptor_decrypt', [_hex])
