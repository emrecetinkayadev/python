import asyncio
from random import randint
import aiohttp
import time
import requests

MAX_POKEMON = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = requests.get(pokemon_url)
    return str(pokemon["name"])


async def get_random_pokemon_name() -> str:
    async with aiohttp.ClientSession() as session:
        pokemon_id = randint(1, MAX_POKEMON)
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            return str(pokemon["name"])


async def main() -> None:
    # Syncronous Programing.
    time_before = time.perf_counter()
    for _ in range(20):
        pokemon_name = await get_random_pokemon_name()
        print(pokemon_name)
    print(f"Total time (synchronous: {time.perf_counter() - time_before})")

    # Asyncronous Programing
    time_before = time.perf_counter()
    result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
    print(result)
    print(f"Total time (asynchronous: {time.perf_counter() - time_before})")


if __name__ == "__main__":
    asyncio.run(main())
