import aiohttp
import asyncio
import time
import aiosqlite


from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterUsers")
async def filterUsers(request):
    request = await request.json()


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)