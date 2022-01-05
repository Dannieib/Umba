# from typing import List
import json

import httpx
# import json
# from pydantic import parse_obj_as
#
# from Models import UserModel


async def get_github_users():
    url = 'https://api.github.com/users'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)

    if resp.status_code == 200:
        data = resp.json()
        return data
    else:
        return
