import os
import requests
from datetime import datetime
import logging
import pandas
import json


os.environ["NO_PROXY"] = "localhost,127.0.0.1"

data_cache = {}
print(os.getcwd())
with open("/private/musiv/tmp/ert-data/storage_server.json")  as f:
    auth = json.load(f)

def get_url():
    return  auth["urls"][0]

def get_auth():
    return ("__token__", auth["authtoken"])

def get_data(data_url):
    logging.info(f"Getting data from {data_url}...")
    http_response = requests.get(data_url, auth=get_auth())
    http_response.raise_for_status()

    logging.info(" done!")
    return http_response.text.split(",")


def get_numeric_data(data_url):
    data = get_data(data_url)
    return [eval(d) for d in data]


def get_csv_data(data_url):
    response = requests.get(data_url,auth=get_auth(), stream=True)
    return pandas.read_csv(response.raw, names=["value"])


def get_ensembles():
    server_url = get_url()
    data_cache["ensembles"] = get_schema(f"{server_url}/ensembles")["ensembles"]
    return data_cache["ensembles"]


def get_ensemble_url(ensemble_id):
    server_url = get_url()
    url = f"{server_url}/ensembles/{ensemble_id}"
    return url


def get_schema(api_url):
    logging.info(f"Getting json from {api_url}...")
    http_response = requests.get(api_url, auth=get_auth())
    http_response.raise_for_status()

    logging.info(" done!")
    return http_response.json()
