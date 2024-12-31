import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    results = await asyncio.gather(*coros)
    return ''.join(i for i in sorted(results,
                   key=lambda x: x.number))
