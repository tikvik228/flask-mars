import asyncio
COEFF = 0.001


async def sowing(*data):
    tasks = []
    for p in data:
        tasks.append(process_plant(*p))
        tasks.append(fertilize(p[0]))
        tasks.append(treatment(p[0]))
    await asyncio.gather(*tasks)


async def process_plant(name, water_time, grow_time, pik_time):
    print(f"0 Beginning of sowing the {name} plant")
    await soak(name, water_time)
    await shelter(name, grow_time)
    await pik(name, pik_time)
    print(f"9 The seedlings of the {name} are ready")


async def soak(name, water_time):
    print(f"1 Soaking of the {name} started")
    await asyncio.sleep(water_time * COEFF)
    print(f"2 Soaking of the {name} is finished")


async def shelter(name, grow_time):
    print(f"3 Shelter of the {name} is supplied")
    await asyncio.sleep(grow_time * COEFF)
    print(f"4 Shelter of the {name} is removed")


async def pik(name, pik_time):
    print(f"5 The {name} has been transplanted")
    await asyncio.sleep(pik_time * COEFF)
    print(f"6 The {name} has taken root")


async def fertilize(name):
    print(f"7 Application of fertilizers for {name}")
    await asyncio.sleep(3 * COEFF)
    print(f"7 Fertilizers for the {name} have been introduced")


async def treatment(name):
    print(f"8 Treatment of {name} from pests")
    await asyncio.sleep(5 * COEFF)
    print(f"8 The {name} is treated from pests")
