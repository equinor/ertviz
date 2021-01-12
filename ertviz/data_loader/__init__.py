import os
import requests
import logging
import pandas


def get_info(project_id=None):
    from ert_shared.storage.connection import get_info

    return get_info(project_id)


os.environ["NO_PROXY"] = "localhost,127.0.0.1"
data_cache = {}


def get_url(project_id=None):
    return get_info(project_id)["baseurl"]


def get_auth(project_id=None):
    return get_info(project_id)["auth"]


def get_csv_data(data_url, project_id=None):
    response = requests.get(data_url, auth=get_auth(project_id), stream=True)
    response.raise_for_status()
    return pandas.read_csv(response.raw, names=["value"])


def get_ensembles(project_id=None):
    server_url = get_url(project_id)
    data_cache["ensembles"] = get_schema(f"{server_url}/ensembles", project_id)[
        "ensembles"
    ]
    return data_cache["ensembles"]


def get_ensemble_url(ensemble_id, project_id=None):
    from ert_shared.storage.paths import ensemble

    server_url = get_url(project_id)
    ensemble_url = ensemble(ensemble_id)
    return f"{server_url}{ensemble_url}"


def get_response_url(ensemble_id, response_id, project_id=None):
    from ert_shared.storage.paths import response

    server_url = get_url(project_id)
    response_url = response(ensemble_id, response_id)
    return f"{server_url}{response_url}"


def get_parameter_url(ensemble_id, parameter_id, project_id=None):
    from ert_shared.storage.paths import parameter

    server_url = get_url(project_id)
    parameter_url = parameter(ensemble_id, parameter_id)
    return f"{server_url}{parameter_url}"


def get_parameter_data_url(ensemble_id, parameter_id, project_id=None):
    from ert_shared.storage.paths import parameter_data

    server_url = get_url(project_id)
    parameter_url = parameter_data(ensemble_id, parameter_id)
    return f"{server_url}{parameter_url}"


def get_schema(api_url, project_id=None):
    logging.info(f"Getting json from {api_url}...")
    http_response = requests.get(api_url, auth=get_auth(project_id))
    http_response.raise_for_status()

    logging.info(" done!")
    return http_response.json()
