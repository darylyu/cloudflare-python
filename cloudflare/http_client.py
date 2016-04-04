# -*- coding: utf-8 -*-
from .config import email, api_key

import requests
DEFAULT_API_HOST = 'https://api.cloudflare.com/client/v4'

class CloudFlareClient(object):

    def __init__(self, api_host=DEFAULT_API_HOST, email=email, api_key=api_key):
        # api_host, email, api_key are optional.
        # If they are not explicitly set, it is assumed that
        # it is used within this package so it gets the auth information
        # from config.JSONConfigReader which in turn gets
        # it from ~/.cloudflare.jsonl
        self.api_host = api_host
        self.email = email
        self.api_key = api_key

        # pre=configure the auth requirements
        self.headers = {}
        self.headers['X-Auth-Email'] = email
        self.headers['X-Auth-Key'] = api_key
        self.headers['Content-Type'] = 'application/json'

    def __get__(self, end_point, query_params={}):
        full_url = '%s%s' % (self.api_host, end_point)
        response = requests.get(full_url, headers=self.headers)
        return response

    def list_zones(self):
        # https://api.cloudflare.com/#zone-list-zones
        end_point = '/zones'
        response = self.__get__(end_point)
        return response
