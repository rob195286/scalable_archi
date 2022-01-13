import asyncio
import aiohttp
from complex_features import complex_mapper
from time import sleep


async def mandelbrot_requests(session, data):
    async with session.post('http://127.0.0.1:5000/', json=data) as resp:
        return await resp.json(content_type='text/html')


async def run_request(xmin, xmax, ymin, ymax, delta_between_points, requests_number = 12):
    async with aiohttp.ClientSession() as session:
        requests = [
            mandelbrot_requests(session, {'real': real_part * delta_between_points, 'img': img_part * delta_between_points})
            for real_part in range(xmin, xmax)
            for img_part in range(ymin, ymax)
        ]
        result_requests, tmp = [], []
        i = 0
        for r in requests:
            tmp.append(r)
            if(i % requests_number == 0):
                result_requests.extend(await asyncio.gather(*tmp))
                tmp.clear()
            i += 1
        if(len(tmp) > 0):
            result_requests.extend(await asyncio.gather(*tmp))
        return result_requests


def get_mandelbrot_numbers(xmin, xmax, ymin, ymax, delta_between_points, requests_number = 12):
    loop = asyncio.get_event_loop()
    valid_mandelbrot_number = filter(
        lambda x : x['mandelbrot'],
        loop.run_until_complete(run_request(xmin, xmax, ymin, ymax, delta_between_points, requests_number))
    )
    return list(map(complex_mapper, valid_mandelbrot_number)) # map(function, iterable)



if __name__ == "__main__":
    delta_between_points = 0.014
    count = 8
    xmin, xmax = -count, count
    ymin, ymax = -count, count
    res = get_mandelbrot_numbers(xmin, xmax, ymin, ymax, delta_between_points)
