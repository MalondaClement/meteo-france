#
#  vigilance/vigilance.py
#
#  Created by Clément Malonda on 25/03/2024.

import requests

from .config import BASIC_URL

def get_vigilance(api_token: str) -> str:
    if not api_token:
        raise ValueError("Missing API token")
    
    request_url = BASIC_URL + "/textesvigilance/encours"
    headers = {"accept": "*/*", "apikey": api_token}

    response = requests.get(request_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_vigilance_map(api_token: str) -> str:
    if not api_token:
        raise ValueError("Missing API token")
    
    request_url = BASIC_URL + "/cartevigilance/encours"
    headers = {"accept": "*/*", "apikey": api_token}

    response = requests.get(request_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_vigilance_image_J(api_token: str):
    if not api_token:
        raise ValueError("Missing API token")

    request_url = BASIC_URL + ""
    headers = {"accept": "*/*", "apikey": api_token}

    response = requests.get(request_url, headers=headers)

    if response.status_code == 200:
        img = response.raw
        return img
    else:
        response.raise_for_status()

def get_vigilance_image_J1(api_token: str):
    if not api_token:
        raise ValueError("Missing API token")

    request_url = BASIC_URL + ""
    headers = {"accept": "*/*", "apikey": api_token}

    response = requests.get(request_url, headers=headers)

    if response.status_code == 200:
        img = response.raw
        return img
    else:
        response.raise_for_status()

def get_vigilance_image_J_J1(api_token: str):
    if not api_token:
        raise ValueError("Missing API token")

    request_url = BASIC_URL + ""
    headers = {"accept": "*/*", "apikey": api_token}

    response = requests.get(request_url, headers=headers)

    if response.status_code == 200:
        img = response.raw
        return img
    else:
        response.raise_for_status()
