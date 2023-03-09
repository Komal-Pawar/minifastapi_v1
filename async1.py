import asyncio


async def main():            # 'main' is 'coroutins'
    print("hello")
    await asyncio.sleep(1)   # a running function is a middle
    print("world")

asyncio.run(main())




