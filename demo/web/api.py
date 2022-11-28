from __future__ import annotations

import json
from typing import Any

import requests


class SignApi(object):
    URL = "http://i.argso.vip:5000/sign"

    @classmethod
    def send(cls, data: dict) -> Any | None:
        resp = requests.post(
            cls.URL,
            headers={
              "x-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjA5ODdaIiwiZXhwIjoxNjcwMjQ4NjgyfQ.oHffsyaJ3tth5QpvjUc8I2mpN2zpvNHR_cnlHrS--ks"
            },
            json=data
        )
        # print("status:", resp.status_code)
        if resp.status_code != 200:
            raise Exception(f"api{cls.URL} network error")
        result: dict = json.loads(resp.content)
        # print("body:", json.dumps(result, indent=4, ensure_ascii=False))
        if result['code'] != 0:
            raise Exception(f"api{cls.URL}return error:", result['msg'])
        return result['data']

    @classmethod
    def get_sign(cls, query, path, ua):
        data = {'path': path, 'query': query, 'ua': ua}
        return SignApi.send(data)