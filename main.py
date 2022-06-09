import aiohttp
from aiohttp import web
import asyncio
import json
from scanner import *
from logging_message import *


async def handle(request):
    response_obj = {' status ': 'success'}
    return web.Response(text=json.dumps(response_obj), status=200)


async def scan(request):
    try:
        ip = request.query['ip']
        begin_port = request.query['begin_port']
        end_port = request.query['end_port']
        result = receive_open_ports(ip, int(begin_port), int(end_port))
        result = {'ip': ip, 'result': [result]}
        send_log("success")
        return web.Response(text=json.dumps(result), status=200)
    except Exception as e:
        send_log(str(e) + ' in scan in main.py')
        print(e, ' something went wrong')


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/scan', scan)

web.run_app(app)
