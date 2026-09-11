# E55.Async I/O in Python.
import time;
import asyncio;
import requests;
async def function1():
    print("Func 1")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    return "Himanshu"
async def function2():
    print("Func 2")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)
async def function3():
    print("Func 3")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
async def main():
    # await function1().
    # await function2().
    # await function3().
    # return 3.
    L = await asyncio.gather(
            function1(),
            function2(),
            function3(),
        )
    print(L)
    # task = asyncio.create_task(function1()).
    # await function1().
    # await function2().
    # await function3().
asyncio.run(main())