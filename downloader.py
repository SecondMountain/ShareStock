import aiohttp
import asyncio


@asyncio.coroutine
def downloader(cc):
    resp = yield from aiohttp.request('GET', cc)  # <4>
    print(resp.content)
    image = yield from resp.read()  # <5>
##########有问题
    return image


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(downloader("https://segmentfault.com/img/bVQd69?w=203&h=95"))
    # downloader("https://segmentfault.com/img/bVQd69?w=203&h=95")
    loop.close()