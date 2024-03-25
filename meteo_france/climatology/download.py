#
#  climatology/downloads.py
#
#  Created by Clément Malonda on 23/01/2024.

import os
import aiohttp
from dotenv import load_dotenv

from .config import BASIC_URL

async def get_file(id_cmd: int) -> str:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    request_url = BASIC_URL + "/commande/fichier"
    headers = {"accept": "*/*", "apikey": api_token}
    params = {"id-cmde": id_cmd}

    if not api_token:
        raise ValueError("API_TOKEN not found in environment variables.")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(request_url, params=params, headers=headers) as response:
            if response.status == 201:
                return await response.text()
            else:
                if response.status == 204:
                    print(f"Status {response.status} : Production still pending or in progress")
                elif response.status == 404:
                    print(f"Status {response.status} : Command number does not exist")
                elif response.status == 410:
                    print(f"Status {response.status} : Production already delivered")
                elif response.status == 500:
                    print(f"Status {response.status} : Production completed, failure")
                elif response.status == 507:
                    print(f"Status {response.status} : Production rejected by the system (too large)")
                else:
                    print(f"Status {response.status}")