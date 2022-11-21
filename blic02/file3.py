import aiohttp
import asyncio
import time
import aiosqlite


from aiohttp import web

routes = web.RouteTableDef()

@routes.post("/filterJokes")
async def filterJokes(request):
    try:
        json = await request.json()
        filtered = {}

        return web.json_response({"status": "OK"}, status=200)
    except Exception as e:
        return web.json_response({"Status S3" : str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)