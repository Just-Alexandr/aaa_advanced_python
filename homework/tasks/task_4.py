async def task_1(i: int, order=''):

    order += '1'

    if i == 0:
        return order

    if i > 5:
        return await task_2(i // 2, order)
    else:
        return await task_2(i - 1, order)


async def task_2(i: int, order=''):

    order += '2'

    if i == 0:
        return order

    if i % 2 == 0:
        return await task_1(i // 2, order)
    else:
        return await task_2(i - 1, order)


async def coroutines_execution_order(i: int = 42) -> int:
    order = await task_1(i)
    return order
