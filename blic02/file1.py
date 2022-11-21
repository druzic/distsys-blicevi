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
                joke = await asyncio.gather(*joke)
                user = await asyncio.gather(*user)
                joke = [await x.json() for x in joke]
                user = [await y.json() for y in user]

                task = asyncio.create_task(filterUsers(user, session))
                task2 = asyncio.create_task(filterUsers(user, session))
                await task
                await task2

            return web.json_response({"status":"ok", "user":user, "joke":joke}, status=200)
    except Exception as e:
        return web.json_response({"status" : "failed", "message" : str(e)}, status=500)


async def filterUsers(user, session):
    for x in range(len(user)):
        async with session.post("http://localhost:8081/filterUsers", json=user[x]) as response:
            rez = await response.text()
    return rez

async def filterJokes(joke, session):
    for x in range(len(joke)):
        async with session.post("http://localhost:8082/filterJokes", json=joke[x]) as response:
            rez = await response.text()
    return rez

app = web.Application()

app.router.add_routes(routes)

web.run_app(app)