from aiohttp import web
import sqlite3


async def write(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    conn = sqlite3.connect('ex.db')
    c = conn.cursor()
    c.execute("INSERT INTO activity VALUES (datetime('now','localtime'),'%s')"%(name))
    conn.commit()
    conn.close()
    return web.Response(text=text)


async def read(request):
    pass






app = web.Application()
app.add_routes([web.get('/read', read),
                web.get('/write/{name}', write)])

if __name__ == '__main__':
    web.run_app(app)