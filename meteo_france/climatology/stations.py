#
#  climatology/stations.py
#
#  Created by Clément Malonda on 18/01/2024.

import os
import requests
from dotenv import load_dotenv


BASIC_URL = "https://public-api.meteofrance.fr/public/DPClim/v1/"

def get_6m_stations_list(id_departement: int) -> str:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    if not api_token:
        raise ValueError("API_TOKEN not found in environment variables.")
    
    request_url = BASIC_URL + "liste-stations/infrahoraire-6m"
    headers = {"accept": "*/*", "apikey": api_token}
    params = {"id-departement": id_departement}

    response = requests.get(request_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_hourly_stations_list(id_departement: int) -> str:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    if not api_token:
        raise ValueError("API_TOKEN not found in environment variables.")
    
    request_url = BASIC_URL + "liste-stations/horaire"
    headers = {"accept": "*/*", "apikey": api_token}
    params = {"id-departement": id_departement}

    response = requests.get(request_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_daily_stations_list(id_departement: int) -> str:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    if not api_token:
        raise ValueError("API_TOKEN not found in environment variables.")
    
    request_url = BASIC_URL + "liste-stations/quotidienne"
    headers = {"accept": "*/*", "apikey": api_token}
    params = {"id-departement": id_departement}

    response = requests.get(request_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_station_info(id_station: str) -> str:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    if not api_token:
        raise ValueError("API_TOKEN not found in environment variables.")
    
    request_url = BASIC_URL + "information-station"
    headers = {"accept": "*/*", "apikey": api_token}
    params = {"id-station": id_station}

    response = requests.get(request_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
