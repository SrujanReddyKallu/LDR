import base64
from PIL import Image
import websockets
import asyncio
import io
from io import StringIO
import PIL.Image
async def hello():
    async with websockets.connect(' wss://1nwc930hd6.execute-api.ap-southeast-1.amazonaws.com/sws') as websocket:
        p=""
        for i in range(0,101):
                myimg = await websocket.recv()
                p=p+myimg[7:]
                print(p)
                print(len(p))
        print(len(p))
        sample_string_bytes = p.encode("ascii")
        with open("imageToSave.jpg", "wb") as fh:
            fh.write(base64.decodebytes(sample_string_bytes))
asyncio.get_event_loop().run_until_complete(hello())