#
#  climatology/commands.py
#
#  Created by Clément Malonda on 23/01/2024.

import os
import requests
from dotenv import load_dotenv

from stations import BASIC_URL


def get__station_info_6m(id_station: str, start_date: str, end_date: str) -> str:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    if not api_token:
        raise ValueError("API_TOKEN not found in environment variables.")
    
    request_url = BASIC_URL + "commande-station/infrahoraire-6m"
    headers = {"accept": "*/*", "apikey": api_token}
    params = {"id-station": id_station, "date-deb-periode": start_date, "date-fin-periode": end_date}

    response = requests.get(request_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get__station_info_hourly(id_station: str, start_date: str, end_date: str) -> str:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    if not api_token:
        raise ValueError("API_TOKEN not found in environment variables.")

    request_url = BASIC_URL + "commande-station/horaire"
    headers = {"accept": "*/*", "apikey": api_token}
    params = {"id-station": id_station, "date-deb-periode": start_date, "date-fin-periode": end_date}

    response = requests.get(request_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get__station_info_daily(id_station: str, start_date: str, end_date: str) -> str:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    if not api_token:
        raise ValueError("API_TOKEN not found in environment variables.")
    
    request_url = BASIC_URL + "commande-station/quotidienne"
    headers = {"accept": "*/*", "apikey": api_token}
    params = {"id-station": id_station, "date-deb-periode": start_date, "date-fin-periode": end_date}

    response = requests.get(request_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()