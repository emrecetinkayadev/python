import asyncio

async def main():
    print("tim")
    await asyncio.create_task(foo("text"))
    # await task
    await asyncio.sleep(0)
    print("finished")


async def foo(text):
    await asyncio.sleep(10)
    print(text)

asyncio.run(main())
