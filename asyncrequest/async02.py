#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Demonstrating how to use the asyncio library by utilizing the pokeapi.co
   to perform 150 HTTP GET lookups



The script should execute correctly, but notice how much slower this method is. Answer the following questions:

Q: Why was aiohttp required? Why didn't we just use requests?
A: Within a single thread, requests is a blocking synchronous library. When it is used in conjunction with threads, this does not present a problem, however, if we are working with an asynchronous library, like asyncio, we need a client that behaves aynchronously.
Q: Where can I read more about aiohttp and the design decisions?
A: Read more about the aiohttp client and how it differs from requests library here, https://docs.aiohttp.org/en/latest/http_request_lifecycle.html#why-is-aiohttp-client-api-that-way



   """

# standard library
import asyncio
import time

# python3 -m pip install aiohttp
import aiohttp

# start a timer to determine how quickly these lookups are performed
start_time = time.time()

async def main():

    async with aiohttp.ClientSession() as session:
        # loop from 1 to 150 (non inclusive of 151)
        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'    # number is defined by the range for-loop
            async with session.get(pokemon_url) as resp:     # the coroutine we are defining should be run async with an event loop
                pokemon = await resp.json()         # pass control back to the event loop (do other things until this happens)
                print(pokemon['name'])

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

