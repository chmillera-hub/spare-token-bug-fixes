# Tests four questions about asyncio.Condition.notify_all (Python forum topic 90932)
import asyncio, sys, time

async def q1_two_notifies():
    cond = asyncio.Condition(); wakeups = 0
    async def waiter():
        nonlocal wakeups
        async with cond:
            while True:
                await cond.wait(); wakeups += 1
    t = asyncio.create_task(waiter()); await asyncio.sleep(0.01)
    async with cond: cond.notify_all()
    async with cond: cond.notify_all()                 # second notify before the waiter had a chance to run
    await asyncio.sleep(0.05); t.cancel()
    return wakeups

async def q2_is_notify_all_a_coroutine():
    cond = asyncio.Condition()
    async with cond:
        return asyncio.iscoroutinefunction(cond.notify_all), cond.notify_all()

async def q3_timing(n):
    cond = asyncio.Condition(); woken = 0
    async def waiter():
        nonlocal woken
        async with cond:
            await cond.wait(); woken += 1
    tasks = [asyncio.create_task(waiter()) for _ in range(n)]; await asyncio.sleep(0.05)
    async with cond:
        t = time.perf_counter(); cond.notify_all(); dt = time.perf_counter() - t
    await asyncio.gather(*tasks)
    return dt * 1000, woken

async def q4_order():
    cond = asyncio.Condition(); log = []
    async def waiter(name):
        async with cond:
            while True:
                await cond.wait(); log.append(name)
    tasks = [asyncio.create_task(waiter(c)) for c in "ABC"]; await asyncio.sleep(0.01)
    for _ in range(3):
        async with cond: cond.notify_all()
        await asyncio.sleep(0.01)
    for t in tasks: t.cancel()
    return "".join(log)

async def main():
    print("Python", sys.version.split()[0])
    print("1. two notify_all calls before the waiter runs -> the waiter loop ran", await q1_two_notifies(), "time(s)")
    print("2. notify_all is a coroutine function (something that can be suspended half way):", (await q2_is_notify_all_a_coroutine())[0])
    for n in (10, 200, 20000):
        ms, woken = await q3_timing(n)
        print(f"3. notify_all with {n} waiting clients took {ms:.3f} ms | clients woken: {woken}")
    print("4. order of wake-ups over three rounds with clients A, B and C:", await q4_order())
    broken = asyncio.Condition
    try:
        async with broken: pass
    except Exception as e: print("5. the posted line 'broadcast_condition = asyncio.Condition' (no parentheses) fails at 'async with':", type(e).__name__)
asyncio.run(main())
