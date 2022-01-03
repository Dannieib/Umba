import httpx

from Services.httpservices import HttpServiceHelper


async def get_users():
    data = await HttpServiceHelper.get_github_users()
    print(data)
    if data:
        # save here to sqlite.
        for user in data:
            return user
    return data

    # return data

