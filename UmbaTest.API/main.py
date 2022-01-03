import uvicorn

from Services.logics import UserService
import fastapi

router = fastapi.FastAPI()


@router.get('/api/1/get_user')
async def get_all_user():
    resp = await UserService.get_users()
    print(resp)
    return resp


uvicorn.run(router)
