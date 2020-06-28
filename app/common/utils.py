import requests
import subprocess
from multiprocessing import Pool
from config.model_config import MODEL_URLS


def run_subprocess(model_args):
    model_name = model_args[0]
    model_url = model_args[1]
    args = ['wget', f'./model/{model_name}', model_url]


def download_models():
    assert isinstance(MODEL_URLS, dict)
    map(run_subprocess, zip(MODEL_URLS.keys(), MODEL_URLS.values()))
