import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getJokes")
async def getJokes(request):
    try:
        async with aiohttp.ClientSession() as session:
            for i in range(6):
                joke = []
                user = []
                for _ in range(2):
                    joke.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
                    user.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
                res = await asyncio.gather(*joke)
                user = await asyncio.gather(*user)
                joke = [await x.json() for x in res]
                user = [await y.json() for y in user]


            return web.json_response({"status":"ok", "data":user}, status=200)
    except Exception as e:
        return web.json_response({"status" : "failed", "message" : str(e)}, status=500)


async def filterUsers(users, session):
    for x in range(len(users)):
        async with session.post("http://0.0.0.0:8081/filterUsers", json=users[x]) as response:
            rez= await response.text()
    return rez

app = web.Application()

app.router.add_routes(routes)

web.run_app(app)