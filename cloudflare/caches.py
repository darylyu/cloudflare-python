# -*- coding: utf-8 -*-
import requests

from .http_client import CloudFlareClient


def purge(url):
    cfc = CloudFlareClient()
    response = cfc.purge_cache(url)
