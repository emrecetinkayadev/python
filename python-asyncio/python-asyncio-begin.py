import asyncio
from random import randint
import aiohttp
import time
from functools import wraps

MAX_POKEMON = 898


# Time counter for performans purpose.
def time_counter(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(
            f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


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


@time_counter
async def main() -> None:
    time_before = time.perf_counter()
    for _ in range(20):
        pokemon_name = await get_random_pokemon_name()
        print(pokemon_name)
    print(f"Total time (synchronous: {time.perf_counter() - time_before})")

    time_before = time.perf_counter()
    result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
    print(result)
    print(f"Total time (asynchronous: {time.perf_counter() - time_before})")


if __name__ == "__main__":
    asyncio.run(main())
