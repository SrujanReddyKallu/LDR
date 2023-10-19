import base64
# from PIL import Image
import websockets
import io
import base64
import asyncio
async def hello():
    async with websockets.connect(
            'wss://1nwc930hd6.execute-api.ap-southeast-1.amazonaws.com/sws') as websocket:
        with open("hi.jpg", "rb") as img_file:
            my_string = base64.b64encode(img_file.read()).decode('utf-8')
        k=100
        chnk_len=len(my_string) // k
        print(my_string)
        for i in range(0,len(my_string),chnk_len):
            await websocket.send('{"action":"sendmessage" , "message":"'+my_string[i:i+chnk_len]+'"}')
            await asyncio.sleep(0.4)         
        await websocket.send('{"action":"sendmessage" , "message":"'+my_string[-(len(my_string) % k):]+'"}')         
        print(len(my_string))
asyncio.get_event_loop().run_until_complete(hello())
#BY UDAY,PRASHANTH,SRUJAN BABBA